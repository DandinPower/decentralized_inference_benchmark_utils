#!/usr/bin/env bash
set -euo pipefail

HOST_NAMES=("tw-05.access.glows.ai")
NET_CARD="enp0s3"
RTT="100ms"
BIAS="10ms"

# Function to resolve host or accept raw IP
resolve_ip() {
  local target="$1"
  if [[ "$target" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "$target"
  else
    ip=$(getent ahosts "$target" | awk '/STREAM/ && $1 ~ /^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$/ {print $1; exit}')
    echo "$ip"
  fi
}

RTT_MS=${RTT%ms}
BIAS_MS=${BIAS%ms}
HALF_RTT_MS=$((RTT_MS / 2))
HALF_BIAS_MS=$((BIAS_MS / 2))

sudo tc qdisc del dev "$NET_CARD" root || true
sudo tc qdisc add dev "$NET_CARD" root handle 1: prio
sudo tc qdisc add dev "$NET_CARD" parent 1:3 handle 30: netem delay "${HALF_RTT_MS}ms" "${HALF_BIAS_MS}ms"

for host in "${HOST_NAMES[@]}"; do
  ip_addr=$(resolve_ip "$host")
  if [[ -z "$ip_addr" ]]; then
    echo "Cannot resolve '$host', skipping."
    continue
  fi

  sudo tc filter add dev "$NET_CARD" \
    protocol ip parent 1:0 prio 1 u32 \
    match ip dst "${ip_addr}/32" flowid 1:3
  echo "Applied delay rule to $host ($ip_addr)"
done