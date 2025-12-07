import asyncio
import argparse
import json
import time
import csv
import re
import httpx
import tiktoken
import sys
from pathlib import Path

DEFAULT_TOKENIZER = "o200k_base"
enc = tiktoken.get_encoding(DEFAULT_TOKENIZER)


def count_tokens(text: str) -> int:
    return len(enc.encode(text))


def read_prompt_from_file(prompt_path: str) -> str:
    prompt_file = Path(prompt_path)
    if not prompt_file.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
    if not prompt_file.suffix.lower() == ".txt":
        raise ValueError(
            f"Prompt file must have .txt extension: {prompt_path}")

    try:
        with open(prompt_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        prompt = " ".join(line.strip() for line in lines if line.strip())

        if not prompt:
            raise ValueError(
                f"Prompt file is empty or contains only whitespace: {prompt_path}")
        return prompt

    except Exception as e:
        raise RuntimeError(f"Error reading prompt file {prompt_path}: {e}")


async def print_progress(progress_data: dict, tasks: list[asyncio.Task]):
    while any(not task.done() for task in tasks):
        sorted_items = sorted(progress_data.items())
        status_line = " | ".join(
            f"Req {idx}: {count:<4} tk" for idx, count in sorted_items)
        sys.stdout.write(f"\r{status_line}{' ' * 10}")
        sys.stdout.flush()
        await asyncio.sleep(0.1)
    sys.stdout.write(f"\r{' ' * 100}\r")
    sys.stdout.flush()


async def run_single(client: httpx.AsyncClient, idx: int, results: list[dict],
                     url: str, headers: dict, payload: dict, progress_data: dict):
    JSON_RE = re.compile(r"^data:\s*(\{.*})\s*$")
    meta = {"id": idx}
    start = time.perf_counter()

    async with client.stream("POST", url, headers=headers, json=payload, timeout=None) as r:
        if r.status_code != 200:
            meta.update(error=f"HTTP {r.status_code}", ttft=None,
                        tpot=None, tks=None, tokens=0)
            results.append(meta)
            return

        first_tok_time = last_tok_time = None
        token_count = 0

        async for line in r.aiter_lines():
            if not line or line.startswith("data: [DONE]"):
                if line and line.startswith("data: [DONE]"):
                    break
                continue

            m = JSON_RE.match(line)
            if not m:
                continue

            chunk = json.loads(m.group(1))
            if "choices" not in chunk:
                continue

            delta = chunk["choices"][0]["delta"].get("content", "")
            if not delta:
                continue

            now = time.perf_counter()
            token_count += count_tokens(delta)
            progress_data[idx] = token_count

            if first_tok_time is None:
                first_tok_time = now
            last_tok_time = now

    end = time.perf_counter()
    ttft = (first_tok_time - start) if first_tok_time else None
    span = (last_tok_time - first_tok_time) if (token_count >
                                                1 and first_tok_time) else 0
    tpot = (span / (token_count - 1)) if token_count > 1 else None
    tks = (token_count / span) if token_count else 0
    meta.update(ttft=ttft, tpot=tpot, tks=tks, tokens=token_count,
                wall=end - start)
    results.append(meta)


async def benchmark(concurrency_levels: list[int], url: str,
                    headers: dict, payload: dict, prompt_tokens: int, csv_output_path: str = None):
    csv_data = []

    async with httpx.AsyncClient(http2=False) as client:
        for conc in concurrency_levels:
            print(f"\n=== {conc} concurrent request(s) ===")
            burst_results: list[dict] = []
            burst_start = time.perf_counter()

            progress_data = {i: 0 for i in range(conc)}
            worker_tasks = [
                asyncio.create_task(
                    run_single(client, i, burst_results, url,
                               headers, payload, progress_data)
                )
                for i in range(conc)
            ]
            printer_task = asyncio.create_task(
                print_progress(progress_data, worker_tasks))
            await asyncio.gather(*worker_tasks)
            await printer_task
            burst_end = time.perf_counter()

            sys_tkn = sum(r["tokens"] for r in burst_results)
            valid_results = [r for r in burst_results if r["ttft"] is not None]
            if valid_results:
                avg_ttft = sum(r["ttft"]
                               for r in valid_results) / len(valid_results)
                avg_tpot = sum(r["tpot"] for r in valid_results if r["tpot"] is not None) / len(
                    [r for r in valid_results if r["tpot"] is not None]) if any(r["tpot"] is not None for r in valid_results) else 0
                avg_req_tks = sum(r["tks"]
                                  for r in valid_results) / len(valid_results)
                avg_tokens = sum(r["tokens"]
                                 for r in valid_results) / len(valid_results)
                sys_tps = sum(r["tks"] for r in valid_results)
            else:
                avg_ttft = avg_tpot = avg_req_tks = avg_tokens = 0
                sys_tps = 0

            print("idx  ttft(s)  tpot(s)  req_tks  tokens")
            for r in sorted(burst_results, key=lambda x: x["id"]):
                print(f"{r['id']:>3}  {r['ttft'] or '-':>7.3f}  "
                      f"{r['tpot'] or '-':>7.3f}  {r['tks'] or 0:>7.1f}  "
                      f"{r['tokens']:>6}")

            print(
                f"User averages: ttft={avg_ttft:.3f}s, tpot={avg_tpot:.3f}s, req_tks={avg_req_tks:.1f}, tokens={avg_tokens:.1f}")
            print(f"System throughput: {sys_tps:.1f} tk/s")

            csv_data.append({
                "Type": "User Average",
                "Prompt Tokens": prompt_tokens,
                "Generated Tokens": f"{avg_tokens:.1f}",
                "Concurrency": conc,
                "TTFT (s)": f"{avg_ttft:.3f}",
                "TPOT (s)": f"{avg_tpot:.3f}",
                "Throughput (tk/s)": f"{avg_req_tks:.1f}",
                "Total duration (s)": "N/A"
            })
            csv_data.append({
                "Type": "System Total",
                "Prompt Tokens": prompt_tokens,
                "Generated Tokens": sys_tkn,
                "Concurrency": conc,
                "TTFT (s)": "N/A",
                "TPOT (s)": "N/A",
                "Throughput (tk/s)": f"{sys_tps:.1f}",
                "Total duration (s)": f"{burst_end - burst_start:.3f}"
            })

    if csv_output_path:
        csv_path = Path(csv_output_path)
        try:
            with csv_path.open("w", newline="", encoding="utf-8") as f:
                header = [
                    "Type", "Prompt Tokens", "Generated Tokens", "Concurrency",
                    "TTFT (s)", "TPOT (s)", "Throughput (tk/s)", "Total duration (s)"
                ]
                writer = csv.DictWriter(f, fieldnames=header)
                writer.writeheader()
                writer.writerows(csv_data)
            print(f"\nDetailed results written to {csv_path.resolve()}")
        except Exception as e:
            print(f"\nError writing to CSV file: {e}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Benchmark prima.cpp LLM service at varying concurrencies"
    )
    p.add_argument("-p", "--prompt-path", required=True,
                   help="Path to .txt file containing the prompt")
    p.add_argument(
        "-c", "--concurrency-levels",
        nargs="+", type=int,
        default=[1, 2, 4, 8, 16],
        help="List of concurrency levels to test, e.g. -c 1 2 4 8 16"
    )
    p.add_argument(
        "--http-mode", type=str, default="https",
        choices=["http", "https"],
        help="Http request mode (default: https)"
    )
    p.add_argument(
        "--host", type=str, default="127.0.0.1",
        help="Server host (default: 127.0.0.1)"
    )
    p.add_argument(
        "--port", type=int, default=8080,
        help="Server port (default: 8080)"
    )
    p.add_argument(
        "--endpoint", type=str, default="/v1/chat/completions",
        help="API endpoint path (default: /v1/chat/completions)"
    )
    p.add_argument(
        "--model", type=str,
        default="Deepseek-R1-Distill-Llama-8B",
        help="Model name to request (default: Deepseek-R1-Distill-Llama-8B)"
    )
    p.add_argument(
        "--max-tokens", dest="max_tokens", type=int,
        default=1000,
        help="Max tokens per request (default: 1000)"
    )
    p.add_argument(
        "--csv-output", dest="csv_output", type=str,
        help="Path to save CSV results (optional, skips CSV if not provided)"
    )
    args = p.parse_args()

    prompt = read_prompt_from_file(args.prompt_path)
    prompt_tokens = count_tokens(prompt)
    full_url = f"{args.http_mode}://{args.host}:{args.port}{args.endpoint}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": args.model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": args.max_tokens,
        "temperature": 0,
        "stream": True,
    }

    asyncio.run(benchmark(
        args.concurrency_levels,
        full_url,
        headers,
        payload,
        prompt_tokens,
        args.csv_output
    ))
