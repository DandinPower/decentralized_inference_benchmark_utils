#!/bin/bash

CONCURRENCY="8"
HOST="tw-05.access.glows.ai"
PORT="26884"
ENDPOINT="/v1/chat/completions"
MODEL="qwen2.5-7b-instruct"
PROMPT_FILE="short_prompt.txt"
MAX_TOKENS="30"
CSV_OUTPUT="7b_gpus3_conc8_short.csv"

# python benchmark.py \
#   -c $CONCURRENCY \
#   --host $HOST \
#   --port $PORT \
#   --endpoint $ENDPOINT \
#   --model $MODEL \
#   --prompt $PROMPT_FILE \
#   --max-tokens $MAX_TOKENS \
#   --csv-output $CSV_OUTPUT

# echo "Benchmark finished. Results saved to $CSV_OUTPUT"

PROMPT_FILE="long_prompt.txt"
MAX_TOKENS="100"
CSV_OUTPUT="7b_gpus3_conc8_long.csv"

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