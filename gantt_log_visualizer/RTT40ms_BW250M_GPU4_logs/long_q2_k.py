rank_0_log="""
[0][2025-12-13T11:47:51.781Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T11:47:52.111Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T11:47:52.113Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T11:47:52.113Z][compute][start][send_tensors][compress]
[0][2025-12-13T11:47:52.129Z][compute][end][send_tensors][compress]
[0][2025-12-13T11:47:52.129Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T11:47:52.129Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T11:47:52.718Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T11:47:52.719Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T11:47:52.719Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T11:47:52.721Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T11:47:52.725Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T11:47:52.818Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T11:47:52.818Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T11:47:50.847Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T11:47:52.190Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T11:47:52.191Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T11:47:52.191Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T11:47:52.194Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T11:47:52.197Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T11:47:52.296Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T11:47:52.296Z][compute][start][send_tensors][compress]
[1][2025-12-13T11:47:52.309Z][compute][end][send_tensors][compress]
[1][2025-12-13T11:47:52.309Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T11:47:51.145Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T11:47:52.371Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T11:47:52.371Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T11:47:52.371Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T11:47:52.374Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T11:47:52.378Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T11:47:52.475Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T11:47:52.475Z][compute][start][send_tensors][compress]
[2][2025-12-13T11:47:52.484Z][compute][end][send_tensors][compress]
[2][2025-12-13T11:47:52.485Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T11:47:51.447Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T11:47:52.546Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T11:47:52.546Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T11:47:52.546Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T11:47:52.549Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T11:47:52.552Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T11:47:52.647Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T11:47:52.647Z][compute][start][send_tensors][compress]
[3][2025-12-13T11:47:52.657Z][compute][end][send_tensors][compress]
[3][2025-12-13T11:47:52.657Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""