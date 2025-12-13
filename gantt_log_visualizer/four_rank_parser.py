from datetime import datetime

RTT = 40

rank_0_log="""
[0][2025-12-13T13:15:40.459Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:15:40.761Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:15:40.763Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T13:15:40.763Z][compute][start][send_tensors][compress]
[0][2025-12-13T13:15:41.047Z][compute][end][send_tensors][compress]
[0][2025-12-13T13:15:41.049Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T13:15:41.049Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T13:15:42.813Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T13:15:42.817Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T13:15:42.817Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T13:15:42.819Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:15:42.823Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:15:42.916Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:15:42.916Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T13:15:38.710Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T13:15:41.149Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T13:15:41.153Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T13:15:41.153Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T13:15:41.155Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T13:15:41.159Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T13:15:41.261Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T13:15:41.261Z][compute][start][send_tensors][compress]
[1][2025-12-13T13:15:41.608Z][compute][end][send_tensors][compress]
[1][2025-12-13T13:15:41.609Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T13:15:39.403Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T13:15:41.708Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T13:15:41.711Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T13:15:41.711Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T13:15:41.713Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T13:15:41.717Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T13:15:41.816Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T13:15:41.816Z][compute][start][send_tensors][compress]
[2][2025-12-13T13:15:42.163Z][compute][end][send_tensors][compress]
[2][2025-12-13T13:15:42.163Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T13:15:40.076Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T13:15:42.262Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T13:15:42.265Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T13:15:42.265Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T13:15:42.267Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T13:15:42.271Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T13:15:42.369Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T13:15:42.369Z][compute][start][send_tensors][compress]
[3][2025-12-13T13:15:42.713Z][compute][end][send_tensors][compress]
[3][2025-12-13T13:15:42.714Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
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

def run_analysis():
    # 1. Parse both logs
    events_0 = parse_rank_log(rank_0_log)
    events_1 = parse_rank_log(rank_1_log)
    events_2 = parse_rank_log(rank_2_log)
    events_3 = parse_rank_log(rank_3_log)
    all_events = events_0 + events_1 + events_2 + events_3

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

    # Latency 2: Rank 1 -> Rank 2
    t_send_1 = get_comm_end(events_1, "send_tensors")
    t_recv_2 = get_comm_end(events_2, "recv_tensors")
    lat_1_to_2 = (t_recv_2 - t_send_1).total_seconds() * 1000 if (t_send_1 and t_recv_2) else 0

    # Latency 3: Rank 2 -> Rank 3
    t_send_2 = get_comm_end(events_2, "send_tensors")
    t_recv_3 = get_comm_end(events_3, "recv_tensors")
    lat_2_to_3 = (t_recv_3 - t_send_2).total_seconds() * 1000 if (t_send_2 and t_recv_3) else 0

    # Latency 4: Rank 3 -> Rank 0
    t_send_3 = get_comm_end(events_3, "send_tensors")
    t_recv_0 = get_comm_end(events_0, "recv_tensors")
    lat_3_to_0 = (t_recv_0 - t_send_3).total_seconds() * 1000 if (t_send_3 and t_recv_0) else 0


    total_real_latency = lat_0_to_1 + lat_1_to_2 + lat_2_to_3 + lat_3_to_0
    basic_net_latency = 4 * (RTT / 2)
    payload_latency = total_real_latency - basic_net_latency

    # 5. Calculate "Others"
    # Others = Total FWD - (All Compute) - (Real Network Latency)
    # This represents uncaptured overhead or gaps.
    total_compute = metrics["input_embedding"] + metrics["transformer_blocks"] + \
                    metrics["output_linear"] + metrics["compress"] + metrics["decompress"]
    
    others = total_fwd_time - total_compute - total_real_latency

    # 6. Compression Overhead %
    total_compression_overhead = ((metrics['compress'] + metrics['decompress']) * 100) / total_fwd_time if total_fwd_time > 0 else 0

    # Communication Overhead %
    total_communication_overhead = total_real_latency * 100 / total_fwd_time if total_fwd_time > 0 else 0

    # --- PRINT RESULTS ---
    print(f"[Compute] Input embedding compute time: {metrics['input_embedding']:.2f} ms")
    print(f"[Compute] Total Transformer block compute: {metrics['transformer_blocks']:.2f} ms")
    print(f"[Compute] Output layer compute time: {metrics['output_linear']:.2f} ms")
    print(f"[Compress] Total Compress time: {metrics['compress']:.2f} ms")
    print(f"[Compress] Total Decompress time: {metrics['decompress']:.2f} ms")
    print(f"[Comm] Real Communication Latency (R0->R1 + R1->R2 + R2->R3 + R3->R0): {total_real_latency:.2f} ms")
    print(f"[Comm] Estimated Basic Propagation Latency (4 x RTT/2): {basic_net_latency:.2f} ms")
    print(f"[Comm] Estimated Payload Latency: {payload_latency:.2f} ms")
    print(f"[Others] (layer switch overhead (transformer->output layer), data movement overhead (cpu<->gpu)): {others:.2f} ms")
    print(f"[Stat] Total fwd time: {total_fwd_time:.2f} ms")
    print(f"[Stat] Total compression overhead (%): {total_compression_overhead:.2f} %")
    print(f"[Stat] Total communication overhead (%): {total_communication_overhead:.2f} %")

    # Debug print to verify latency components
    print("-" * 30)
    print(f"DEBUG Details:")
    print(f"Latency R0->R1: {lat_0_to_1:.2f} ms")
    print(f"Latency R1->R2: {lat_1_to_2:.2f} ms")
    print(f"Latency R2->R3: {lat_2_to_3:.2f} ms")
    print(f"Latency R3->R0: {lat_3_to_0:.2f} ms")
    

if __name__ == "__main__":
    run_analysis()