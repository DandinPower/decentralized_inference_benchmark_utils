import re
from datetime import datetime

log_data = """
[0][2025-12-07T15:42:12.948Z][compute][start][input_embedding][sbatch_tokens: 1038, ubatch_tokens: 512]
[0][2025-12-07T15:42:13.381Z][compute][end][input_embedding][sbatch_tokens: 1038, ubatch_tokens: 512]
[0][2025-12-07T15:42:13.382Z][comm][start][send_tensors][sbatch_tokens: 1038, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-07T15:42:13.382Z][compute][start][send_tensors][compress]
[0][2025-12-07T15:42:13.665Z][compute][end][send_tensors][compress]
[0][2025-12-07T15:42:13.666Z][comm][end][send_tensors][sbatch_tokens: 1038, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-07T15:42:13.666Z][comm][start][recv_tensors][sbatch_tokens: 1038, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-07T15:42:16.299Z][compute][start][recv_tensors][decompress]
[0][2025-12-07T15:42:16.303Z][compute][end][recv_tensors][decompress]
[0][2025-12-07T15:42:16.303Z][comm][end][recv_tensors][sbatch_tokens: 1038, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-07T15:42:16.305Z][compute][start][transformer_blocks][sbatch_tokens: 1038, ubatch_tokens: 512]
[0][2025-12-07T15:42:16.319Z][compute][end][transformer_blocks][sbatch_tokens: 1038, ubatch_tokens: 512]
[0][2025-12-07T15:42:16.404Z][compute][start][output_linear][sbatch_tokens: 1038, ubatch_tokens: 512]
[0][2025-12-07T15:42:16.404Z][compute][end][output_linear][sbatch_tokens: 1038, ubatch_tokens: 512]
"""

def parse_logs(data):
    # Dictionary to store start times
    start_times = {}
    # Dictionary to store calculated durations
    durations = {}
    
    # Specific timestamps for Total FWD calculation
    fwd_start_time = None
    fwd_end_time = None

    lines = data.strip().split('\n')

    for line in lines:
        if not line.strip(): continue

        # Remove outer brackets and split by ']['
        # Logic: '[A][B]' -> 'A][B' -> split on ']['
        clean_line = line.strip()[1:-1]
        parts = clean_line.split('][')

        # Structure based on log:
        # [0]: Rank
        # [1]: Timestamp
        # [2]: Type (compute/comm)
        # [3]: State (start/end)
        # [4]: Name (input_embedding, etc.)
        # [5]: Extra info (sbatch_tokens or specific operations like compress)
        
        if len(parts) < 6: continue # Skip malformed lines

        timestamp_str = parts[1]
        state = parts[3]
        name = parts[4]
        extra_info = parts[5]

        # Parse Timestamp
        curr_time = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")

        # Identify the event key
        event_key = None
        
        if name == "input_embedding":
            event_key = "input_embedding"
            if state == "start": fwd_start_time = curr_time
            
        elif name == "output_linear":
            event_key = "output_linear"
            if state == "end": fwd_end_time = curr_time
            
        elif name == "transformer_blocks":
            event_key = "transformer_blocks"
            
        elif name == "send_tensors" and "compress" in extra_info:
            event_key = "compress"
            
        elif name == "recv_tensors" and "decompress" in extra_info:
            event_key = "decompress"

        # Calculate duration if it's a tracked event
        if event_key:
            if state == "start":
                start_times[event_key] = curr_time
            elif state == "end" and event_key in start_times:
                duration_ms = (curr_time - start_times[event_key]).total_seconds() * 1000
                durations[event_key] = duration_ms

    # Calculate Total FWD Time
    total_fwd = 0
    if fwd_start_time and fwd_end_time:
        total_fwd = (fwd_end_time - fwd_start_time).total_seconds() * 1000

    return durations, total_fwd

# Run the parser
metrics, total_fwd_time = parse_logs(log_data)

# formatting output to match your list
print(f"1. Total fwd time: {total_fwd_time:.2f} ms")
print(f"2. Input embedding compute time: {metrics.get('input_embedding', 0):.2f} ms")
print(f"3. 4 x Transformer block compute: {4 * metrics.get('transformer_blocks', 0):.2f} ms")
print(f"4. Output layer compute time: {metrics.get('output_linear', 0):.2f} ms")
print(f"5. 4 x Compress time: {4 * metrics.get('compress', 0):.2f} ms")
print(f"6. 4 x Decompress time: {4 * metrics.get('decompress', 0):.2f} ms")
print(f"7. 4 x estimate RTT/2 time: {80:.2f} ms")

others = total_fwd_time - (4 * metrics.get('transformer_blocks', 0)) - metrics.get('input_embedding', 0) - metrics.get('output_linear', 0) - (4 * metrics.get('compress', 0)) - (4 * metrics.get('decompress', 0)) - 80

total_compression_overhead = ((4 * metrics.get('compress', 0)) + (4 * metrics.get('decompress', 0))) * 100 / total_fwd_time

print(f"8. others (overhead and payload/network BW): {others:.2f} ms")
print(f"9. total compression overhead (%): {total_compression_overhead:.2f} %")