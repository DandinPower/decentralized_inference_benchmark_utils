import re
import json
import asyncio

from argparse import ArgumentParser, Namespace
from collections import defaultdict
from datetime import datetime
from datasets import load_dataset, Dataset
from openai import AsyncOpenAI
from tqdm import tqdm

MMLU_PRO_DATASET = "TIGER-Lab/MMLU-Pro"
RETRY = 3

def get_client(base_url: str, api_key: str):
    client = AsyncOpenAI(
        base_url=base_url,
        api_key=api_key,
    )
    return client


async def call_api(client, model_name: str, prompt: str, max_tokens: int):
    message_text = [{"role": "user", "content": prompt}]
    completion = await client.chat.completions.create(
        model=model_name,
        messages=message_text,
        temperature=0,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    result = completion.choices[0].message.content
    return result


def load_mmlu_pro(dataset_path: str):
    def extract_questions(hf_dataset: Dataset):
        questions = []
        for each in hf_dataset:
            options = []
            for opt in each["options"]:
                if opt == "N/A":
                    continue
                options.append(opt)
            each["options"] = options
            questions.append(each)
        return questions

    def categorization(questions: list) -> dict[str, list]:
        categorized_questions = defaultdict(list)
        for question in questions:
            categorized_questions[question["category"]].append(question)
        return categorized_questions

    dataset = load_dataset(dataset_path)
    test_dataset, val_dataset = dataset["test"], dataset["validation"]
    test_questions = extract_questions(test_dataset)
    val_questions = extract_questions(val_dataset)
    val_categorized_questions = categorization(val_questions)
    return test_questions, val_categorized_questions


def extract_answer(text):
    match = re.search(r"answer is \(?([A-J])\)?", text)
    if match:
        return match.group(1)
    match = re.search(r".*[aA]nswer:\s*([A-J])", text)
    if match:
        return match.group(1)
    match = re.search(r"\b[A-J]\b(?!.*\b[A-J]\b)", text, re.DOTALL)
    if match:
        return match.group(0)
    return None


def format_val_example(question: str, options: list[str], cot_content: str) -> str:
    if cot_content.startswith("A: "):
        cot_content = cot_content[3:]
    example = f"Question: {question}\nOptions: "
    choice_map = "ABCDEFGHIJ"
    for i, opt in enumerate(options):
        example += f"{choice_map[i]}. {opt}\n"
    example += "Answer: " + cot_content + "\n\n"
    return example


def format_test_examplpe(question: str, options: list[str]) -> str:
    example = f"Question: {question}\nOptions: \n"
    choice_map = "ABCDEFGHIJ"
    for i, opt in enumerate(options):
        example += f"{choice_map[i]}. {opt}\n"
    return example


async def single_request(client, model_name, single_question, cot_examples_dict, max_tokens):
    category = single_question["category"]
    cot_examples = cot_examples_dict[category]
    question = single_question["question"]
    options = single_question["options"]
    prompt = f'The following are multiple choice questions (with answers) about {category}. Think step by step and then output the answer in the format of "The answer is (X)" at the end.\n\n'

    for each in cot_examples:
        prompt += format_val_example(each["question"], each["options"], each["cot_content"])
    prompt += format_test_examplpe(question, options)

    retry = 0
    while True:
        try:
            response = await call_api(client, model_name, prompt, max_tokens)
            response = response.replace("**", "")
            break
        except Exception as e:
            if retry >= RETRY:
                return None, None, None
            retry += 1
            print(f"Error: {e}, Retry: {retry}/{RETRY}")

    pred = extract_answer(response)
    return pred, response, prompt


async def evaluate(args: Namespace):
    update_lock = asyncio.Lock()

    async def worker_fn(
        worker_id: int,
        task_queue: asyncio.Queue,
        test_questions: list,
        progress_bar: tqdm,
        model_name: str,
        base_url: str,
        api_key: str,
        max_tokens: int
    ) -> tuple[int, int]:
        corr, wrong = 0, 0
        client = get_client(base_url, api_key)
        while True:
            task_id = await task_queue.get()
            if task_id is None:
                task_queue.task_done()
                break
            print(f"[{datetime.now()}][WORKER:{worker_id}][TASK:{task_id}]")
            label = test_questions[task_id]["answer"]
            pred, response, prompt = await single_request(
                client, model_name, test_questions[task_id], val_categorized_questions, max_tokens
            )
            async with update_lock:
                if response is not None:
                    test_questions[task_id]["pred"] = pred
                    test_questions[task_id]["model_outputs"] = response
                    test_questions[task_id]["prompt"] = prompt
                    if pred is not None and pred == label:
                        corr += 1
                        test_questions[task_id]["answer_result"] = "correct"
                    else:
                        wrong += 1
                        test_questions[task_id]["answer_result"] = "wrong"
                else:
                    test_questions[task_id]["pred"] = "None"
                    test_questions[task_id]["model_outputs"] = "None"
                    test_questions[task_id]["answer_result"] = "wrong"
                progress_bar.update(1)
            task_queue.task_done()
        return corr, wrong

    test_questions, val_categorized_questions = load_mmlu_pro(MMLU_PRO_DATASET)

    n_questions = int(
        len(test_questions) if args.number_of_questions is None else args.number_of_questions
    )
    workers = int(args.workers)
    progress_bar = tqdm(total=n_questions, desc="Evaluating", unit="question")

    task_queue = asyncio.Queue(maxsize=n_questions + workers)
    for i in range(n_questions):
        await task_queue.put(i)
    for _ in range(workers):
        await task_queue.put(None)

    worker_tasks = [
        asyncio.create_task(
            worker_fn(
                worker_id=i,
                task_queue=task_queue,
                test_questions=test_questions,
                progress_bar=progress_bar,
                model_name=args.model_name,
                base_url=args.base_url,
                api_key=args.api_key,
                max_tokens=int(args.max_tokens)
            )
        )
        for i in range(workers)
    ]

    results = await asyncio.gather(*worker_tasks)
    await task_queue.join()
    progress_bar.close()

    corr = sum([c for c, _ in results])
    wrong = sum([w for _, w in results])
    score = (0 if corr == 0 else corr / n_questions) * 100

    output_json = {
        "number_of_questions": n_questions,
        "number_of_correct": corr,
        "number_of_wrong": wrong,
        "score": score,
        "questions": test_questions[:n_questions],
    }

    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(output_json, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--number_of_questions",
        "-n",
        default=None,
        help="MMLU has over 10,000 questions by default. You can specify the number you want to evaluate.",
    )
    parser.add_argument(
        "--output_path",
        "-o",
        default="output.json",
        help="The output JSON file that contains evaluation results and logs.",
    )
    parser.add_argument(
        "--workers",
        "-w",
        default=1,
        help="The number of workers that will call the model API concurrently.",
    )
    parser.add_argument(
        "--model_name", "-m", required=True, help="The model name for the OpenAI-compatible API."
    )
    parser.add_argument(
        "--base_url", required=True, help="The base URL for the OpenAI-compatible API."
    )
    parser.add_argument(
        "--api_key", required=True, help="The API key for the OpenAI-compatible API."
    )
    parser.add_argument(
        "--max_tokens", default=4096, help="The max tokens for the OpenAI-compatible API."
    )
    args = parser.parse_args()
    asyncio.run(evaluate(args))
