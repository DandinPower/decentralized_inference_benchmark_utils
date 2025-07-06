# gguf metadata converter

After implementing the flexible GGUF splits loader in [prima.cpp#3](https://github.com/DandinPower/prima.cpp/pull/3), many ranks only require the metadata from the first split to initialize, without loading the full weight tensors. Downloading and storing the entire GGUF blob can be prohibitively large on devices with limited storage.

This converter strips out all tensor data from the first-split file (e.g. `prefix-00001-of-0000X.gguf`), leaving a valid, metadata-only stub. You can then pass this stub to `prima -m` for ranks that don’t require split index 0, reclaiming the storage space previously occupied by the weights.

### How It Works

1. **Memory-map** the input GGUF file in read-only mode (no weight pages are faulted in).
2. **Scan** the header, KV section, and tensor descriptors to find where metadata ends.
3. **Align** the metadata end offset to `general.alignment` (default 32 bytes).
4. **Truncate & overwrite** the original file, writing only the metadata stub.

### Usage

```
# Replace the GGUF file in-place with its metadata-only stub:
./gguf_meta_stub.py path/to/prefix-00001-of-0000X.gguf
```

The script will print the size of the retained metadata and overwrite the original file.