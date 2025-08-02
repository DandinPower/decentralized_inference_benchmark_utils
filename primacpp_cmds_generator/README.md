# prima.cpp Commands Generator

This utility automates the construction of both `llama-cli`, `llama-server` and `llama-perplexity` commands for multi-node inference with prima.cpp. It reads a JSON configuration file describing your cluster topology and outputs ready-to-run shell commands for each node.

### Features

* **Multi Mode Support**: Generates both CLI, server and perplexity mode commands
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

#### Perplexity Mode (Evaluation)

Generates `llama-perplexity` commands for perplexity evaluation:

```bash
cd primacpp_cmds_generator
python generate_commands.py -c perplexity_example.json
```

### Configuration Files

#### CLI Mode Configuration

For `llama-cli` text generation, create a config file like `cli_example.json`:

```json
{
    "mode": "cli",
    "gguf_file": "/datadrive/gguf/Qwen2.5/qwen2.5-7b-instruct-q4_k_m-00001-of-00002.gguf",
    "ctx_size": 4096,
    "n_batch": 4096,
    "n_ubatch": 512,
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
    "n_batch": 16394,
    "n_ubatch": 512,
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

#### Perplexity Mode Configuration

For `llama-perplexity` text generation, create a config file like `perplexity_example.json`:

```json
{
    "mode": "perplexity",
    "gguf_file": "gguf/qwen2.5-7b-instruct-q4_k_m-00001-of-00002.gguf",
    "text_file": "wikitext-2-raw/wiki.test.raw",
    "master_node": {
        "layer_window_size": 14,
        "loopback_ip": "127.0.0.1",
        "public_ip": "192.168.4.9",
        "data_port": 9000,
        "signal_port": 9001,
        "public_data_port": 9000,
        "public_signal_port": 9001,
        "additional_flags": "-fa"
    },
    "server_nodes": [
        {
            "layer_window_size": 14,
            "public_ip": "192.168.4.10",
            "data_port": 9000,
            "signal_port": 9001,
            "public_data_port": 9000,
            "public_signal_port": 9001,
            "additional_flags": "-fa"
        }
    ]
}
```

### Configuration Fields

#### Common Fields
- `mode`: Operation mode ("cli", "server" and "perplexity")
- `gguf_file`: Path to your GGUF model file

#### For CLI and Server

- `ctx_size`: Context size for the model
- `n_batch`: The total batch size the model processes at once.
- `n_ubatch`: The micro-batch size, which may be used for pipelined execution.

#### CLI Mode Specific
- `n_predict`: Number of tokens to generate
- Requires `-p/--prompt-path` argument

#### Server Mode Specific  
- `server_host`: Host to bind the HTTP server (e.g., "0.0.0.0", "127.0.0.1")
- `server_port`: Port for the HTTP API (e.g., 8080)
- `number_process`: Number of processes for the server

#### Perplexity Mode Specific
- `text_file`: Path to your evaluated text file

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