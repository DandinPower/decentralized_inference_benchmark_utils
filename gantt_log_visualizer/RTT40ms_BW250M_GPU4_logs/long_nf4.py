rank_0_log="""
[0][2025-12-13T12:44:31.387Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:44:31.726Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:44:31.728Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:44:31.728Z][compute][start][send_tensors][compress]
[0][2025-12-13T12:44:31.739Z][compute][end][send_tensors][compress]
[0][2025-12-13T12:44:31.740Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:44:31.740Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:44:32.464Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T12:44:32.465Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T12:44:32.465Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:44:32.467Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:44:32.471Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:44:32.564Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:44:32.564Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T12:44:30.352Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:44:31.834Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T12:44:31.835Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T12:44:31.835Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:44:31.837Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:44:31.841Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:44:31.939Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T12:44:31.939Z][compute][start][send_tensors][compress]
[1][2025-12-13T12:44:31.955Z][compute][end][send_tensors][compress]
[1][2025-12-13T12:44:31.956Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T12:44:30.685Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:44:32.050Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T12:44:32.051Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T12:44:32.051Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:44:32.053Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:44:32.057Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:44:32.157Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T12:44:32.157Z][compute][start][send_tensors][compress]
[2][2025-12-13T12:44:32.166Z][compute][end][send_tensors][compress]
[2][2025-12-13T12:44:32.166Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T12:44:31.020Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:44:32.260Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T12:44:32.261Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T12:44:32.261Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:44:32.263Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:44:32.267Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:44:32.362Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T12:44:32.362Z][compute][start][send_tensors][compress]
[3][2025-12-13T12:44:32.370Z][compute][end][send_tensors][compress]
[3][2025-12-13T12:44:32.371Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""