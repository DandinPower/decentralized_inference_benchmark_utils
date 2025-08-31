#!/usr/bin/env bash
set -euo pipefail

# === knobs ===
HOST_NAMES=("192.168.4.20")
NET_CARD="enp6s0"

# latency model: use half on egress so round trip ≈ RTT
RTT="40ms"
BIAS="5ms"

# outbound bandwidth cap (egress only)
RATE="250mbit"
BURST="128k"          # keep modest to avoid big spikes
LATENCY_BUF="500ms"  # max queuing time inside TBF

# --- helpers ---
resolve_ip() {
  local target="$1"
  if [[ "$target" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "$target"
  else
    getent ahosts "$target" \
      | awk '/STREAM/ && $1 ~ /^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$/ {print $1; exit}'
  fi
}

RTT_MS=${RTT%ms}
BIAS_MS=${BIAS%ms}
HALF_RTT_MS=$((RTT_MS / 2))
HALF_BIAS_MS=$((BIAS_MS / 2))

# --- reset egress stack ---
sudo tc qdisc del dev "$NET_CARD" root 2>/dev/null || true

# --- egress: prio -> netem -> tbf ---
sudo tc qdisc add dev "$NET_CARD" root handle 1: prio

# band 3 carries our shaped flows
sudo tc qdisc add dev "$NET_CARD" parent 1:3 handle 30: netem \
  delay "${HALF_RTT_MS}ms" "${HALF_BIAS_MS}ms"

# cap outbound rate after delay
sudo tc qdisc add dev "$NET_CARD" parent 30: handle 31: tbf \
  rate "$RATE" burst "$BURST" latency "$LATENCY_BUF"

# classify: match dst host IPs into band 3
for host in "${HOST_NAMES[@]}"; do
  ip_addr=$(resolve_ip "$host" || true)
  if [[ -z "${ip_addr:-}" ]]; then
    echo "Cannot resolve '$host', skipping."
    continue
  fi
  sudo tc filter add dev "$NET_CARD" protocol ip parent 1:0 prio 1 u32 \
    match ip dst "${ip_addr}/32" flowid 1:3
  echo "Applied egress delay+rate to $host ($ip_addr)"
done

echo "Done. Egress shaping only."
echo "Check: tc -s qdisc show dev $NET_CARD"