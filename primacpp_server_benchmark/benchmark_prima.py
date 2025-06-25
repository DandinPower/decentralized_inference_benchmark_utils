import asyncio, argparse, json, time, csv, re
import httpx
import tiktoken

from pathlib import Path

DEFAULT_TOKENIZER = "o200k_base"

enc = tiktoken.get_encoding(DEFAULT_TOKENIZER)
def count_tokens(text: str) -> int:
    return len(enc.encode(text))

JSON_RE = re.compile(r"^data:\s*(\{.*})\s*$")

# ---------- per-request worker ----------
async def run_single(client: httpx.AsyncClient, idx: int, results: list[dict],
                     url: str, headers: dict, payload: dict):
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

            if first_tok_time is None:
                first_tok_time = now
            last_tok_time = now

    end = time.perf_counter()
    # ----- metrics -----
    ttft = (first_tok_time - start) if first_tok_time else None
    span = (last_tok_time - first_tok_time) if (token_count > 1 and first_tok_time) else 0
    tpot = (span / (token_count - 1)) if token_count > 1 else None
    tks  = (token_count / (end - start)) if token_count else 0

    meta.update(ttft=ttft, tpot=tpot, tks=tks, tokens=token_count,
                wall=end - start)
    results.append(meta)

# ---------- main orchestration ----------
async def benchmark(concurrency_levels: list[int], url: str,
                    headers: dict, payload: dict, csv_output_path: str = None):
    csv_data = []

    async with httpx.AsyncClient(http2=False) as client:
        for conc in concurrency_levels:
            print(f"\n=== {conc} concurrent request(s) ===")
            burst_results: list[dict] = []
            burst_start = time.perf_counter()

            tasks = [
                asyncio.create_task(
                    run_single(client, i, burst_results, url, headers, payload)
                )
                for i in range(conc)
            ]
            await asyncio.gather(*tasks)
            burst_end = time.perf_counter()

            # aggregate
            sys_tkn = sum(r["tokens"] for r in burst_results)
            sys_tps = sys_tkn / (burst_end - burst_start) if sys_tkn else 0

            # calculate user-level averages (only for successful requests)
            valid_results = [r for r in burst_results if r["ttft"] is not None]
            if valid_results:
                avg_ttft = sum(r["ttft"] for r in valid_results) / len(valid_results)
                avg_tpot = sum(r["tpot"] for r in valid_results if r["tpot"] is not None) / len([r for r in valid_results if r["tpot"] is not None]) if any(r["tpot"] is not None for r in valid_results) else 0
                avg_req_tks = sum(r["tks"] for r in valid_results) / len(valid_results)
                avg_tokens = sum(r["tokens"] for r in valid_results) / len(valid_results)
            else:
                avg_ttft = avg_tpot = avg_req_tks = avg_tokens = 0

            # pretty print
            print("idx  ttft(s)  tpot(s)  req_tks  tokens")
            for r in sorted(burst_results, key=lambda x: x["id"]):
                print(f"{r['id']:>3}  {r['ttft'] or '-':>7.3f}  "
                      f"{r['tpot'] or '-':>7.3f}  {r['tks'] or 0:>7.1f}  "
                      f"{r['tokens']:>6}")

            print(f"User averages: ttft={avg_ttft:.3f}s, tpot={avg_tpot:.3f}s, req_tks={avg_req_tks:.1f}, tokens={avg_tokens:.1f}")
            print(f"System throughput: {sys_tps:.1f} tk/s")
            
            # Store data for CSV output
            csv_data.append({
                "type": "user_avg",
                "concurrency": conc,
                "ttft_s": avg_ttft,
                "tpot_s": avg_tpot,
                "throughput_tk_s": avg_req_tks,
                "generated_tokens": avg_tokens,
                "total_duration_s": None
            })
            csv_data.append({
                "type": "system_total",
                "concurrency": conc,
                "ttft_s": None,
                "tpot_s": None,
                "throughput_tk_s": sys_tps,
                "generated_tokens": sys_tkn,
                "total_duration_s": burst_end - burst_start
            })

    # CSV export (optional)
    if csv_output_path:
        csv_path = Path(csv_output_path)
        with csv_path.open("w", newline="") as f:
            writer = csv.writer(f)
            
            # Write header
            writer.writerow(["concurrency", "ttft (s)", "tpot (s)", "throughput (tk/s)", "generated tokens", "total duration (s)"])
            
            # Group by concurrency level
            for conc in concurrency_levels:
                # Write user average row
                user_data = next(d for d in csv_data if d["type"] == "user_avg" and d["concurrency"] == conc)
                writer.writerow([
                    f"{conc} (user avg)", 
                    f"{user_data['ttft_s']:.3f}" if user_data['ttft_s'] else "",
                    f"{user_data['tpot_s']:.3f}" if user_data['tpot_s'] else "",
                    f"{user_data['throughput_tk_s']:.1f}" if user_data['throughput_tk_s'] else "",
                    f"{user_data['generated_tokens']:.1f}" if user_data['generated_tokens'] else "",
                    f"{user_data['total_duration_s']:.3f}" if user_data['total_duration_s'] else ""
                ])
                
                # Write system total row
                sys_data = next(d for d in csv_data if d["type"] == "system_total" and d["concurrency"] == conc)
                writer.writerow([
                    f"{conc} (system total)",
                    f"{sys_data['ttft_s']:.3f}" if sys_data['ttft_s'] else "",
                    f"{sys_data['tpot_s']:.3f}" if sys_data['tpot_s'] else "",
                    f"{sys_data['throughput_tk_s']:.1f}" if sys_data['throughput_tk_s'] else "",
                    f"{sys_data['generated_tokens']:.0f}" if sys_data['generated_tokens'] else "",
                    f"{sys_data['total_duration_s']:.3f}" if sys_data['total_duration_s'] else ""
                ])
                
                # Add empty row for separation
                writer.writerow([])
                
        print(f"\nDetailed results written to {csv_path.resolve()}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Benchmark prima.cpp LLM service at varying concurrencies"
    )
    p.add_argument(
        "-c", "--concurrency-levels",
        nargs="+", type=int,
        default=[1, 2, 4, 8, 16],
        help="List of concurrency levels to test, e.g. -c 1 2 4 8 16"
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
        "--prompt", type=str,
        default="Explain what is edge AI in detail?",
        help="User prompt content (default: edge AI explanation)"
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

    # Build URL, headers, and payload from args
    full_url = f"http://{args.host}:{args.port}{args.endpoint}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": args.model,
        "messages": [{"role": "user", "content": args.prompt}],
        "max_tokens": args.max_tokens,
        "temperature": 0.7,
        "stream": True,
    }

    asyncio.run(benchmark(
        args.concurrency_levels,
        full_url,
        headers,
        payload,
        args.csv_output
    ))
