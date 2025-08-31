# Decentralized Inference Benchmark and Utility Collection

This repository contains a comprehensive suite of tools designed for benchmarking, configuring, and managing multi-node deployments of `prima.cpp` and `petals`. These utilities streamline the process of setting up and evaluating distributed large language model inference.

## Tools Included

This collection provides the following utilities:

* **[Activation Visualizer](./activation_visualizer/README.md)**: A tool to visualize neural network activation tensors as 3D heatmaps from binary tensor files.
* **[Gantt Log Visualizer](./gantt_log_visualizer/README.md)**: A tool to visualize multi-rank logs as an interactive Gantt chart.
* **[GGUF Split](./gguf-split-b5734/README.md)**: A utility to split GGUF model files into smaller, manageable shards.
* **[GGUF Metadata Converter](./gguf_metadata_converter/README.md)**: A script to strip tensor data from GGUF files, leaving only the metadata.
* **[LLM Evaluation](./llm_evaluation/README.md)**: A concurrent MMLU-Pro evaluation script for benchmarking Large Language Models with OpenAI-compatible APIs.
* **[Delay RTT and Rate](./delay_rtt_rate/README.md)**: A shell script to simulate network latency and limited bandwidth for testing distributed setups.
* **[Prima.cpp Commands Generator](./primacpp_cmds_generator/README.md)**: A Python script to automate the generation of `llama-cli` and `llama-server` commands.
* **[Prima.cpp Server Benchmark](./primacpp_server_benchmark/README.md)**: A tool for benchmarking the performance of a `prima.cpp` server.
* **[Client Inference Code for Petals Swarm](./petals_client_for_benchmark/README.md)**: A Python client to run inference on a Petals swarm and benchmark key metrics like Time to First Token (TTFT) and throughput.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.