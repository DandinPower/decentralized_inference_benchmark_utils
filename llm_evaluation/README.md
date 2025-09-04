# LLM Evaluation Suite

Lightweight scripts to benchmark LLMs on multiple public datasets using a shared async pipeline.

## Scripts at a glance

| Script            | Dataset                                  | Purpose                                              |
| ----------------- | ---------------------------------------- | ---------------------------------------------------- |
| `mmlu_pro.py`     | `TIGER-Lab/MMLU-Pro`                     | Full evaluation with per-category CoT exemplars      |
| `gpqa_diamond.py` | `Idavidrein/gpqa` (split `gpqa_diamond`) | Quick sanity check on 198 expert-level questions     |
| `aime_2025.py`    | `yentinglin/aime_2025`                   | AIME 2025 integer answers; strict integer extraction |

All three follow the same flow: load data, build prompts, call an OpenAI-compatible chat API asynchronously, extract answers, and write a JSON report.

## Common pipeline

| Step              | Details                                                                                                        |
| ----------------- | -------------------------------------------------------------------------------------------------------------- |
| Argument parsing  | `-m/--model_name`, `--base_url`, `--api_key`, `-w/--workers`, `-n/--number_of_questions`, `-o/--output_path`, `--max_tokens` |
| Async client      | `openai.AsyncOpenAI(base_url=..., api_key=...)`                                                                |
| Prompting         | Question plus options; `mmlu_pro.py` prepends CoT exemplars from the validation set by category                |
| API call          | `client.chat.completions.create(..., temperature=0, max_tokens=...)`                                           |
| Answer extraction | MMLU/GPQA read final letter (A–J); AIME 2025 extracts a clean integer only                                     |
| Concurrency       | Work queue with N workers                                                                                      |
| Reporting         | Per-question logs and accuracy in a single JSON file                                                           |

### Dataset specifics

| Feature               | `mmlu_pro.py`                                         | `gpqa_diamond.py`                                                     | `aime_2025.py`                  |
| --------------------- | ----------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------|
| Split used            | `test` for eval, `validation` for CoT exemplars       | `gpqa_diamond` (uses the `train` split of this config)                | `default` (uses the `train` split) |
| Expected final answer | One of A…J                                            | One of A…D                                                            | Integer only                    |
| Default question count| 10k+                                                  | 198                                                                   | 30                              |

**GPQA determinism:** the position of the correct option is randomized without a fixed seed, so runs are not deterministic. If you need reproducibility, add a fixed seed in the code before loading questions.

## Installation

Using `uv`:

```bash
# From the root of this repository
uv sync
````

## Usage

### General form

```bash
python {mmlu_pro.py|gpqa_diamond.py|aime_2025.py} \
  --model_name <model_name> \
  --base_url <openai-compatible-base-url> \
  --api_key <api_key> \
  --output_path results.json \
  --workers 16 \
  --number_of_questions 200 \
  --max_tokens 4096
```

This evaluates 200 questions with 16 concurrent workers. Omit `--number_of_questions` to run the full split. `--max_tokens` defaults to `4096`.

### Hugging Face Inference Endpoint router

```bash
python {mmlu_pro.py|gpqa_diamond.py|aime_2025.py} \
  -m <model_name> \
  --base_url https://router.huggingface.co/v1 \
  --api_key $HF_TOKEN \
  -w 4 \
  -n 100 \
  --max_tokens 2048
```

### Ollama (local)

```bash
python {mmlu_pro.py|gpqa_diamond.py|aime_2025.py} \
  -m <model_name> \
  --base_url http://localhost:11434/v1 \
  --api_key "" \
  -w 4 \
  -n 30 \
  --max_tokens 1024
```

## Output format

All scripts write a single JSON file:

```json
{
  "number_of_questions": 200,
  "number_of_correct": 167,
  "number_of_wrong": 33,
  "score": 83.5,
  "questions": [
    {
      "question": "…",
      "options": ["…"],
      "answer": "B",
      "pred": "B",
      "model_outputs": "…The answer is (B).",
      "prompt": "…",
      "answer_result": "correct"
    }
  ]
}
```

Notes:

* For AIME 2025, `answer` and `pred` are integer **strings** (e.g., `"42"`). For MMLU/GPQA they are letters.
* `model_outputs` contains the raw model response.
* `score` is the percentage accuracy.

## Tips

* These scripts expect an OpenAI-compatible **Chat Completions** API. If your server uses a different path or schema, set `--base_url` accordingly.
* Throughput depends heavily on your endpoint; tune `--workers` and `--max_tokens` to avoid rate limits or context overflows.