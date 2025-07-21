import time

from argparse import ArgumentParser, Namespace
from pathlib import Path
from transformers import AutoTokenizer, TextStreamer
from petals import AutoDistributedModelForCausalLM


class TTFTStreamer(TextStreamer):
    def __init__(self, tokenizer: AutoTokenizer, **kwargs):
        super().__init__(tokenizer, **kwargs)
        self.start_time = 0
        self.end_time = 0
        self.ttft = 0.0
        self.first_token_received = False

    def on_finalized_text(self, text: str, stream_end: bool = False):
        # This method is called when a token is fully decoded
        if not self.first_token_received and text:
            # Record TTFT on the first valid token
            end_time = time.monotonic()
            self.ttft = end_time - self.start_time
            self.first_token_received = True

        # Call the original method to print the text to the console
        super().on_finalized_text(text, stream_end=stream_end)


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


def main(args: Namespace):
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    model = AutoDistributedModelForCausalLM.from_pretrained(
        args.model_name, initial_peers=args.initial_peers)
    streamer = TTFTStreamer(tokenizer, skip_prompt=True)
    prompt = read_prompt_from_file(args.prompt_path)
    inputs = tokenizer(prompt, return_tensors="pt")

    generation_kwargs = dict(inputs, streamer=streamer,
                             max_new_tokens=args.generation_length, use_cache=True)
    streamer.start_time = time.monotonic()
    outputs = model.generate(**generation_kwargs)
    streamer.end_time = time.monotonic()

    decoding_time = streamer.end_time - streamer.start_time - streamer.ttft
    prompt_tokens = inputs["input_ids"].shape[-1]
    generated_tokens = outputs.shape[-1] - inputs["input_ids"].shape[-1]
    tpot = decoding_time/generated_tokens
    throughput = 1/tpot
    print(f"\n\n--- Measurement ---")
    print(f"Prompt Tokens: {prompt_tokens}")
    print(f"Time to First Token (TTFT): {streamer.ttft:.4f} seconds")
    print(f"Time Per Output Token (TPOT): {tpot:.4f} seconds")
    print(f"Throughput (Token/s): {throughput:.4f}")


if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("-m", "--model-name", required=True, type=str)
    p.add_argument("-p", "--prompt-path", required=True, type=str,
                   help="Path to .txt file containing the prompt")
    p.add_argument("-i", "--initial-peers", required=True, nargs="+")
    p.add_argument("-g", "--generation-length", required=True, type=int)
    main(p.parse_args())
