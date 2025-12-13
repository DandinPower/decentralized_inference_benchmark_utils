rank_0_log="""
[0][2025-12-13T12:47:21.660Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:47:21.973Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:47:21.975Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:47:21.975Z][compute][start][send_tensors][compress]
[0][2025-12-13T12:47:21.986Z][compute][end][send_tensors][compress]
[0][2025-12-13T12:47:21.987Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:47:21.987Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:47:22.711Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T12:47:22.716Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T12:47:22.716Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:47:22.718Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:47:22.722Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:47:22.812Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:47:22.812Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T12:47:20.624Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:47:22.077Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T12:47:22.083Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T12:47:22.083Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:47:22.086Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:47:22.090Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:47:22.188Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T12:47:22.188Z][compute][start][send_tensors][compress]
[1][2025-12-13T12:47:22.196Z][compute][end][send_tensors][compress]
[1][2025-12-13T12:47:22.197Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T12:47:20.955Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:47:22.287Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T12:47:22.292Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T12:47:22.292Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:47:22.295Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:47:22.299Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:47:22.398Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T12:47:22.398Z][compute][start][send_tensors][compress]
[2][2025-12-13T12:47:22.406Z][compute][end][send_tensors][compress]
[2][2025-12-13T12:47:22.407Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T12:47:21.292Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:47:22.496Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T12:47:22.502Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T12:47:22.502Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:47:22.504Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:47:22.508Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:47:22.606Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T12:47:22.606Z][compute][start][send_tensors][compress]
[3][2025-12-13T12:47:22.621Z][compute][end][send_tensors][compress]
[3][2025-12-13T12:47:22.621Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""