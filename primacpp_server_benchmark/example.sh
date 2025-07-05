#!/bin/bash

CONCURRENCY="4"
HOST="tw-06.access.glows.ai"
PORT="25503"
ENDPOINT="/v1/chat/completions"
MODEL="qwen2.5-72b-instruct"
PROMPT_FILE="short_prompt.txt"
MAX_TOKENS="100"
CSV_OUTPUT="profiling.csv"

python benchmark.py \
  -c $CONCURRENCY \
  --host $HOST \
  --port $PORT \
  --endpoint $ENDPOINT \
  --model $MODEL \
  --prompt $PROMPT_FILE \
  --max-tokens $MAX_TOKENS \
  --csv-output $CSV_OUTPUT

echo "Benchmark finished. Results saved to $CSV_OUTPUT"

PROMPT_FILE="long_prompt.txt"
MAX_TOKENS="100"
CSV_OUTPUT="qwen2.5-72b_gpus2_long.csv"

python benchmark.py \
  -c $CONCURRENCY \
  --host $HOST \
  --port $PORT \
  --endpoint $ENDPOINT \
  --model $MODEL \
  --prompt $PROMPT_FILE \
  --max-tokens $MAX_TOKENS \
  --csv-output $CSV_OUTPUT

echo "Benchmark finished. Results saved to $CSV_OUTPUT"