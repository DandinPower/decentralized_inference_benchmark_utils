rank_0_log="""
[0][2025-12-13T12:58:38.091Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:58:38.410Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:58:38.411Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:58:38.411Z][compute][start][send_tensors][compress]
[0][2025-12-13T12:58:38.711Z][compute][end][send_tensors][compress]
[0][2025-12-13T12:58:38.722Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:58:38.722Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:58:42.332Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T12:58:42.338Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T12:58:42.338Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:58:42.341Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:58:42.345Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:58:42.438Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:58:42.438Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T12:58:35.009Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:58:39.276Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T12:58:39.282Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T12:58:39.282Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:58:39.284Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:58:39.288Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:58:39.390Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T12:58:39.390Z][compute][start][send_tensors][compress]
[1][2025-12-13T12:58:39.752Z][compute][end][send_tensors][compress]
[1][2025-12-13T12:58:39.763Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T12:58:36.143Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:58:40.292Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T12:58:40.297Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T12:58:40.297Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:58:40.299Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:58:40.303Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:58:40.402Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T12:58:40.402Z][compute][start][send_tensors][compress]
[2][2025-12-13T12:58:40.760Z][compute][end][send_tensors][compress]
[2][2025-12-13T12:58:40.768Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T12:58:37.269Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:58:41.318Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T12:58:41.323Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T12:58:41.323Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:58:41.325Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:58:41.329Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:58:41.427Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T12:58:41.427Z][compute][start][send_tensors][compress]
[3][2025-12-13T12:58:41.784Z][compute][end][send_tensors][compress]
[3][2025-12-13T12:58:41.801Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""