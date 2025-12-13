rank_0_log="""
[0][2025-12-13T13:12:43.522Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:12:43.849Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:12:43.851Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T13:12:43.851Z][compute][start][send_tensors][compress]
[0][2025-12-13T13:12:44.136Z][compute][end][send_tensors][compress]
[0][2025-12-13T13:12:44.139Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T13:12:44.139Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T13:12:46.337Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T13:12:46.342Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T13:12:46.342Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T13:12:46.344Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:12:46.348Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:12:46.441Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:12:46.441Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T13:12:41.545Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T13:12:44.325Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T13:12:44.331Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T13:12:44.331Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T13:12:44.333Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T13:12:44.337Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T13:12:44.439Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T13:12:44.439Z][compute][start][send_tensors][compress]
[1][2025-12-13T13:12:44.789Z][compute][end][send_tensors][compress]
[1][2025-12-13T13:12:44.792Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T13:12:42.309Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T13:12:45.005Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T13:12:45.008Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T13:12:45.008Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T13:12:45.011Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T13:12:45.014Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T13:12:45.113Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T13:12:45.113Z][compute][start][send_tensors][compress]
[2][2025-12-13T13:12:45.463Z][compute][end][send_tensors][compress]
[2][2025-12-13T13:12:45.465Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T13:12:43.074Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T13:12:45.676Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T13:12:45.679Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T13:12:45.679Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T13:12:45.682Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T13:12:45.685Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T13:12:45.784Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T13:12:45.784Z][compute][start][send_tensors][compress]
[3][2025-12-13T13:12:46.129Z][compute][end][send_tensors][compress]
[3][2025-12-13T13:12:46.131Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""