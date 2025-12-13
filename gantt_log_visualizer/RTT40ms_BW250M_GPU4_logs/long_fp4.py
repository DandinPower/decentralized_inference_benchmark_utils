rank_0_log="""
[0][2025-12-13T12:54:07.095Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:54:07.406Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:54:07.408Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:54:07.408Z][compute][start][send_tensors][compress]
[0][2025-12-13T12:54:07.418Z][compute][end][send_tensors][compress]
[0][2025-12-13T12:54:07.419Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:54:07.419Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:54:08.114Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T12:54:08.116Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T12:54:08.116Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:54:08.119Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:54:08.123Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:54:08.216Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:54:08.216Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T12:54:06.105Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:54:07.504Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T12:54:07.507Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T12:54:07.507Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:54:07.510Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:54:07.513Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:54:07.615Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T12:54:07.615Z][compute][start][send_tensors][compress]
[1][2025-12-13T12:54:07.623Z][compute][end][send_tensors][compress]
[1][2025-12-13T12:54:07.623Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T12:54:06.426Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:54:07.709Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T12:54:07.713Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T12:54:07.713Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:54:07.716Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:54:07.720Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:54:07.818Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T12:54:07.818Z][compute][start][send_tensors][compress]
[2][2025-12-13T12:54:07.828Z][compute][end][send_tensors][compress]
[2][2025-12-13T12:54:07.828Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T12:54:06.758Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:54:07.914Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T12:54:07.918Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T12:54:07.918Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:54:07.920Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:54:07.924Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:54:08.020Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T12:54:08.020Z][compute][start][send_tensors][compress]
[3][2025-12-13T12:54:08.028Z][compute][end][send_tensors][compress]
[3][2025-12-13T12:54:08.029Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""