rank_0_log="""
[0][2025-12-13T12:17:21.765Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:17:22.123Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:17:22.125Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:17:22.125Z][compute][start][send_tensors][compress]
[0][2025-12-13T12:17:22.472Z][compute][end][send_tensors][compress]
[0][2025-12-13T12:17:22.472Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:17:22.472Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:17:24.032Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T12:17:24.034Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T12:17:24.034Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:17:24.036Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:17:24.040Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:17:24.133Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:17:24.133Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T12:17:16.135Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:17:22.531Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T12:17:22.533Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T12:17:22.533Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:17:22.536Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:17:22.539Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:17:22.641Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T12:17:22.641Z][compute][start][send_tensors][compress]
[1][2025-12-13T12:17:22.977Z][compute][end][send_tensors][compress]
[1][2025-12-13T12:17:22.977Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T12:17:18.806Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:17:23.036Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T12:17:23.038Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T12:17:23.038Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:17:23.041Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:17:23.045Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:17:23.144Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T12:17:23.145Z][compute][start][send_tensors][compress]
[2][2025-12-13T12:17:23.483Z][compute][end][send_tensors][compress]
[2][2025-12-13T12:17:23.483Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T12:17:21.483Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:17:23.541Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T12:17:23.543Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T12:17:23.543Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:17:23.545Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:17:23.549Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:17:23.647Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T12:17:23.647Z][compute][start][send_tensors][compress]
[3][2025-12-13T12:17:23.974Z][compute][end][send_tensors][compress]
[3][2025-12-13T12:17:23.974Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""