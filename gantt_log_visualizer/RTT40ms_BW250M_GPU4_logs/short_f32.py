rank_0_log="""
[0][2025-12-13T11:40:50.463Z][compute][start][input_embedding][sbatch_tokens: 0, ubatch_tokens: 14]
[0][2025-12-13T11:40:50.468Z][compute][end][input_embedding][sbatch_tokens: 0, ubatch_tokens: 14]
[0][2025-12-13T11:40:50.468Z][comm][start][send_tensors][sbatch_tokens: 0, ubatch_tokens: 14, send the result to the next node or the master]
[0][2025-12-13T11:40:50.468Z][comm][end][send_tensors][sbatch_tokens: 0, ubatch_tokens: 14, send the result to the next node or the master]
[0][2025-12-13T11:40:50.468Z][comm][start][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 14, receive data from other nodes]
[0][2025-12-13T11:40:50.653Z][comm][end][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 14, receive data from other nodes]
[0][2025-12-13T11:40:50.653Z][compute][start][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 14]
[0][2025-12-13T11:40:50.657Z][compute][end][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 14]
[0][2025-12-13T11:40:50.674Z][compute][start][output_linear][sbatch_tokens: 0, ubatch_tokens: 14]
[0][2025-12-13T11:40:50.674Z][compute][end][output_linear][sbatch_tokens: 0, ubatch_tokens: 14]
"""

rank_1_log="""
[1][2025-12-13T11:40:48.330Z][comm][start][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 14, receive data from other nodes]
[1][2025-12-13T11:40:50.498Z][comm][end][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 14, receive data from other nodes]
[1][2025-12-13T11:40:50.498Z][compute][start][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 14]
[1][2025-12-13T11:40:50.502Z][compute][end][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 14]
[1][2025-12-13T11:40:50.520Z][comm][start][send_tensors][sbatch_tokens: 0, ubatch_tokens: 14, send the result to the next node or the master]
[1][2025-12-13T11:40:50.521Z][comm][end][send_tensors][sbatch_tokens: 0, ubatch_tokens: 14, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T11:40:49.057Z][comm][start][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 14, receive data from other nodes]
[2][2025-12-13T11:40:50.552Z][comm][end][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 14, receive data from other nodes]
[2][2025-12-13T11:40:50.552Z][compute][start][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 14]
[2][2025-12-13T11:40:50.555Z][compute][end][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 14]
[2][2025-12-13T11:40:50.572Z][comm][start][send_tensors][sbatch_tokens: 0, ubatch_tokens: 14, send the result to the next node or the master]
[2][2025-12-13T11:40:50.572Z][comm][end][send_tensors][sbatch_tokens: 0, ubatch_tokens: 14, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T11:40:49.768Z][comm][start][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 14, receive data from other nodes]
[3][2025-12-13T11:40:50.602Z][comm][end][recv_tensors][sbatch_tokens: 0, ubatch_tokens: 14, receive data from other nodes]
[3][2025-12-13T11:40:50.602Z][compute][start][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 14]
[3][2025-12-13T11:40:50.605Z][compute][end][transformer_blocks][sbatch_tokens: 0, ubatch_tokens: 14]
[3][2025-12-13T11:40:50.622Z][comm][start][send_tensors][sbatch_tokens: 0, ubatch_tokens: 14, send the result to the next node or the master]
[3][2025-12-13T11:40:50.622Z][comm][end][send_tensors][sbatch_tokens: 0, ubatch_tokens: 14, send the result to the next node or the master]
"""