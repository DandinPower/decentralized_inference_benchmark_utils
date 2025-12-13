# p2p_zmq_benchmark

A tiny peer-to-peer ZeroMQ (PUSH/PULL) benchmark that sends a single large multipart payload and reports:

- End-to-end one-way latency (sender timestamp to receiver timestamp)
- Approx throughput based on `payload_bytes / latency`

This is mainly useful for controlled experiments (fixed RTT, rate limit, TCP tuning) where you want a quick sanity check for “can my link saturate” style questions.

## Directory structure

```
p2p_zmq_benchmark/
├── README.md
└── zmq_benchmark.cpp
```

## Requirements

1. Tested on Ubuntu/Debian.

```bash
sudo apt update
sudo apt install -y libzmq3-dev cppzmq-dev iproute2 nmap iperf3 net-tools chrony
```

## Build

```bash
g++ zmq_benchmark.cpp -o zmq_bench -lzmq -std=c++17
```

## Usage

This benchmark has two modes:

* `recv`: bind and wait
* `send`: connect, do a warmup send, wait 3 seconds, then do the real benchmark send

### Receiver node (start this first)

```bash
# Listen on port 5555
./zmq_bench recv 5555
```

### Sender node

```bash
# Send to <receiver_ip>:<port> with payload size in BYTES
./zmq_bench send <receiver_ip> 5555 <buffer_size_bytes>
```

Examples:

```bash
# 1 MiB
./zmq_bench send 192.168.4.40 5555 1048576

# 64 MiB
./zmq_bench send 192.168.4.40 5555 67108864
```

### What it prints

* Sender prints send start/stop timestamps for warmup and benchmark.
* Receiver prints recv stop timestamp, computed latency (ms), and throughput (Mbps/Gbps).

Important: latency is derived from wall-clock time on two machines. If clocks are not synced, the latency can be nonsense (even negative).

## Network shaping (bandwidth + latency)

If you want reproducible results, shape the network. This script applies **egress-only** shaping for traffic going to specific destination hosts.

On each node, set:

* `HOST_NAMES` to the remote peers you want to shape traffic to
* `NET_CARD` to the correct NIC (check with `ip link` or `ifconfig`)

Then run:

```bash
#!/usr/bin/env bash
set -euo pipefail

# === knobs ===
HOST_NAMES=("192.168.4.39" "192.168.4.40")
NET_CARD="enp7s0"

# latency model: use half on egress so round trip ≈ RTT
RTT="40ms"
BIAS="5ms"

# outbound bandwidth cap (egress only)
RATE="250mbit"
BURST="128k"          # keep modest to avoid big spikes
LATENCY_BUF="500ms"   # max queuing time inside TBF

RTT_MS=${RTT%ms}
BIAS_MS=${BIAS%ms}
HALF_RTT_MS=$((RTT_MS / 2))
HALF_BIAS_MS=$((BIAS_MS / 2))

resolve_ip() {
  local target="$1"
  if [[ "$target" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "$target"
  else
    getent ahosts "$target" \
      | awk '/STREAM/ && $1 ~ /^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$/ {print $1; exit}'
  fi
}

# reset
sudo tc qdisc del dev "$NET_CARD" root 2>/dev/null || true

# egress: prio -> netem -> tbf
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
```

## Time synchronization (Chrony)

This benchmark relies on synchronized clocks (UTC timestamps).

1. Check Chrony sources:

```bash
chronyc sources
```

2. Check UTC time on every machine:

```bash
date -u +"%Y-%m-%dT%H:%M:%SZ"
```

If machines differ by more than a millisecond-level tolerance, your one-way latency result is not trustworthy.

## TCP tuning (optional but usually necessary for high RTT)

### Disable TCP slow start after idle

This matters for bursty P2P traffic (pipeline parallel style). Without it, you often fail to ramp up fast enough under high RTT.

```bash
sudo sysctl -w net.ipv4.tcp_slow_start_after_idle=0
```

### Increase TCP memory buffers

For RTT = 40 ms and bandwidth = 250 Mbit/s:

* BDP = 0.040 s * 250 Mbit/s = 10 Mbit ≈ 1.25 MB

Set buffers larger than BDP. 4 MB is a reasonable starting point:

```bash
sudo sysctl -w net.core.rmem_max=4194304
sudo sysctl -w net.core.wmem_max=4194304
```

If you still cannot saturate, you may need to adjust additional TCP parameters (rmem/wmem defaults, window scaling, congestion control), but start simple and change one thing at a time.

## Benchmark workflow (recommended)

1. Ensure shaping is applied on BOTH nodes (each node shapes traffic to the other).
2. Ensure Chrony is healthy and clocks are aligned.
3. Start receiver.
4. Run sender with a payload large enough to hit steady-state bandwidth (tens of MiB for high RTT links).

Example:

Receiver:

```bash
./zmq_bench recv 5555
```

Sender:

```bash
./zmq_bench send 192.168.4.40 5555 67108864
```