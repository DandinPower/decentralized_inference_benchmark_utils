# prima.cpp_benchmark_utils

A collection of tools for benchmarking multi-node prima.cpp ([DandinPower's fork](https://github.com/DandinPower/prima.cpp)), including:

1. prima.cpp commands generator
2. delay.sh
3. gguf-split
4. gguf first split metadata extractor (coming soon)


## prima.cpp Commands Generator

This utility automates the construction of `llama-cli` commands tailored for multi-node inference with `prima.cpp`. It reads a JSON configuration file describing your cluster topology and outputs the exact shell commands for each node.

### Features

* Generates commands for a master node and any number of server nodes
* Supports both single-split and multi-split GGUF models
* Validates key configuration fields to catch common errors early
* Produces ready-to-run `llama-cli` invocations with all required flags

### Prerequisites

* [prima.cpp](https://github.com/DandinPower/prima.cpp) that forked by DandinPower (adding public port configuration and multi splits optimization) 

### Configuration File

Create a JSON file (e.g. `example_config.json`) with the following structure:

```json
{
    "gguf_file": "download/Llama-3.2-1B-Instruct-Q4_K_M-00001-of-00003.gguf",
    "world": 3,
    "ctx_size": 4096,
    "n_predict": 1024,
    "master_node": {
        "layer_window_size": 4,
        "loopback_ip": "127.0.0.1",
        "public_ip": "tw-05.access.glows.ai",
        "data_port": 9000,
        "signal_port": 9001,
        "public_data_port": 25443,
        "public_signal_port": 25751,
        "splits": "0,1,2"
    },
    "server_nodes": [
        {
            "layer_window_size": 8,
            "public_ip": "tw-05.access.glows.ai",
            "data_port": 9000,
            "signal_port": 9002,
            "public_data_port": 25142,
            "public_signal_port": 25450,
            "splits": "0,1"
        },
        {
            "layer_window_size": 4,
            "public_ip": "tw-05.access.glows.ai",
            "data_port": 9000,
            "signal_port": 9001,
            "public_data_port": 25149,
            "public_signal_port": 25457,
            "splits": "1,2"
        }
    ]
}
```

### Usage

Run the script with your prompt and path to the config:

```bash
python generate_commands.py --prompt "<｜User｜>What is 1+1?<｜Assistant｜>" --config-path config.json [--multi-splits]
```

* `--prompt`: The text generation prompt.
* `--config-path`: Path to your JSON configuration file.
* `--multi-splits`: Include this flag to pass `--splits` to `llama-cli`.

### Output

The script prints:

* A `Master Node Command: ==========` section
* A `Server N Node Command:` section for each server node

You can directly copy and paste these lines into your shell on the respective machines.

### Example

```bash
$ python generate_commands.py --prompt "<｜User｜>What is 1+1?<｜Assistant｜>" --config-path config.json --multi-splits
Master Node Command:
------------------------------------------------------------
./llama-cli --splits 0,1,2 -m download/Llama-3.2-1B-Instruct-Q4_K_M-00001-of-00003.gguf -c 4096 -n 1024 -p "<｜User｜>What is 1+1?<｜Assistant｜>" --world 3 --rank 0 --prefetch -lw "4,8,4" -ngl 4 --master 127.0.0.1 --data_port 9000 --signal_port 9001 --next tw-05.access.glows.ai --master_data_port 25443 --next_node_data_port 25142 --next_node_signal_port 25450
------------------------------------------------------------
Server 0 Node Command:
./llama-cli --splits 0,1 -m download/Llama-3.2-1B-Instruct-Q4_K_M-00001-of-00003.gguf --world 3 --rank 1 --prefetch -ngl 8 --master tw-05.access.glows.ai --data_port 9000 --signal_port 9002 --next tw-05.access.glows.ai --master_data_port 25443 --next_node_data_port 25149 --next_node_signal_port 25457
------------------------------------------------------------
Server 1 Node Command:
./llama-cli --splits 1,2 -m download/Llama-3.2-1B-Instruct-Q4_K_M-00001-of-00003.gguf --world 3 --rank 2 --prefetch -ngl 4 --master tw-05.access.glows.ai --data_port 9000 --signal_port 9001 --next tw-05.access.glows.ai --master_data_port 25443 --next_node_data_port 25443 --next_node_signal_port 25751
------------------------------------------------------------
```

---

## delay.sh

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
---

## gguf-split

A command-line utility from the `llama.cpp` project to split `.gguf` model files into smaller shards, either by tensor count or total size. This supports multi-split loading in distributed setups.

### Release Information

* Source repository: [https://github.com/ggml-org/llama.cpp/tree/master/tools/gguf-split](https://github.com/ggml-org/llama.cpp/tree/master/tools/gguf-split)
* Release tag: `b5734`

### Usage

```bash
cd gguf-split-b5734
./llama-gguf-split --split-max-tensors <N> <input.gguf> <output_prefix>
```

For example:

```bash
./llama-gguf-split --split-max-tensors 38 \
    ../gguf_examples/Llama-3.2-1B-Instruct-Q4_K_M.gguf \
    ../gguf_examples/Llama-3.2-1B-Instruct-Q4_K_M
```

* `--split-max-tensors <N>`: Maximum number of tensors per shard.
* `input.gguf`: Path to the original GGUF model file.
* `output_prefix`: Prefix for the generated split files (they will end with `.gguf`).

- gguf metadata extractor 

    after i implement the multiple file 

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.