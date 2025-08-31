# Delay RTT and Bitrate

A Bash script to simulate network delay and bandwidth caps on specific hosts using Linux `tc`. Handy for testing distributed inference under controlled network conditions.

## Prerequisites
- Linux with `tc` (`iproute2` package)
- `sudo` privileges
- Network privileges (not always available in containers)

## Usage
```bash
sudo bash delay.sh
```

Defaults can be adjusted inside the script:
- HOST_NAMES: list of hostnames or IPs
- NET_CARD: network interface (e.g., enp6s0)
- RTT: round-trip delay (e.g., 100ms)
- BIAS: jitter (e.g., 10ms)
- RATE: max egress bandwidth (e.g., 250mbit)
- BURST: buffer size for spikes
- LATENCY_BUF: max queuing time

## How it works
1.	Splits RTT and bias into one-way delay (applied egress only).
2.	Clears existing tc rules on the interface.
3.	Builds a qdisc stack: prio → netem (delay) → tbf (rate limit).
4.	Resolves each host to IPv4 and attaches filters so only matching traffic is shaped.

## Check applied rules:

`tc -s qdisc show dev <net_card>`