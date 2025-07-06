# gguf-split

A command-line utility from the `llama.cpp` project to split `.gguf` model files into smaller shards, either by tensor count or total size. This supports multi-split loading in distributed setups.

### Release Information

* Source repository: [https://github.com/ggml-org/llama.cpp/tree/master/tools/gguf-split](https://github.com/ggml-org/llama.cpp/tree/master/tools/gguf-split)
* Release tag: `b5734`

### Usage

```bash
cd gguf-split-b5734
./llama-gguf-split --split-max-tensors <N> <input.gguf> <output_prefix>
```

For example:

```bash
./llama-gguf-split --split-max-tensors 38 \
    ../gguf_examples/Llama-3.2-1B-Instruct-Q4_K_M.gguf \
    ../gguf_examples/Llama-3.2-1B-Instruct-Q4_K_M
```

* `--split-max-tensors <N>`: Maximum number of tensors per shard.
* `input.gguf`: Path to the original GGUF model file.
* `output_prefix`: Prefix for the generated split files (they will end with `.gguf`).