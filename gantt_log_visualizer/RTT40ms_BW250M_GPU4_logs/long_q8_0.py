rank_0_log="""
[0][2025-12-13T12:10:29.309Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:10:29.645Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:10:29.647Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:10:29.647Z][compute][start][send_tensors][compress]
[0][2025-12-13T12:10:29.651Z][compute][end][send_tensors][compress]
[0][2025-12-13T12:10:29.654Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:10:29.654Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:10:30.736Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T12:10:30.737Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T12:10:30.737Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:10:30.739Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:10:30.743Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:10:30.833Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:10:30.833Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T12:10:28.061Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:10:29.856Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T12:10:29.856Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T12:10:29.856Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:10:29.859Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:10:29.862Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:10:29.962Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T12:10:29.962Z][compute][start][send_tensors][compress]
[1][2025-12-13T12:10:29.966Z][compute][end][send_tensors][compress]
[1][2025-12-13T12:10:29.969Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T12:10:28.471Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:10:30.143Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T12:10:30.144Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T12:10:30.144Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:10:30.147Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:10:30.150Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:10:30.248Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T12:10:30.248Z][compute][start][send_tensors][compress]
[2][2025-12-13T12:10:30.252Z][compute][end][send_tensors][compress]
[2][2025-12-13T12:10:30.254Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T12:10:28.876Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:10:30.455Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T12:10:30.455Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T12:10:30.455Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:10:30.457Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:10:30.461Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:10:30.556Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T12:10:30.556Z][compute][start][send_tensors][compress]
[3][2025-12-13T12:10:30.560Z][compute][end][send_tensors][compress]
[3][2025-12-13T12:10:30.562Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""