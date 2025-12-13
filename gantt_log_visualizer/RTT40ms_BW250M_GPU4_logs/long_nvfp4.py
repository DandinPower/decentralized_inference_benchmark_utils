rank_0_log="""
[0][2025-12-13T12:41:26.540Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:41:26.865Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:41:26.867Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:41:26.867Z][compute][start][send_tensors][compress]
[0][2025-12-13T12:41:26.882Z][compute][end][send_tensors][compress]
[0][2025-12-13T12:41:26.883Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:41:26.883Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:41:27.630Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T12:41:27.636Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T12:41:27.636Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:41:27.638Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:41:27.642Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:41:27.732Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:41:27.732Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T12:41:25.495Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:41:26.978Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T12:41:26.983Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T12:41:26.983Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:41:26.986Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:41:26.989Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:41:27.089Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T12:41:27.089Z][compute][start][send_tensors][compress]
[1][2025-12-13T12:41:27.103Z][compute][end][send_tensors][compress]
[1][2025-12-13T12:41:27.103Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T12:41:25.835Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:41:27.198Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T12:41:27.203Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T12:41:27.203Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:41:27.206Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:41:27.210Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:41:27.307Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T12:41:27.307Z][compute][start][send_tensors][compress]
[2][2025-12-13T12:41:27.321Z][compute][end][send_tensors][compress]
[2][2025-12-13T12:41:27.321Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T12:41:26.174Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:41:27.416Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T12:41:27.421Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T12:41:27.421Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:41:27.423Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:41:27.427Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:41:27.522Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T12:41:27.522Z][compute][start][send_tensors][compress]
[3][2025-12-13T12:41:27.536Z][compute][end][send_tensors][compress]
[3][2025-12-13T12:41:27.537Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""