# Manual RTT Delay

A Bash script to simulate network latency toward specific hosts using the Linux `tc` (traffic control) utility. Useful for testing how distributed inference behaves under varied network delays.

### Prerequisites

* Linux machine with `tc` (part of the `iproute2` package)
* `sudo` privileges
* `network` privileges (note: these are often unavailable in container environments)

### Usage

```bash
sudo bash delay.sh -n <hostname_or_ip> -c < network_interface > -r <RTT> -b <BIAS>
```

For example:

```bash
sudo bash delay.sh -n 192.168.3.1 -c enp6s0 -r 10ms -b 1ms
```

Options:

* `-n, --names`: Comma-separated list of hostnames or IPs to target
* `-c, --card`: Network interface (e.g., `enp6s0`)
* `-r, --rtt`: Round-trip delay to introduce (e.g., `100ms`)
* `-b, --bias`: Delay bias/jitter (e.g., `10ms`)

### How It Works

1. Parses RTT and bias into one-way delays (half of each).
2. Clears existing `tc` rules on the specified interface.
3. Adds a `prio` qdisc and a `netem` qdisc with the computed delay.
4. Resolves each hostname to an IPv4 address and attaches a `tc filter` to only delay traffic destined for that IP.