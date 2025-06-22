#!/usr/bin/env python3
import argparse
import mmap
import struct
from pathlib import Path

MAGIC = b"GGUF"
DEFAULT_ALIGNMENT = 32

# scalar byte widths (strings handled separately)
_SCALAR_SIZE = {
    0: 1, 1: 1,                # UINT8 / INT8
    2: 2, 3: 2,                # UINT16 / INT16
    4: 4, 5: 4, 6: 4,          # UINT32 / INT32 / FLOAT32
    7: 1,                      # BOOL  (stored as int8)
    10: 8, 11: 8, 12: 8,       # UINT64 / INT64 / FLOAT64
}


def align_up(x: int, a: int) -> int:
    return (x + a - 1) & ~(a - 1)


def scan_meta(mm: mmap.mmap) -> tuple[int, int]:
    """
    Walk the memory-mapped GGUF and return
        meta_size   – first byte after metadata, padded to alignment
        alignment   – value of KV "general.alignment" (or default 32)
    """
    off = 0

    # -- header ----------------------------------------------------------------
    if mm[off:off + 4] != MAGIC:
        raise ValueError("bad GGUF magic")
    off += 4

    version, = struct.unpack_from("<I", mm, off); off += 4
    n_tensors, = struct.unpack_from("<q", mm, off); off += 8
    n_kv, = struct.unpack_from("<q", mm, off); off += 8

    alignment = DEFAULT_ALIGNMENT

    # -- KV section ------------------------------------------------------------
    for _ in range(n_kv):
        k_len, = struct.unpack_from("<Q", mm, off); off += 8
        key = mm[off:off + k_len].decode("utf-8"); off += k_len

        v_type, = struct.unpack_from("<i", mm, off); off += 4

        if v_type == 9:  # GGUF_TYPE_ARRAY
            arr_type, = struct.unpack_from("<i", mm, off); off += 4
            n_elem, = struct.unpack_from("<Q", mm, off); off += 8

            if arr_type == 8:  # array of strings
                for _ in range(n_elem):
                    s_len, = struct.unpack_from("<Q", mm, off); off += 8 + s_len
            else:
                elem_sz = _SCALAR_SIZE[arr_type]
                off += n_elem * elem_sz
        else:  # scalar
            if v_type == 8:  # string
                s_len, = struct.unpack_from("<Q", mm, off); off += 8 + s_len
            else:
                off += _SCALAR_SIZE[v_type]

            if key == "general.alignment":
                # rewind back to the start of this value and re-read it as an unsigned int
                alignment, = struct.unpack_from("<I", mm, off - _SCALAR_SIZE[v_type])

    # -- tensor descriptors ----------------------------------------------------
    for _ in range(n_tensors):
        name_len, = struct.unpack_from("<Q", mm, off); off += 8 + name_len
        n_dims, = struct.unpack_from("<I", mm, off); off += 4 + n_dims * 8
        off += 4 + 8  # dtype + data-offset

    meta_end = off
    meta_size = align_up(meta_end, alignment)
    return meta_size, alignment


def write_meta_only_inplace(src: Path) -> None:
    # 1) mmap the file read-only, scan metadata, and slice out the stub
    with src.open("rb") as fh:
        mm = mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ)
        meta_size, alignment = scan_meta(mm)
        meta_bytes = mm[:meta_size]
        mm.close()

    # 2) truncate & overwrite the original file with only the metadata stub
    with src.open("wb") as fout:
        fout.write(meta_bytes)

    print(f"Replaced {src} with metadata-only stub ({meta_size:,d} bytes, alignment={alignment})")


def main() -> None:
    p = argparse.ArgumentParser(
        description="Replace a GGUF file in-place with a metadata-only stub."
    )
    p.add_argument(
        "input",
        type=Path,
        help="path/to/00001-of-000NN.gguf (will be overwritten)",
    )
    args = p.parse_args()

    if not args.input.exists():
        p.error(f"{args.input} does not exist")

    write_meta_only_inplace(args.input)


if __name__ == "__main__":
    main()