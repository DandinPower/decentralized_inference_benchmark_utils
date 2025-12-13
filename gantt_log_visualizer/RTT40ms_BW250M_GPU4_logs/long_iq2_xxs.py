rank_0_log="""
[0][2025-12-13T12:25:04.873Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:25:05.225Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:25:05.226Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:25:05.226Z][compute][start][send_tensors][compress]
[0][2025-12-13T12:25:05.410Z][compute][end][send_tensors][compress]
[0][2025-12-13T12:25:05.411Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:25:05.411Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:25:06.477Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T12:25:06.479Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T12:25:06.479Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:25:06.482Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:25:06.486Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:25:06.579Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:25:06.579Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T12:25:01.664Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:25:05.467Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T12:25:05.469Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T12:25:05.469Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:25:05.472Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:25:05.475Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:25:05.576Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T12:25:05.576Z][compute][start][send_tensors][compress]
[1][2025-12-13T12:25:05.748Z][compute][end][send_tensors][compress]
[1][2025-12-13T12:25:05.748Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T12:25:03.122Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:25:05.807Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T12:25:05.809Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T12:25:05.809Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:25:05.812Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:25:05.816Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:25:05.915Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T12:25:05.915Z][compute][start][send_tensors][compress]
[2][2025-12-13T12:25:06.094Z][compute][end][send_tensors][compress]
[2][2025-12-13T12:25:06.094Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T12:25:04.580Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:25:06.153Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T12:25:06.155Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T12:25:06.155Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:25:06.157Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:25:06.161Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:25:06.259Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T12:25:06.259Z][compute][start][send_tensors][compress]
[3][2025-12-13T12:25:06.425Z][compute][end][send_tensors][compress]
[3][2025-12-13T12:25:06.426Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""