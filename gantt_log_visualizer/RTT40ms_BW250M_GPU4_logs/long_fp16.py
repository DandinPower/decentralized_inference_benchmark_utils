rank_0_log="""
[0][2025-12-13T12:32:24.230Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:32:24.529Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:32:24.531Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:32:24.531Z][compute][start][send_tensors][compress]
[0][2025-12-13T12:32:24.539Z][compute][end][send_tensors][compress]
[0][2025-12-13T12:32:24.546Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:32:24.546Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:32:26.190Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T12:32:26.191Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T12:32:26.191Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:32:26.194Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:32:26.198Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:32:26.291Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:32:26.291Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T12:32:22.571Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:32:24.866Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T12:32:24.867Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T12:32:24.867Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:32:24.869Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:32:24.873Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:32:24.972Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T12:32:24.972Z][compute][start][send_tensors][compress]
[1][2025-12-13T12:32:24.980Z][compute][end][send_tensors][compress]
[1][2025-12-13T12:32:24.987Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T12:32:23.121Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:32:25.318Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T12:32:25.319Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T12:32:25.319Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:32:25.322Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:32:25.326Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:32:25.425Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T12:32:25.425Z][compute][start][send_tensors][compress]
[2][2025-12-13T12:32:25.433Z][compute][end][send_tensors][compress]
[2][2025-12-13T12:32:25.439Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T12:32:23.661Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:32:25.747Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T12:32:25.747Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T12:32:25.747Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:32:25.750Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:32:25.754Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:32:25.852Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T12:32:25.852Z][compute][start][send_tensors][compress]
[3][2025-12-13T12:32:25.858Z][compute][end][send_tensors][compress]
[3][2025-12-13T12:32:25.862Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""