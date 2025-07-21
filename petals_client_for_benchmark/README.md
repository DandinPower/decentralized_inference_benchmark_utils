# Petals Benchmark Client

This directory contains a Python-based client designed to benchmark large language model inference performance on a [Petals](https://github.com/bigscience-workshop/petals) swarm. It measures key metrics such as **Time to First Token (TTFT)** and **throughput**, providing a clear picture of the decentralized network's efficiency.

## Installation

This client requires a specific fork of the Petals library. To install it, run the following command:

```bash
pip install git+https://github.com/DandinPower/petals
```

## Usage

You can start the benchmark by running the `main.py` script. You'll need to specify the model, a prompt file, at least one initial peer from the swarm, and the desired generation length.

### Command

```bash
python main.py \
    --model-name <MODEL_ON_HUB> \
    --prompt-path <PATH_TO_PROMPT_FILE> \
    --initial-peers <PEER_MULTIADDRESS> \
    --generation-length <NUMBER_OF_TOKENS>
```

### Example

Here's an example of how to run the client, connecting to a local peer:

```bash
python main.py \
    -m mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated \
    -p prompts/llama8B_short.txt \
    -i /ip4/127.0.0.1/tcp/9000/p2p/12D3KooWGffvVbLCWYJBQV5QVNEAcG6T5szndcSS9otqZHzhknHR \
    -g 1024
```

## Command-Line Arguments

The script accepts the following arguments:

| Argument | Short | Description | Required |
| :--- | :---: | :--- | :---: |
| `--model-name` | `-m` | The name of the model on the Hugging Face Hub (e.g., `petals-infra/Llama-3-8B-Instruct-v2`). | **Yes** |
| `--prompt-path` | `-p` | The path to a `.txt` file containing the input prompt. | **Yes** |
| `--initial-peers` | `-i` | One or more multiaddresses of the initial peers in the Petals swarm. | **Yes** |
| `--generation-length`| `-g` | The maximum number of new tokens to generate. | **Yes** |

## Output Metrics

After the generation is complete, the script prints a summary of the performance metrics:

  * **Prompt Tokens**: The total number of tokens in the input prompt.
  * **Time to First Token (TTFT)**: The time in seconds from starting the request until the first new token is received. This metric is crucial for evaluating the latency of the system.
  * **Time Per Output Token (TPOT)**: The average time in seconds required to generate each token *after* the first one. This measures the steady-state generation speed.
  * **Throughput (Token/s)**: The rate of token generation during the decoding phase, calculated as `1 / TPOT`. A higher throughput indicates better performance.

### Sample Output

```
--- Measurement ---
Prompt Tokens: 887
Time to First Token (TTFT): 1.2345 seconds
Time Per Output Token (TPOT): 0.0567 seconds
Throughput (Token/s): 17.6367
```