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


# ---------------------------------------------------------------------------


def scan_meta(mm: mmap.mmap) -> tuple[int, int]:
    """
    Walk the memory‑mapped GGUF and return
        meta_size   – first byte after metadata, padded to alignment
        alignment   – value of KV  "general.alignment"  (or default 32)
    The cursor advances via an integer offset (no reads/copies).
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
        key = mm[off:off + k_len].decode("utf‑8"); off += k_len

        v_type, = struct.unpack_from("<i", mm, off); off += 4

        if v_type == 9:                                 # GGUF_TYPE_ARRAY
            arr_type, = struct.unpack_from("<i", mm, off); off += 4
            n_elem, = struct.unpack_from("<Q", mm, off); off += 8

            if arr_type == 8:                           # array of strings
                for _ in range(n_elem):
                    s_len, = struct.unpack_from("<Q", mm, off); off += 8 + s_len
            else:
                elem_sz = _SCALAR_SIZE[arr_type]
                off += n_elem * elem_sz
        else:                                           # scalar
            if v_type == 8:                             # string
                s_len, = struct.unpack_from("<Q", mm, off); off += 8 + s_len
            else:
                off += _SCALAR_SIZE[v_type]

            # catch alignment KV while bytes are still warm in L1
            if key == "general.alignment":
                alignment, = struct.unpack_from("<I", mm, off - _SCALAR_SIZE[v_type])

    # -- tensor descriptors ----------------------------------------------------
    for _ in range(n_tensors):
        name_len, = struct.unpack_from("<Q", mm, off); off += 8 + name_len
        n_dims, = struct.unpack_from("<I", mm, off); off += 4 + n_dims * 8
        off += 4 + 8                                    # dtype + data‑offset

    meta_end = off
    meta_size = align_up(meta_end, alignment)
    return meta_size, alignment


# ---------------------------------------------------------------------------


def write_meta_only(src: Path, dst: Path) -> None:
    with src.open("rb") as fh:
        # map entire file read‑only – no pages are faulted until touched
        mm = mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ)

        meta_size, alignment = scan_meta(mm)

        # slice is a *view* – copying happens only inside write()
        with dst.open("wb") as fout:
            fout.write(mm[:meta_size])

        mm.close()

    print(f"meta‑only bytes: {meta_size:,d}   alignment: {alignment}   →  {dst}")


# ---------------------------------------------------------------------------


def main() -> None:
    p = argparse.ArgumentParser(description="Generate a metadata‑only GGUF stub "
                                            "using mmap so the weight blob is never read.")
    p.add_argument("input", type=Path, help="path/to/00001-of-000NN.gguf")
    p.add_argument("output", type=Path, help="metadata‑only *.gguf to create")
    args = p.parse_args()

    if args.output.exists():
        p.error(f"{args.output} already exists")

    write_meta_only(args.input, args.output)


if __name__ == "__main__":
    main()