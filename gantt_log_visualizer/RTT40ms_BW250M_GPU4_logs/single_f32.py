rank_0_log="""
[0][2025-12-13T11:40:50.676Z][compute][start][input_embedding][sbatch_tokens: 0, ubatch_tokens: 1]
[0][2025-12-13T11:40:50.676Z][compute][end][input_embedding][sbatch_tokens: 0, ubatch_tokens: 1]
[0][2025-12-13T11:40:50.676Z][comm][start][send_tensors][sbatch_tokens: 0, ubatch_tokens: 1, send the result to the next node or the master]
[0][2025-12-13T11:40:50.676Z][comm][end][send_tensors][sbatch_tokens: 0, ubatch_tokens: 1, send the result to the next node or the master]
[0][2025-12-13T11:40:50.676Z][comm][start][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 1, receive data from other nodes]
[0][2025-12-13T11:40:50.810Z][comm][end][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 1, receive data from other nodes]
[0][2025-12-13T11:40:50.810Z][compute][start][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 1]
[0][2025-12-13T11:40:50.814Z][compute][end][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 1]
[0][2025-12-13T11:40:50.827Z][compute][start][output_linear][sbatch_tokens: 0, ubatch_tokens: 1]
[0][2025-12-13T11:40:50.827Z][compute][end][output_linear][sbatch_tokens: 0, ubatch_tokens: 1]
"""

rank_1_log="""
[1][2025-12-13T11:40:50.697Z][comm][start][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 1, receive data from other nodes]
[1][2025-12-13T11:40:50.698Z][comm][end][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 1, receive data from other nodes]
[1][2025-12-13T11:40:50.698Z][compute][start][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 1]
[1][2025-12-13T11:40:50.702Z][compute][end][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 1]
[1][2025-12-13T11:40:50.715Z][comm][start][send_tensors][sbatch_tokens: 0, ubatch_tokens: 1, send the result to the next node or the master]
[1][2025-12-13T11:40:50.715Z][comm][end][send_tensors][sbatch_tokens: 0, ubatch_tokens: 1, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T11:40:50.718Z][comm][start][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 1, receive data from other nodes]
[2][2025-12-13T11:40:50.737Z][comm][end][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 1, receive data from other nodes]
[2][2025-12-13T11:40:50.737Z][compute][start][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 1]
[2][2025-12-13T11:40:50.741Z][compute][end][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 1]
[2][2025-12-13T11:40:50.753Z][comm][start][send_tensors][sbatch_tokens: 0, ubatch_tokens: 1, send the result to the next node or the master]
[2][2025-12-13T11:40:50.753Z][comm][end][send_tensors][sbatch_tokens: 0, ubatch_tokens: 1, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T11:40:50.737Z][comm][start][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 1, receive data from other nodes]
[3][2025-12-13T11:40:50.774Z][comm][end][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 1, receive data from other nodes]
[3][2025-12-13T11:40:50.774Z][compute][start][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 1]
[3][2025-12-13T11:40:50.777Z][compute][end][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 1]
[3][2025-12-13T11:40:50.790Z][comm][start][send_tensors][sbatch_tokens: 0, ubatch_tokens: 1, send the result to the next node or the master]
[3][2025-12-13T11:40:50.790Z][comm][end][send_tensors][sbatch_tokens: 0, ubatch_tokens: 1, send the result to the next node or the master]
"""