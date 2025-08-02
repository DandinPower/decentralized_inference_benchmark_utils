# MMLU-Pro Evaluation Script

This script evaluates the performance of Large Language Models (LLMs) on the [MMLU-Pro benchmark](https://github.com/TIGER-AI-Lab/MMLU-Pro). It is designed to work with any OpenAI-compatible API endpoint and leverages `asyncio` to run evaluations concurrently, significantly speeding up the process.

### Attribution

This evaluation script is based on the methodology and dataset from the official [MMLU-Pro repository](https://github.com/TIGER-AI-Lab/MMLU-Pro) by TIGER AI Lab.

## Installation

The required dependencies are listed in the `pyproject.toml` file at the root of this repository. Install them using `uv`:

```bash
# From the root of the 'decentralized_inference_benchmark_utils' repository
uv sync
```

## Usage

Run the script from the command line, providing the model name and API credentials.

```bash
python mmlu_pro.py \
    --model-name <MODEL_NAME> \
    --base-url <API_BASE_URL> \
    --api-key <YOUR_API_KEY> \
    --output-path results.json \
    --workers 16 \
    --number-of-questions 100
```

### Command-Line Arguments

| Argument                | Short | Description                                                                   | Required | Default       |
| ----------------------- | :---: | ----------------------------------------------------------------------------- | :------: | ------------- |
| `--model-name`          | `-m`  | The model identifier to be used in the API call.                              |  **Yes** | N/A           |
| `--base-url`            |       | The base URL of the OpenAI-compatible API endpoint.                           |  **Yes** | N/A           |
| `--api-key`             |       | The API key for authentication.                                               |  **Yes** | N/A           |
| `--output-path`         | `-o`  | Path to save the output JSON file with results.                               |    No    | `output.json` |
| `--workers`             | `-w`  | Number of concurrent workers for sending API requests.                        |    No    | `1`           |
| `--number-of-questions` | `-n`  | The number of questions to evaluate from the test set. If omitted, all questions are used. |    No    | All           |

## How It Works

1.  **Loads Data**: Downloads and caches the `TIGER-Lab/MMLU-Pro` dataset from the Hugging Face Hub.
2.  **Builds Prompts**: For each test question, it constructs a few-shot prompt. The examples are dynamically selected from the validation set based on the question's category.
3.  **Concurrent Evaluation**: It uses an `asyncio`-based worker pool to send multiple requests to the specified API endpoint simultaneously.
4.  **Answer Extraction**: A regex-based function extracts the final choice (e.g., `(A)`, `B`) from the model's free-text response.
5.  **Scoring**: The extracted answer is compared against the ground truth to calculate the overall accuracy.
6.  **Saves Results**: A detailed JSON report is generated, including the final score, counts, and a log of each question with its prompt, model output, and correctness.

## Output JSON Format

The script produces a JSON file containing the overall score and a detailed breakdown of each question.

```json
{
  "number_of_questions": 100,
  "number_of_correct": 85,
  "number_of_wrong": 15,
  "score": 85.0,
  "questions": [
    {
      "question": "Which of the following is a primary color?",
      "options": ["Green", "Blue", "Orange"],
      "answer": "B",
      "category": "art",
      "pred": "B",
      "model_outputs": "Let's think step by step... Blue is a primary color. The answer is (B).",
      "prompt": "The following are multiple choice questions (with answers) about art...",
      "answer_result": "correct"
    }
  ]
}
```