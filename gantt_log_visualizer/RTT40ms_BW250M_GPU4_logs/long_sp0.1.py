rank_0_log="""
[0][2025-12-13T13:15:40.459Z][compute][start][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:15:40.761Z][compute][end][input_embedding][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:15:40.763Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T13:15:40.763Z][compute][start][send_tensors][compress]
[0][2025-12-13T13:15:41.047Z][compute][end][send_tensors][compress]
[0][2025-12-13T13:15:41.049Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[0][2025-12-13T13:15:41.049Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T13:15:42.813Z][compute][start][recv_tensors][decompress]
[0][2025-12-13T13:15:42.817Z][compute][end][recv_tensors][decompress]
[0][2025-12-13T13:15:42.817Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[0][2025-12-13T13:15:42.819Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:15:42.823Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:15:42.916Z][compute][start][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
[0][2025-12-13T13:15:42.916Z][compute][end][output_linear][sbatch_tokens: 526, ubatch_tokens: 512]
"""

rank_1_log="""
[1][2025-12-13T13:15:38.710Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T13:15:41.149Z][compute][start][recv_tensors][decompress]
[1][2025-12-13T13:15:41.153Z][compute][end][recv_tensors][decompress]
[1][2025-12-13T13:15:41.153Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[1][2025-12-13T13:15:41.155Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T13:15:41.159Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[1][2025-12-13T13:15:41.261Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[1][2025-12-13T13:15:41.261Z][compute][start][send_tensors][compress]
[1][2025-12-13T13:15:41.608Z][compute][end][send_tensors][compress]
[1][2025-12-13T13:15:41.609Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_2_log="""
[2][2025-12-13T13:15:39.403Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T13:15:41.708Z][compute][start][recv_tensors][decompress]
[2][2025-12-13T13:15:41.711Z][compute][end][recv_tensors][decompress]
[2][2025-12-13T13:15:41.711Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[2][2025-12-13T13:15:41.713Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T13:15:41.717Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[2][2025-12-13T13:15:41.816Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[2][2025-12-13T13:15:41.816Z][compute][start][send_tensors][compress]
[2][2025-12-13T13:15:42.163Z][compute][end][send_tensors][compress]
[2][2025-12-13T13:15:42.163Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""

rank_3_log="""
[3][2025-12-13T13:15:40.076Z][comm][start][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T13:15:42.262Z][compute][start][recv_tensors][decompress]
[3][2025-12-13T13:15:42.265Z][compute][end][recv_tensors][decompress]
[3][2025-12-13T13:15:42.265Z][comm][end][recv_tensors][sbatch_tokens: 526, ubatch_tokens: 512, receive data from other nodes]
[3][2025-12-13T13:15:42.267Z][compute][start][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T13:15:42.271Z][compute][end][transformer_blocks][sbatch_tokens: 526, ubatch_tokens: 512]
[3][2025-12-13T13:15:42.369Z][comm][start][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
[3][2025-12-13T13:15:42.369Z][compute][start][send_tensors][compress]
[3][2025-12-13T13:15:42.713Z][compute][end][send_tensors][compress]
[3][2025-12-13T13:15:42.714Z][comm][end][send_tensors][sbatch_tokens: 526, ubatch_tokens: 512, send the result to the next node or the master]
"""