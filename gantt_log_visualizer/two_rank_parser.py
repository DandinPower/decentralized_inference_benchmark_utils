import re
from datetime import datetime

# --- LOG DATA ---
rank_0_log = """
[0][2025-12-13T08:40:52.376Z][compute][start][input_embedding][sbatch_tokens: 1038, ubatch_tokens: 512]                                                                                                                                                                                                                     
[0][2025-12-13T08:40:52.376Z][compute][end][input_embedding][sbatch_tokens: 1038, ubatch_tokens: 512]                                                                                                                                                                                                                       
[0][2025-12-13T08:40:52.377Z][comm][start][send_tensors][sbatch_tokens: 1038, ubatch_tokens: 512, send the result to the next node or the master]                                                                                                                                                                           
[0][2025-12-13T08:40:52.377Z][compute][start][send_tensors][compress]                                                                                                                                                                                                                                                       
[0][2025-12-13T08:40:52.381Z][compute][end][send_tensors][compress]                                                                                                                                                                                                                                                         
[0][2025-12-13T08:40:52.382Z][comm][end][send_tensors][sbatch_tokens: 1038, ubatch_tokens: 512, send the result to the next node or the master]                                                                                                                                                                             
[0][2025-12-13T08:40:52.382Z][comm][start][recv_tensors][sbatch_tokens: 1038, ubatch_tokens: 512, receive data from other nodes]                                                                                                                                                                                            
[0][2025-12-13T08:40:52.846Z][compute][start][recv_tensors][decompress]                                                                                                                                                                                                                                                     
[0][2025-12-13T08:40:52.846Z][compute][end][recv_tensors][decompress]                                                                                                                                                                                                                                                       
[0][2025-12-13T08:40:52.847Z][comm][end][recv_tensors][sbatch_tokens: 1038, ubatch_tokens: 512, receive data from other nodes]                                                                                                                                                                                              
[0][2025-12-13T08:40:52.851Z][compute][start][transformer_blocks][sbatch_tokens: 1038, ubatch_tokens: 512]                                                                                                                                                                                                                  
[0][2025-12-13T08:40:52.871Z][compute][end][transformer_blocks][sbatch_tokens: 1038, ubatch_tokens: 512]                                                                                                                                                                                                                    
[0][2025-12-13T08:40:52.943Z][compute][start][output_linear][sbatch_tokens: 1038, ubatch_tokens: 512]                                                                                                                                                                                                                       
[0][2025-12-13T08:40:52.943Z][compute][end][output_linear][sbatch_tokens: 1038, ubatch_tokens: 512]
"""

rank_1_log = """
[1][2025-12-13T08:40:52.383Z][comm][start][recv_tensors][sbatch_tokens: 1038, ubatch_tokens: 512, receive data from other nodes]            
[1][2025-12-13T08:40:52.558Z][compute][start][recv_tensors][decompress]                                                                                       
[1][2025-12-13T08:40:52.562Z][compute][end][recv_tensors][decompress]                                                                                         
[1][2025-12-13T08:40:52.562Z][comm][end][recv_tensors][sbatch_tokens: 1038, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T08:40:52.563Z][compute][start][transformer_blocks][sbatch_tokens: 1038, ubatch_tokens: 512]                                  
[1][2025-12-13T08:40:52.586Z][compute][end][transformer_blocks][sbatch_tokens: 1038, ubatch_tokens: 512]                                  
[1][2025-12-13T08:40:52.668Z][comm][start][send_tensors][sbatch_tokens: 1038, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T08:40:52.668Z][compute][start][send_tensors][compress]                                                                                         
[1][2025-12-13T08:40:52.670Z][compute][end][send_tensors][compress]                                                                                           
[1][2025-12-13T08:40:52.671Z][comm][end][send_tensors][sbatch_tokens: 1038, ubatch_tokens: 512, send the result to the next node or the master]
"""

def parse_rank_log(data):
    """Parses a single rank log into a list of event dicts."""
    events = []
    lines = data.strip().split('\n')
    pending_starts = {}

    for line in lines:
        if not line.strip(): continue

        # Format: [Rank][Time][Type][State][Name][Extra]
        clean_line = line.strip()[1:-1]
        parts = clean_line.split('][')
        if len(parts) < 6: continue

        rank = int(parts[0])
        timestamp_str = parts[1]
        event_type = parts[2] # compute or comm
        state = parts[3]      # start or end
        name = parts[4]
        extra_info = parts[5]

        # Convert timestamp
        curr_time = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")

        # Create a unique key to match Start/End pairs
        # We must distinguish "send_tensors"(comm) from "send_tensors"(compute/compress)
        is_compress = "compress" in extra_info
        is_decompress = "decompress" in extra_info
        
        # Categorize for key matching
        subtype = "main"
        if is_compress: subtype = "compress"
        elif is_decompress: subtype = "decompress"
        
        key = (name, event_type, subtype)

        if state == "start":
            pending_starts[key] = curr_time
        elif state == "end":
            if key in pending_starts:
                start_time = pending_starts.pop(key)
                duration_ms = (curr_time - start_time).total_seconds() * 1000
                
                # Assign a simple category for aggregation
                category = name
                if subtype == "compress": category = "compress"
                if subtype == "decompress": category = "decompress"

                events.append({
                    "rank": rank,
                    "category": category,
                    "type": event_type,
                    "name": name,
                    "start_time": start_time,
                    "end_time": curr_time,
                    "duration_ms": duration_ms
                })
    return events

def run_two_rank_analysis():
    # 1. Parse both logs
    events_0 = parse_rank_log(rank_0_log)
    events_1 = parse_rank_log(rank_1_log)
    all_events = events_0 + events_1

    # 2. Aggregate Compute Metrics (Summing durations from both ranks)
    metrics = {
        "input_embedding": 0,
        "transformer_blocks": 0,
        "output_linear": 0,
        "compress": 0,
        "decompress": 0
    }

    for e in all_events:
        cat = e["category"]
        if cat in metrics:
            metrics[cat] += e["duration_ms"]

    # 3. Calculate Total Pipeline FWD Time
    # Pipeline Start: Rank 0 'input_embedding' Start
    # Pipeline End:   Rank 0 'output_linear' End
    # (Assuming Rank 0 is the master that starts and finishes the full cycle)
    r0_input_start = next((e["start_time"] for e in events_0 if e["name"] == "input_embedding"), None)
    r0_output_end = next((e["end_time"] for e in events_0 if e["name"] == "output_linear"), None)

    total_fwd_time = 0
    if r0_input_start and r0_output_end:
        total_fwd_time = (r0_output_end - r0_input_start).total_seconds() * 1000

    # 4. Calculate REAL Communication Latency
    # Logic: (Recv Node End Time) - (Send Node End Time)
    
    # helper to find comm end time
    def get_comm_end(events, name):
        # We look for type='comm' and name matches
        match = next((e for e in events if e["name"] == name and e["type"] == "comm"), None)
        return match["end_time"] if match else None

    # Latency 1: Rank 0 -> Rank 1
    t_send_0 = get_comm_end(events_0, "send_tensors")
    t_recv_1 = get_comm_end(events_1, "recv_tensors")
    lat_0_to_1 = (t_recv_1 - t_send_0).total_seconds() * 1000 if (t_send_0 and t_recv_1) else 0

    # Latency 2: Rank 1 -> Rank 0
    t_send_1 = get_comm_end(events_1, "send_tensors")
    t_recv_0 = get_comm_end(events_0, "recv_tensors")
    lat_1_to_0 = (t_recv_0 - t_send_1).total_seconds() * 1000 if (t_send_1 and t_recv_0) else 0

    total_real_latency = lat_0_to_1 + lat_1_to_0

    # 5. Calculate "Others"
    # Others = Total FWD - (All Compute) - (Real Network Latency)
    # This represents uncaptured overhead or gaps.
    total_compute = metrics["input_embedding"] + metrics["transformer_blocks"] + \
                    metrics["output_linear"] + metrics["compress"] + metrics["decompress"]
    
    others = total_fwd_time - total_compute - total_real_latency

    # 6. Compression Overhead %
    total_compression_overhead = ((metrics['compress'] + metrics['decompress']) * 100) / total_fwd_time if total_fwd_time > 0 else 0

    # --- PRINT RESULTS ---
    print(f"1. Total fwd time: {total_fwd_time:.2f} ms")
    print(f"2. Input embedding compute time: {metrics['input_embedding']:.2f} ms")
    print(f"3. Total Transformer block compute: {metrics['transformer_blocks']:.2f} ms")
    print(f"4. Output layer compute time: {metrics['output_linear']:.2f} ms")
    print(f"5. Total Compress time: {metrics['compress']:.2f} ms")
    print(f"6. Total Decompress time: {metrics['decompress']:.2f} ms")
    print(f"7. Real Communication Latency (R0->R1 + R1->R0): {total_real_latency:.2f} ms")
    print(f"8. Others (unaccounted gaps): {others:.2f} ms")
    print(f"9. Total compression overhead (%): {total_compression_overhead:.2f} %")

    # Debug print to verify latency components
    print("-" * 30)
    print(f"DEBUG Details:")
    print(f"Latency R0->R1 (R1_Recv_End - R0_Send_End): {lat_0_to_1:.2f} ms")
    print(f"Latency R1->R0 (R0_Recv_End - R1_Send_End): {lat_1_to_0:.2f} ms")

if __name__ == "__main__":
    run_two_rank_analysis()