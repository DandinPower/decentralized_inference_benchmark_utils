# prima.cpp_benchmark_utils

A comprehensive collection of tools for benchmarking and configuring multi-node prima.cpp ([DandinPower's fork](https://github.com/DandinPower/prima.cpp)) deployments, including:

1. **prima.cpp Commands Generator** - Automated command generation for CLI and server modes
2. **Server Benchmark Tool** - Performance testing for prima.cpp servers
3. **GGUF Utilities** - Model file splitting and metadata conversion
4. **Network Simulation** - Latency simulation for distributed testing

## prima.cpp Commands Generator

This utility automates the construction of both `llama-cli` and `llama-server` commands for multi-node inference with prima.cpp. It reads a JSON configuration file describing your cluster topology and outputs ready-to-run shell commands for each node.

### Features

* **Dual Mode Support**: Generates both CLI and server mode commands
* **Multi-Node Orchestration**: Supports master node + any number of server nodes
* **GGUF Optimization**: Single-split and multi-split model support
* **Configuration Validation**: Catches common setup errors early
* **Production Ready**: Outputs complete commands with all required flags

### Prerequisites

* [prima.cpp](https://github.com/DandinPower/prima.cpp) - DandinPower's fork with public port configuration and multi-split optimization

### Usage Modes

#### CLI Mode (One-time Text Generation)

Generates `llama-cli` commands for direct text generation:

```bash
cd primacpp_cmds_generator
python generate_commands.py -c cli_example.json -p prompt.txt
```

#### Server Mode (API Service)

Generates `llama-server` commands for HTTP API service:

```bash
cd primacpp_cmds_generator
python generate_commands.py -c server_example.json
```

### Configuration Files

#### CLI Mode Configuration

For `llama-cli` text generation, create a config file like `cli_example.json`:

```json
{
    "mode": "cli",
    "gguf_file": "/datadrive/gguf/Qwen2.5/qwen2.5-7b-instruct-q4_k_m-00001-of-00002.gguf",
    "ctx_size": 4096,
    "n_predict": 1024,
    "master_node": {
        "layer_window_size": 7,
        "loopback_ip": "127.0.0.1",
        "public_ip": "tw-05.access.glows.ai",
        "data_port": 9000,
        "signal_port": 9001,
        "public_data_port": 26554,
        "public_signal_port": 26862,
        "additional_flags": "-fa"
    },
    "server_nodes": [
        {
            "layer_window_size": 7,
            "public_ip": "tw-05.access.glows.ai",
            "data_port": 9000,
            "signal_port": 9001,
            "public_data_port": 25329,
            "public_signal_port": 25021,
            "additional_flags": "-fa"
        },
        {
            "layer_window_size": 7,
            "public_ip": "tw-05.access.glows.ai", 
            "data_port": 9000,
            "signal_port": 9001,
            "public_data_port": 25945,
            "public_signal_port": 23985,
            "additional_flags": "-fa"
        },
        {
            "layer_window_size": 7,
            "public_ip": "tw-07.access.glows.ai",
            "data_port": 9000,
            "signal_port": 9001,
            "public_data_port": 24369,
            "public_signal_port": 27389,
            "additional_flags": "-fa"
        }
    ]
}
```

#### Server Mode Configuration

For `llama-server` HTTP API service, add server-specific fields:

```json
{
    "mode": "server",
    "gguf_file": "/datadrive/gguf/Qwen2.5/qwen2.5-7b-instruct-q4_k_m-00001-of-00002.gguf",
    "ctx_size": 16384,
    "master_node": {
        "layer_window_size": 7,
        "loopback_ip": "127.0.0.1",
        "public_ip": "tw-05.access.glows.ai",
        "data_port": 9000,
        "signal_port": 9001,
        "public_data_port": 26554,
        "public_signal_port": 26862,
        "server_host": "0.0.0.0",
        "server_port": 8080,
        "number_process": 4,
        "additional_flags": "--alias qwen2.5-7b-instruct -fa -cb"
    },
    "server_nodes": [
        {
            "layer_window_size": 7,
            "public_ip": "tw-05.access.glows.ai",
            "data_port": 9000,
            "signal_port": 9001,
            "public_data_port": 25329,
            "public_signal_port": 25021,
            "additional_flags": "-fa"
        }
        // ... additional server nodes
    ]
}
```

### Configuration Fields

#### Common Fields
- `mode`: Operation mode ("cli" or "server")
- `gguf_file`: Path to your GGUF model file
- `ctx_size`: Context size for the model

#### CLI Mode Specific
- `n_predict`: Number of tokens to generate
- Requires `-p/--prompt-path` argument

#### Server Mode Specific  
- `server_host`: Host to bind the HTTP server (e.g., "0.0.0.0", "127.0.0.1")
- `server_port`: Port for the HTTP API (e.g., 8080)
- `number_process`: Number of processes for the server

#### Node Configuration
Each node requires:
- `layer_window_size`: Number of layers this node handles
- `public_ip`: External IP address for inter-node communication
- `data_port`/`signal_port`: Internal communication ports
- `public_data_port`/`public_signal_port`: External ports for NAT/firewall traversal
- `additional_flags`: (Optional) Additional command-line flags to pass to llama-cli/llama-server
- `splits`: (Optional) Comma-separated split indices for multi-split models

### Command Line Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `-c, --config-path` | Yes | Path to JSON configuration file |
| `-p, --prompt-path` | CLI mode only | Path to `.txt` file containing the prompt |

### Prompt File Format (CLI Mode Only)

For CLI mode, create a `.txt` file containing your prompt. Multi-line prompts are automatically joined:

**prompt.txt:**
```
<｜User｜>
What is 1+1?
Please explain step by step.
<｜Assistant｜>
```

Converted to: `<｜User｜> What is 1+1? Please explain step by step. <｜Assistant｜>`

### Output Format

The generator outputs ready-to-run commands:

```
Master Node Command:
------------------------------------------------------------
[Complete command for master node]
------------------------------------------------------------
Server 0 Node Command:
[Complete command for server node 0]
------------------------------------------------------------
Server 1 Node Command:
[Complete command for server node 1]
------------------------------------------------------------
```

Copy and paste these commands directly into your shell on the respective machines.

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
* Calculates user-level averages across all concurrent requests
* Computes aggregate system throughput (tokens/sec) per burst
* Outputs results to console and saves a structured CSV with user averages and system totals

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
  --max-tokens 1000 \
  --csv-output benchmark_results.csv
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
| `--csv-output`             | Path to save CSV results (optional, skips CSV if not provided) |

### Output

* **Console**: Per-request metrics, user averages, and system throughput for each concurrency level
* **CSV**: Optional structured results file (only created if `--csv-output` is specified) with format:

  | concurrency | ttft (s) | tpot (s) | throughput (tk/s) | generated tokens | total duration (s) |
  |-------------|----------|----------|-------------------|------------------|--------------------|
  | 1 (user avg) | 0.150 | 0.010 | 95.3 | 950.0 | |
  | 1 (system total) | | | 374.5 | 3787 | 10.120 |
  | 4 (user avg) | 0.151 | 0.011 | 94.7 | 946.8 | |
  | 4 (system total) | | | 1498.2 | 3787 | 2.528 | |

### Example Output

```
=== 4 concurrent request(s) ===
idx  ttft(s)  tpot(s)  req_tks  tokens
  0    0.150    0.010     95.3    950
  1    0.152    0.011     94.8    944
  2    0.148    0.010     96.1    961
  3    0.155    0.011     93.2    932
User averages: ttft=0.151s, tpot=0.011s, req_tks=94.9, tokens=946.8
System throughput: 374.5 tk/s

Detailed results written to /path/to/benchmark_results.csv  # Only if --csv-output is specified
```

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.