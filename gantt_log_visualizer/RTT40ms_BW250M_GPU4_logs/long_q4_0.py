rank_0_log="""
[0][2025-12-13T11:59:24.813Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T11:59:25.169Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T11:59:25.171Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T11:59:25.171Z][compute][start][send_tensors][compress]
[0][2025-12-13T11:59:25.175Z][compute][end][send_tensors][compress]
[0][2025-12-13T11:59:25.176Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T11:59:25.176Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T11:59:25.914Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T11:59:25.915Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T11:59:25.915Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T11:59:25.917Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T11:59:25.921Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T11:59:26.014Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T11:59:26.014Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T11:59:23.744Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T11:59:25.280Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T11:59:25.280Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T11:59:25.280Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T11:59:25.283Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T11:59:25.287Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T11:59:25.385Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T11:59:25.385Z][compute][start][send_tensors][compress]
[1][2025-12-13T11:59:25.391Z][compute][end][send_tensors][compress]
[1][2025-12-13T11:59:25.391Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T11:59:24.078Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T11:59:25.494Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T11:59:25.494Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T11:59:25.494Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T11:59:25.498Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T11:59:25.502Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T11:59:25.598Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T11:59:25.598Z][compute][start][send_tensors][compress]
[2][2025-12-13T11:59:25.601Z][compute][end][send_tensors][compress]
[2][2025-12-13T11:59:25.601Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
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