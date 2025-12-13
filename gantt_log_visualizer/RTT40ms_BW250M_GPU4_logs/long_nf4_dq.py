rank_0_log="""
[0][2025-12-13T12:50:24.013Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:50:24.326Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:50:24.328Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:50:24.328Z][compute][start][send_tensors][compress]
[0][2025-12-13T12:50:24.338Z][compute][end][send_tensors][compress]
[0][2025-12-13T12:50:24.339Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:50:24.339Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:50:25.045Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T12:50:25.046Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T12:50:25.046Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:50:25.048Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:50:25.052Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:50:25.142Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:50:25.142Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T12:50:23.007Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:50:24.427Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T12:50:24.428Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T12:50:24.428Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:50:24.430Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:50:24.434Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:50:24.535Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T12:50:24.535Z][compute][start][send_tensors][compress]
[1][2025-12-13T12:50:24.557Z][compute][end][send_tensors][compress]
[1][2025-12-13T12:50:24.557Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T12:50:23.335Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:50:24.645Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T12:50:24.646Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T12:50:24.646Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:50:24.649Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:50:24.652Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:50:24.751Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T12:50:24.751Z][compute][start][send_tensors][compress]
[2][2025-12-13T12:50:24.760Z][compute][end][send_tensors][compress]
[2][2025-12-13T12:50:24.760Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T12:50:23.668Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:50:24.848Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T12:50:24.848Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T12:50:24.848Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:50:24.851Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:50:24.854Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:50:24.949Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T12:50:24.949Z][compute][start][send_tensors][compress]
[3][2025-12-13T12:50:24.957Z][compute][end][send_tensors][compress]
[3][2025-12-13T12:50:24.958Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""