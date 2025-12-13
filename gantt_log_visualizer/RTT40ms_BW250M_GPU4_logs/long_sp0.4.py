rank_0_log="""
[0][2025-12-13T13:06:23.578Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:06:23.895Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:06:23.897Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T13:06:23.897Z][compute][start][send_tensors][compress]
[0][2025-12-13T13:06:24.192Z][compute][end][send_tensors][compress]
[0][2025-12-13T13:06:24.200Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T13:06:24.200Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T13:06:27.119Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T13:06:27.125Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T13:06:27.125Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T13:06:27.127Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:06:27.131Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:06:27.224Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:06:27.225Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T13:06:21.014Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T13:06:24.560Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T13:06:24.565Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T13:06:24.565Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T13:06:24.567Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T13:06:24.571Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T13:06:24.673Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T13:06:24.673Z][compute][start][send_tensors][compress]
[1][2025-12-13T13:06:25.031Z][compute][end][send_tensors][compress]
[1][2025-12-13T13:06:25.038Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T13:06:21.975Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T13:06:25.421Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T13:06:25.427Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T13:06:25.427Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T13:06:25.429Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T13:06:25.433Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T13:06:25.534Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T13:06:25.534Z][compute][start][send_tensors][compress]
[2][2025-12-13T13:06:25.891Z][compute][end][send_tensors][compress]
[2][2025-12-13T13:06:25.898Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T13:06:22.928Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T13:06:26.268Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T13:06:26.272Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T13:06:26.272Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T13:06:26.275Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T13:06:26.278Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T13:06:26.377Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T13:06:26.377Z][compute][start][send_tensors][compress]
[3][2025-12-13T13:06:26.724Z][compute][end][send_tensors][compress]
[3][2025-12-13T13:06:26.729Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""