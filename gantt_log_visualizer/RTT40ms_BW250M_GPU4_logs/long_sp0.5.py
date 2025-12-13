rank_0_log="""
[0][2025-12-13T13:02:44.582Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:02:44.918Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:02:44.920Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T13:02:44.920Z][compute][start][send_tensors][compress]
[0][2025-12-13T13:02:45.232Z][compute][end][send_tensors][compress]
[0][2025-12-13T13:02:45.242Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T13:02:45.242Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T13:02:48.473Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T13:02:48.479Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T13:02:48.479Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T13:02:48.481Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:02:48.485Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:02:48.578Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:02:48.578Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T13:02:41.789Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T13:02:45.708Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T13:02:45.714Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T13:02:45.714Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T13:02:45.716Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T13:02:45.720Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T13:02:45.821Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T13:02:45.822Z][compute][start][send_tensors][compress]
[1][2025-12-13T13:02:46.181Z][compute][end][send_tensors][compress]
[1][2025-12-13T13:02:46.190Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T13:02:42.848Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T13:02:46.633Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T13:02:46.637Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T13:02:46.637Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T13:02:46.640Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T13:02:46.643Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T13:02:46.742Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T13:02:46.742Z][compute][start][send_tensors][compress]
[2][2025-12-13T13:02:47.097Z][compute][end][send_tensors][compress]
[2][2025-12-13T13:02:47.103Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T13:02:43.882Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T13:02:47.546Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T13:02:47.551Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T13:02:47.551Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T13:02:47.553Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T13:02:47.557Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T13:02:47.655Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T13:02:47.655Z][compute][start][send_tensors][compress]
[3][2025-12-13T13:02:48.003Z][compute][end][send_tensors][compress]
[3][2025-12-13T13:02:48.010Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""