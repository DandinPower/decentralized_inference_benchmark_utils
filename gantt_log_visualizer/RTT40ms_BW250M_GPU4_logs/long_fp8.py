rank_0_log="""
[0][2025-12-13T12:38:41.734Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:38:42.053Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:38:42.055Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:38:42.055Z][compute][start][send_tensors][compress]
[0][2025-12-13T12:38:42.066Z][compute][end][send_tensors][compress]
[0][2025-12-13T12:38:42.068Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:38:42.068Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:38:43.076Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T12:38:43.080Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T12:38:43.080Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:38:43.082Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:38:43.086Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:38:43.179Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:38:43.180Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T12:38:40.506Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:38:42.225Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T12:38:42.230Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T12:38:42.230Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:38:42.232Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:38:42.236Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:38:42.336Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T12:38:42.336Z][compute][start][send_tensors][compress]
[1][2025-12-13T12:38:42.347Z][compute][end][send_tensors][compress]
[1][2025-12-13T12:38:42.349Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T12:38:40.912Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:38:42.524Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T12:38:42.528Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T12:38:42.528Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:38:42.531Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:38:42.534Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:38:42.632Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T12:38:42.632Z][compute][start][send_tensors][compress]
[2][2025-12-13T12:38:42.643Z][compute][end][send_tensors][compress]
[2][2025-12-13T12:38:42.645Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T12:38:41.312Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:38:42.802Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T12:38:42.806Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T12:38:42.806Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:38:42.808Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:38:42.812Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:38:42.907Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T12:38:42.907Z][compute][start][send_tensors][compress]
[3][2025-12-13T12:38:42.917Z][compute][end][send_tensors][compress]
[3][2025-12-13T12:38:42.919Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""