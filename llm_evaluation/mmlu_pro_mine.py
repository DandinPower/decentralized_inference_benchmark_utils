import os
import re
import time
from collections import defaultdict

from datasets import load_dataset, Dataset
from openai import OpenAI
from tqdm import tqdm

BASE_URL = "https://router.huggingface.co/v1"
API_KEY = ""
MODEL_NAME = "google/gemma-2-9b-it:groq"
MMLU_PRO_DATASET = "TIGER-Lab/MMLU-Pro"
OUTPUT_DIR = ""

def get_client(base_url: str, api_key: str):
    client = OpenAI(
        base_url=base_url,
        api_key=api_key,
    )
    return client

def call_api(client, model_name: str, prompt: str):
    start = time.time()
    message_text = [{"role": "user", "content": prompt}]
    completion = client.chat.completions.create(
        model=model_name,
        messages=message_text,
        temperature=0,
        max_tokens=4096,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    result = completion.choices[0].message.content
    print("cost time", time.time() - start)
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
    match = re.search(r'.*[aA]nswer:\s*([A-J])', text)
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
    cot_content = "Let's think step by step."
    example = f"Question: {question}\nOptions: \n"
    choice_map = "ABCDEFGHIJ"
    for i, opt in enumerate(options):
        example += f"{choice_map[i]}. {opt}\n"
    example += "Answer: " + cot_content + "\n\n"
    return example

def single_request(client, model_name, single_question, cot_examples_dict):
    category = single_question["category"]
    cot_examples = cot_examples_dict[category]
    question = single_question["question"]
    options = single_question["options"]
    prompt = f"The following are multiple choice questions (with answers) about {category}. Think step by step and then output the answer in the format of \"The answer is (X)\" at the end.\n\n"
    
    for each in cot_examples:
        prompt += format_val_example(each["question"],
                                 each["options"], each["cot_content"])
    prompt += format_test_examplpe(question, options)
    
    try:
        response = call_api(client, model_name, prompt)
        response = response.replace('**', '')
    except Exception as e:
        print("error", e)
        return None, None
    
    pred = extract_answer(response)
    return pred, response, prompt

def evaluate():
    client = get_client(BASE_URL, API_KEY)
    test_questions, val_categorized_questions = load_mmlu_pro(MMLU_PRO_DATASET)

    corr, wrong = 0, 0
    # for each in tqdm(test_questions):
    each = test_questions[0]
    label = each["answer"]
    pred, response, prompt = single_request(client, MODEL_NAME, each, val_categorized_questions)
    if response is not None:
        each["pred"] = pred
        each["model_outputs"] = response
        each["prompt"] = prompt
        if pred is not None:
            if pred == label:
                corr += 1
            else:
                wrong += 1
        else:
            wrong += 1
    
    print(each)
    print(corr, wrong)

if __name__ == "__main__":
    evaluate()