# prima.cpp Server Benchmark

This benchmark tool measures latency and throughput of a prima.cpp-based LLM service under varying concurrency levels.

### Features

* Configurable server `host`, `port`, and HTTP `endpoint`
* Prompt loading from `.txt` files with validation and token counting
* Variable concurrency levels via CLI (`-c/--concurrency-levels`)
* Real-time progress tracking during benchmark execution
* Measures per-request TTFT (time-to-first-token), TPOT (time-per-output-token), and tokens/sec
* Calculates user-level averages across all concurrent requests
* Computes aggregate system throughput (tokens/sec) per burst
* Structured CSV output with separate user average and system total metrics
* Uses tiktoken for accurate token counting with configurable encoding

### Installation

```bash
pip install httpx[http2] tiktoken
```

### Usage

```bash
python benchmark.py \
  -p prompt.txt \
  -c 1 2 4 8 16 \
  --host 127.0.0.1 \
  --port 8080 \
  --endpoint /v1/chat/completions \
  --model "Deepseek-R1-Distill-Llama-8B" \
  --max-tokens 1000 \
  --csv-output benchmark_results.csv
```

#### Arguments

| Option                     | Required | Description                                                 |
| -------------------------- | -------- | ----------------------------------------------------------- |
| `-p, --prompt-path`        | Yes      | Path to `.txt` file containing the prompt                   |
| `-c, --concurrency-levels` | No       | List of concurrency levels (default: `1 2 4 8 16`)          |
| `--http-mode`              | No       | Http request mode (default: https)                          |
| `--host`                   | No       | Server host (default: `127.0.0.1`)                          |
| `--port`                   | No       | Server port (default: `8080`)                               |
| `--endpoint`               | No       | API endpoint path (default: `/v1/chat/completions`)         |
| `--model`                  | No       | Model name (default: `Deepseek-R1-Distill-Llama-8B`)        |
| `--max-tokens`             | No       | Max tokens per request (default: `1000`)                    |
| `--csv-output`             | No       | Path to save CSV results (optional, skips CSV if not provided) |

### Prompt File Format

Create a `.txt` file containing your prompt. Multi-line prompts are automatically joined:

**prompt.txt:**
```
What is edge AI?
Please explain the key benefits and use cases.
Provide specific examples.
```

Converted to: `What is edge AI? Please explain the key benefits and use cases. Provide specific examples.`

### Output

* **Console**: Real-time progress tracking, per-request metrics, user averages, and system throughput for each concurrency level
* **CSV**: Optional structured results file with comprehensive metrics including:

| Type | Prompt Tokens | Generated Tokens | Concurrency | TTFT (s) | TPOT (s) | Throughput (tk/s) | Total duration (s) |
|------|---------------|------------------|-------------|----------|----------|-------------------|--------------------|
| User Average | 15 | 946.8 | 4 | 0.151 | 0.011 | 94.7 | N/A |
| System Total | 15 | 3787 | 4 | N/A | N/A | 1498.2 | 2.528 |

### Example Output

```
=== 4 concurrent request(s) ===
Req 0:  234 tk | Req 1:  189 tk | Req 2:  156 tk | Req 3:  203 tk

idx  ttft(s)  tpot(s)  req_tks  tokens
  0    0.150    0.010     95.3    950
  1    0.152    0.011     94.8    944
  2    0.148    0.010     96.1    961
  3    0.155    0.011     93.2    932
User averages: ttft=0.151s, tpot=0.011s, req_tks=94.9, tokens=946.8
System throughput: 1498.2 tk/s

Detailed results written to /path/to/save.csv  # Only if --csv-output is specified
```