rank_0_log="""
[0][2025-12-13T12:14:02.956Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:14:03.320Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:14:03.322Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:14:03.322Z][compute][start][send_tensors][compress]
[0][2025-12-13T12:14:03.428Z][compute][end][send_tensors][compress]
[0][2025-12-13T12:14:03.429Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:14:03.429Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:14:04.310Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T12:14:04.312Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T12:14:04.312Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:14:04.314Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:14:04.318Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:14:04.412Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:14:04.412Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T12:13:53.492Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:14:03.489Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T12:14:03.490Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T12:14:03.490Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:14:03.493Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:14:03.497Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:14:03.598Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T12:14:03.598Z][compute][start][send_tensors][compress]
[1][2025-12-13T12:14:03.703Z][compute][end][send_tensors][compress]
[1][2025-12-13T12:14:03.703Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T12:13:58.127Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:14:03.763Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T12:14:03.769Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T12:14:03.769Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:14:03.771Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:14:03.775Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:14:03.875Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T12:14:03.875Z][compute][start][send_tensors][compress]
[2][2025-12-13T12:14:03.980Z][compute][end][send_tensors][compress]
[2][2025-12-13T12:14:03.980Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T12:14:02.653Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:14:04.041Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T12:14:04.043Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T12:14:04.043Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:14:04.045Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:14:04.049Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:14:04.147Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T12:14:04.147Z][compute][start][send_tensors][compress]
[3][2025-12-13T12:14:04.250Z][compute][end][send_tensors][compress]
[3][2025-12-13T12:14:04.251Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""