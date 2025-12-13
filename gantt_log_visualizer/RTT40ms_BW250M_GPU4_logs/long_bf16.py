rank_0_log="""
[0][2025-12-13T12:28:26.988Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:28:27.282Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:28:27.283Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:28:27.283Z][compute][start][send_tensors][compress]
[0][2025-12-13T12:28:27.291Z][compute][end][send_tensors][compress]
[0][2025-12-13T12:28:27.297Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:28:27.297Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:28:28.934Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T12:28:28.935Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T12:28:28.935Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:28:28.937Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:28:28.941Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:28:29.034Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:28:29.034Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T12:28:25.346Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:28:27.629Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T12:28:27.629Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T12:28:27.629Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:28:27.632Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:28:27.635Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:28:27.736Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T12:28:27.736Z][compute][start][send_tensors][compress]
[1][2025-12-13T12:28:27.744Z][compute][end][send_tensors][compress]
[1][2025-12-13T12:28:27.750Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T12:28:25.899Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:28:28.070Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T12:28:28.071Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T12:28:28.071Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:28:28.074Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:28:28.077Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:28:28.176Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T12:28:28.176Z][compute][start][send_tensors][compress]
[2][2025-12-13T12:28:28.182Z][compute][end][send_tensors][compress]
[2][2025-12-13T12:28:28.186Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T12:28:26.437Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:28:28.511Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T12:28:28.511Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T12:28:28.511Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:28:28.514Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:28:28.518Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:28:28.616Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T12:28:28.616Z][compute][start][send_tensors][compress]
[3][2025-12-13T12:28:28.622Z][compute][end][send_tensors][compress]
[3][2025-12-13T12:28:28.632Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""