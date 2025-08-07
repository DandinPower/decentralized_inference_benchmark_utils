# LLM‑Evaluation Suite

This repository contains two evaluation scripts that benchmark Large‑Language‑Models (LLMs) against two public multiple‑choice datasets:

## Script Overview

| Script             | Dataset                         | Purpose                                                                 |
|--------------------|----------------------------------|-------------------------------------------------------------------------|
| `mmlu_pro.py`      | MMLU‑Pro – 12K+ high‑quality academic questions | Full‑scale evaluation with chain‑of‑thought (CoT) examples from the validation set |
| `gpqa_diamond.py`  | GPQA‑Diamond – 198 question‑answer pairs        | Quick sanity‑check evaluation |

Both scripts share the same evaluation pipeline – data loading, prompt construction, asynchronous API calls, answer extraction, and result reporting.

## Common Parts

| Step                | What It Does                                                                 | Why It Matters                                                     |
|---------------------|------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Argument Parsing    | Uses `argparse.ArgumentParser` to accept `<model_name>`, `<base_url>`, `<api_key>`, `<workers>`, `<number_of_questions>`, and `<output_path>` | Provides a consistent CLI for both scripts                         |
| Async OpenAI Client | `AsyncOpenAI(base_url=…, api_key=…)`                                         | Enables non‑blocking, concurrent requests                           |
| Prompt Construction | Builds a prompt with the question, options, and (for MMLU‑Pro) CoT examples | Controls how the model is presented with the task                   |
| API Call            | `client.chat.completions.create(..., temperature=0, max_tokens=…)`           | Sends the prompt and receives a free‑text response                  |
| Answer Extraction   | Regex search for patterns like `answer is (A)` or `Answer: B`                | Normalizes model output into a single letter                        |
| Result Aggregation  | Logs prediction, outputs, prompt, and result; computes accuracy              | Generates a comprehensive JSON report                               |
| Concurrent Workers  | `asyncio.Queue` + `asyncio.Task` per worker                                 | Speeds up evaluation with parallel requests                         |

## Differences Between `mmlu_pro.py` and `gpqa_diamond.py`

| Feature              | `mmlu_pro.py`                                                                                         | `gpqa_diamond.py`                                                                                       |
|----------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Dataset              | `TIGER-Lab/MMLU-Pro`                                                                                   | `Idavidrein/gpqa`                                                                                         |
| Prompt Style         | Includes CoT examples per category, followed by test question. <br> `max_tokens=4096`                  | Short prompt: question + shuffled options. <br> `max_tokens=8192` for verbose reasoning                   |
| Option Shuffling     | Options remain in original dataset order                                                               | Options randomly shuffled because original dataset don't provide order                                           |
| Answer Extraction    | Same as shared logic                                                                                   | Same as shared logic                                                                                      |
| Number of Questions  | Defaults to full test set (~12K+)                                                                    | Defaults to full test set (~198)                                                                        |
| Prompt Prefix        | "The following are multiple choice questions (with answers) about <category>."                         | "The following question is a multiple‑choice question. Please explain your solution…"                    |
| Token Budget         | 4096                                                                                                   | 8192                                                                                                      |

## Usage Examples

### Installation

The required dependencies are listed in the `pyproject.toml` file at the root of this repository. Install them using `uv`:

```bash
# From the root of the 'decentralized_inference_benchmark_utils' repository
uv sync
```

### 1. MMLU‑Pro Evaluation

```bash
python mmlu_pro.py \
    --model_name openai/gpt-4o-mini \
    --base_url https://api.openai.com/v1 \
    --api_key $OPENAI_API_KEY \
    --output_path mmlu_results.json \
    --workers 16 \
    --number_of_questions 200
````

Evaluates 200 random MMLU‑Pro questions with 16 concurrent workers. If `--number_of_questions` is omitted, all \~12K+ questions are evaluated.

### Using Hugging Face Inference Endpoint

```bash
python mmlu_pro.py \
    --model_name huggingface/gemma-2-9b-it \
    --base_url https://router.huggingface.co/v1 \
    --api_key $HF_TOKEN \
    -w 4 \
    -n 100
```

### 2. GPQA‑Diamond Evaluation

```bash
python gpqa_diamond.py \
    --model_name openai/gpt-4o-mini \
    --base_url https://api.openai.com/v1 \
    --api_key $OPENAI_API_KEY \
    --output_path gpqa_results.json \
    --workers 8 \
    --number_of_questions 500
```

If `--number_of_questions` is omitted, the script evaluates all \~198 GPQA‑Diamond questions.

---

## Output JSON Format

Both scripts produce the same JSON structure:

```json
{
  "number_of_questions": 200,
  "number_of_correct": 167,
  "number_of_wrong": 33,
  "score": 83.5,
  "questions": [
    {
      "question": "What is the capital of France?",
      "options": ["London", "Paris", "Berlin"],
      "answer": "B",
      "pred": "B",
      "model_outputs": "Let me think step by step… The capital of France is Paris. The answer is (B).",
      "prompt": "The following are multiple choice questions (with answers) about geography. ...",
      "answer_result": "correct"
    }
  ]
}
```

* `number_of_correct / number_of_questions` gives the **accuracy percentage**.
* `questions` contains detailed logs per question, useful for debugging model behavior.