# prima.cpp_benchmark_utils

A collection of tools for benchmarking multi-node prima.cpp ([DandinPower's fork](https://github.com/DandinPower/prima.cpp)), including:

1. prima.cpp commands generator
2. delay.sh
3. gguf-split
4. gguf metadata converter


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

Run the script with your prompt file and path to the config:

```bash
python generate_commands.py --prompt-path prompt.txt --config-path config.json [--multi-splits]
```

* `--prompt-path`: Path to a `.txt` file containing the text generation prompt.
* `--config-path`: Path to your JSON configuration file.
* `--multi-splits`: Include this flag to pass `--splits` to `llama-cli`.

#### Prompt File Format

Create a `.txt` file containing your prompt. The script will read all lines and join them into a single line for the command generation. For example:

**prompt.txt:**
```
<｜User｜>
What is 1+1?
Please explain step by step.
<｜Assistant｜>
```

This will be converted to: `<｜User｜> What is 1+1? Please explain step by step. <｜Assistant｜>`

### Output

The script prints:

* A `Master Node Command: ==========` section
* A `Server N Node Command:` section for each server node

You can directly copy and paste these lines into your shell on the respective machines.

### Example

```bash
$ python generate_commands.py --prompt-path prompt.txt --config-path config.json --multi-splits
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

## gguf metadata converter

After implementing the flexible GGUF splits loader in [prima.cpp#3](https://github.com/DandinPower/prima.cpp/pull/3), many ranks only require the metadata from the first split to initialize, without loading the full weight tensors. Downloading and storing the entire GGUF blob can be prohibitively large on devices with limited storage.

This converter strips out all tensor data from the first-split file (e.g. `prefix-00001-of-0000X.gguf`), leaving a valid, metadata-only stub. You can then pass this stub to `prima -m` for ranks that don’t require split index 0, reclaiming the storage space previously occupied by the weights.

### How It Works

1. **Memory-map** the input GGUF file in read-only mode (no weight pages are faulted in).
2. **Scan** the header, KV section, and tensor descriptors to find where metadata ends.
3. **Align** the metadata end offset to `general.alignment` (default 32 bytes).
4. **Truncate & overwrite** the original file, writing only the metadata stub.

### Usage

```
# Replace the GGUF file in-place with its metadata-only stub:
./gguf_meta_stub.py path/to/prefix-00001-of-0000X.gguf
```

The script will print the size of the retained metadata and overwrite the original file.

## prima.cpp Server Mode Benchmark Utility

This benchmark tool measures latency and throughput of a prima.cpp-based LLM service under varying concurrency levels.

### Features

* Configurable server `host`, `port`, and HTTP `endpoint`
* Customizable `model`, `prompt`, and `max_tokens`
* Variable concurrency levels via CLI (`-c/--concurrency-levels`)
* Measures per-request TTFT (time-to-first-token), TPOT (time-per-output-token), and tokens/sec
* Computes aggregate system throughput (tokens/sec) per burst
* Outputs results to console and saves a CSV (`benchmark_results.csv`)

### Installation

```bash
pip install httpx[http2] tiktoken
```

### Usage

```bash
python benchmark_prima.py \
  -c 1 2 4 8 16 \
  --host 127.0.0.1 \
  --port 8080 \
  --endpoint /v1/chat/completions \
  --model "Deepseek-R1-Distill-Llama-8B" \
  --prompt "Explain what is edge AI in detail?" \
  --max-tokens 1000
```

#### Arguments

| Option                     | Description                                                 |
| -------------------------- | ----------------------------------------------------------- |
| `-c, --concurrency-levels` | List of concurrency levels (e.g. `1 2 4 8 16`)              |
| `--host`                   | Server host (default: `127.0.0.1`)                          |
| `--port`                   | Server port (default: `8080`)                               |
| `--endpoint`               | API endpoint path (default: `/v1/chat/completions`)         |
| `--model`                  | Model name (default: `Deepseek-R1-Distill-Llama-8B`)        |
| `--prompt`                 | Prompt text (default: `Explain what is edge AI in detail?`) |
| `--max-tokens`             | Max tokens per request (default: `1000`)                    |

### Output

* **Console**: Per-request metrics and system throughput for each concurrency level
* **CSV**: `benchmark_results.csv` with detailed columns:

  * `concurrency`, `id`, `ttft`, `tpot`, `tks`, `tokens`, `wall`

### Example Output

```
=== 4 concurrent request(s) ===
idx  ttft(s)  tpot(s)  req_tks  tokens
  0    0.150    0.010     95.3    950
  1    0.152    0.011     94.8    944
  2    0.148    0.010     96.1    961
  3    0.155    0.011     93.2    932
System throughput: 374.5 tk/s

Detailed results written to /path/to/benchmark_results.csv
```

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.