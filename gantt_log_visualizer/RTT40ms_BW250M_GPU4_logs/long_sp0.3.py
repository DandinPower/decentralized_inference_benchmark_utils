rank_0_log="""
[0][2025-12-13T13:09:35.237Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:09:35.534Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:09:35.536Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T13:09:35.536Z][compute][start][send_tensors][compress]
[0][2025-12-13T13:09:35.825Z][compute][end][send_tensors][compress]
[0][2025-12-13T13:09:35.829Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T13:09:35.829Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T13:09:38.380Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T13:09:38.385Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T13:09:38.385Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T13:09:38.387Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:09:38.391Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:09:38.485Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:09:38.485Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T13:09:32.975Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T13:09:36.129Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T13:09:36.134Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T13:09:36.134Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T13:09:36.136Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T13:09:36.140Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T13:09:36.242Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T13:09:36.242Z][compute][start][send_tensors][compress]
[1][2025-12-13T13:09:36.594Z][compute][end][send_tensors][compress]
[1][2025-12-13T13:09:36.598Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T13:09:33.831Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T13:09:36.893Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T13:09:36.897Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T13:09:36.897Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T13:09:36.900Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T13:09:36.903Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T13:09:37.002Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T13:09:37.002Z][compute][start][send_tensors][compress]
[2][2025-12-13T13:09:37.352Z][compute][end][send_tensors][compress]
[2][2025-12-13T13:09:37.355Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T13:09:34.707Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T13:09:37.627Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T13:09:37.631Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T13:09:37.631Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T13:09:37.634Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T13:09:37.637Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T13:09:37.736Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T13:09:37.736Z][compute][start][send_tensors][compress]
[3][2025-12-13T13:09:38.080Z][compute][end][send_tensors][compress]
[3][2025-12-13T13:09:38.083Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""