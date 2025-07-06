# Multi‑Rank Log Visualizer

Turn multi-rank logs into an interactive Gantt timeline in your browser.

## Installation

```bash
pip install pandas plotly
```

## Quick start

```bash
python log_visualizer.py --rank-logs ./logs --rank-offsets 0s 0s --out my_run.html
```

### Arguments

| Argument          | Default         | Purpose                                  |
| ------------- | --------------- | ---------------------------------------- |
| `--rank-logs FILES`  | Required | Specifies log files for each rank, or directories containing all rank logs (searched recursively for *.log). The number of log files provided should match the number of ranks, and each file should correspond to a single rank to prevent ordering issues.                        |
| `--rank-offsets OFFSETS`  | Required | Time offsets for each rank. This argument is required, and the number of offsets must equal the number of ranks. Example format: "0s 0s 1ms". If an offset is not needed for a specific rank, use 0s.                            |
| `--out FILE`  | `timeline.html` | Output path                              |

## Log format contract

```
[rank]           Integer, digits only
[timestamp]      ISO 8601 recommended, any string parsable by pandas.to_datetime(..., utc=True)
[operation_type]      Free text, no ] allowed
[start/end]      Literal token "start" or "end"
[operation]      Free text, no ] allowed
[additional description]     Remainder of the line, may contain spaces
```

Examples:

```
[0][2025-07-05T14:07:34.302Z][compute][start][input_embedding][sbatch_tokens: 3216, ubatch_tokens: 512]
[0][2025-07-05T14:07:34.303Z][compute][end][input_embedding][sbatch_tokens: 3216, ubatch_tokens: 512]
[0][2025-07-05T14:07:34.303Z][comm][start][send_tensors][sbatch_tokens: 3216, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-07-05T14:07:34.304Z][comm][end][send_tensors][sbatch_tokens: 3216, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-07-05T14:07:34.304Z][comm][start][recv_tensors][sbatch_tokens: 3216, ubatch_tokens: 512, receive data from other nodes]
[0][2025-07-05T14:07:34.690Z][comm][end][recv_tensors][sbatch_tokens: 3216, ubatch_tokens: 512, receive data from other nodes]
```

## Troubleshooting

| Symptom                                        | Likely cause                                        |
| ---------------------------------------------- | --------------------------------------------------- |
| `ValueError: malformed line or missing [RANK]` | Log producer dropped a bracket or rank field        |
| `Double START without END`                     | Same rank and operation started twice before ending |
| `END without START`                            | Mismatched ordering or missing START                |