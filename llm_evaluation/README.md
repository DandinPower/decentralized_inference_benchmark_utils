# LLM Evaluation Suite

Lightweight scripts to benchmark LLMs on multiple public datasets using a shared async pipeline.

## Scripts at a glance

| Script            | Dataset                                  | Purpose                                              |
| ----------------- | ---------------------------------------- | ---------------------------------------------------- |
| `mmlu_pro.py`     | `TIGER-Lab/MMLU-Pro`                     | Full evaluation with per-category CoT exemplars      |
| `gpqa_diamond.py` | `Idavidrein/gpqa` (split `gpqa_diamond`) | Quick sanity check on 198 expert-level questions     |
| `aime_2025.py`    | `yentinglin/aime_2025`                   | AIME 2025 integer answers, strict integer extraction |

All three follow the same flow: load data, build prompts, call an OpenAI-compatible chat API asynchronously, extract answers, and write a JSON report.

## Common pipeline

| Step              | Details                                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------------ |
| Argument parsing  | `-m/--model_name`, `--base_url`, `--api_key`, `-w/--workers`, `-n/--number_of_questions`, `-o/--output_path` |
| Async client      | `openai.AsyncOpenAI(base_url=..., api_key=...)`                                                              |
| Prompting         | Question plus options. `mmlu_pro.py` prepends CoT exemplars from the validation set by category              |
| API call          | `client.chat.completions.create(..., temperature=0)`                                                         |
| Answer extraction | MMLU/GPQA use final letter A–J. AIME 2025 extracts a clean integer only                                      |
| Concurrency       | Work queue with N workers                                                                                    |
| Reporting         | Per-question logs and accuracy in a single JSON file                                                         |

### Dataset specifics

| Feature                | `mmlu_pro.py`                                         | `gpqa_diamond.py`                                                                    | `aime_2025.py`                      |
| ---------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------ | ----------------------------------- |
| Split used             | `test` for evaluation, `validation` for CoT exemplars | `gpqa_diamond`                                                                       | `default`                             |
| Expected final answer  | One of A…J                                            | One of A…D                                                                           | Integer only                        |
| Default question count | 12K+                 | 198 | 30 |

**Note on GPQA randomness:** because options are shuffled without a seed, runs are not deterministic. If you need exact reproducibility, add a fixed seed in the code before loading questions.

## Installation

Use `uv`.

```bash
# From the root of this repository
uv sync
```

## Usage

### General form

```bash
python {mmlu_pro.py|gpqa_diamond.py|aime_2025.py} \
  --model_name <model_name> \
  --base_url <openai-compatible-base-url> \
  --api_key <api_key> \
  --output_path results.json \
  --workers 16 \
  --number_of_questions 200
```

This evaluates 200 questions with 16 concurrent workers. Omit `--number_of_questions` to run the full set.

### Hugging Face Inference Endpoint router

```bash
python {mmlu_pro.py|gpqa_diamond.py|aime_2025.py} \
  -m <model_name> \
  --base_url https://router.huggingface.co/v1 \
  --api_key $HF_TOKEN \
  -w 4 \
  -n 100
```

### Ollama (local)

```bash
python {mmlu_pro.py|gpqa_diamond.py|aime_2025.py} \
  -m <model_name> \
  --base_url http://localhost:11434/v1 \
  --api_key "" \
  -w 4 \
  -n 30
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
For AIME 2025, `answer` and `pred` are integers. For MMLU/GPQA they are letters.