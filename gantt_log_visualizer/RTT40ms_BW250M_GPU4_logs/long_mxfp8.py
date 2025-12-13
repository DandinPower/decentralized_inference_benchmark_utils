rank_0_log="""
[0][2025-12-13T12:35:46.040Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:35:46.336Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:35:46.338Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:35:46.338Z][compute][start][send_tensors][compress]
[0][2025-12-13T12:35:46.345Z][compute][end][send_tensors][compress]
[0][2025-12-13T12:35:46.347Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T12:35:46.347Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:35:47.412Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T12:35:47.416Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T12:35:47.416Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T12:35:47.418Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:35:47.422Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:35:47.512Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T12:35:47.512Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T12:35:44.797Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:35:46.531Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T12:35:46.535Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T12:35:46.535Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T12:35:46.538Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:35:46.541Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T12:35:46.639Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T12:35:46.639Z][compute][start][send_tensors][compress]
[1][2025-12-13T12:35:46.645Z][compute][end][send_tensors][compress]
[1][2025-12-13T12:35:46.648Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T12:35:45.214Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:35:46.832Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T12:35:46.836Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T12:35:46.836Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T12:35:46.839Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:35:46.843Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T12:35:46.939Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T12:35:46.939Z][compute][start][send_tensors][compress]
[2][2025-12-13T12:35:46.947Z][compute][end][send_tensors][compress]
[2][2025-12-13T12:35:46.949Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T12:35:45.615Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:35:47.137Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T12:35:47.141Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T12:35:47.141Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T12:35:47.143Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:35:47.147Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T12:35:47.242Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T12:35:47.242Z][compute][start][send_tensors][compress]
[3][2025-12-13T12:35:47.248Z][compute][end][send_tensors][compress]
[3][2025-12-13T12:35:47.250Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""