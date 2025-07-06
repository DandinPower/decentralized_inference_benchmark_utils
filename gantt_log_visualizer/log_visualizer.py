import logging
import re
import sys
from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Iterable

import pandas as pd
import plotly.express as px

LOG_RE = re.compile(
    r"""\[
        (?P<rank>\d+)]\[
        (?P<ts>[^\]]+)]\[
        (?P<op_type>[^\]]+)]\[
        (?P<phase>start|end)]\[
        (?P<op>[^\]]+)]\[
        (?P<rest>.*)]$""",
    re.VERBOSE,
)

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)


def parse_line(raw: str, source: str, line_no: int) -> dict | None:
    match = LOG_RE.match(raw.rstrip("\n"))
    if not match:
        msg = f"{source}:{line_no} malformed line or missing [RANK]"
        logging.warning(msg)
        return None
    rec = match.groupdict()
    rec["source"] = source
    return rec


def parse_file(rows: list[dict], path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as fh:
        for idx, raw in enumerate(fh, 1):
            rec = parse_line(raw, path.name, idx)
            if rec:
                rows.append(rec)
    return rows


def gather_paths(items: Iterable[str | Path]) -> list[Path]:
    files: list[Path] = []
    for item in items:
        p = Path(item)
        if p.is_dir():
            files.extend(sorted(p.rglob("*.log")))
        else:
            files.append(p)
    return files


def load_logs(logs: list[str | Path], offsets: list[str]) -> pd.DataFrame:
    files = gather_paths(logs)
    if not files:
        raise SystemExit("No .log files found")

    logging.info("Scanning %d log files", len(files))

    rows: list[dict] = []
    for file in files:
        parse_file(rows, file)
    if not rows:
        raise SystemExit("No valid log lines collected")

    df = pd.DataFrame(rows)
    df["rank"] = df["rank"].astype(int)
    df["timestamp"] = pd.to_datetime(df["ts"], utc=True, errors="raise")

    # When multiple identical timestamps appear consecutively,
    # we increment each subsequent one by 1 ms to avoid overlap in Gantt chart visualization.
    ts = df["timestamp"]
    new_block = ~(ts.diff() == pd.Timedelta(0))
    block_id = new_block.cumsum()

    def adjust_ts(group_ts: pd.Series) -> pd.Series:
        n = len(group_ts)
        if n <= 1:
            return group_ts
        offsets = pd.to_timedelta(range(n), unit="ms")
        return group_ts + offsets
    df["timestamp"] = df.groupby(block_id)["timestamp"].transform(adjust_ts)

    offsets_dict = {index: pd.to_timedelta(
        offset_string) for index, offset_string in enumerate(offsets)}

    def apply_rank_offset(row):
        return row["timestamp"] + offsets_dict.get(row["rank"], pd.Timedelta(0))

    df["timestamp"] = df.apply(apply_rank_offset, axis=1)

    logging.info("Parsed %d lines across %d ranks",
                 len(df), df["rank"].nunique())
    return df[["rank", "timestamp", "op_type", "phase", "op", "rest", "source"]]


def build_events(df: pd.DataFrame) -> pd.DataFrame:
    active: dict[tuple[int, str], pd.Series] = {}
    completed: list[dict] = []

    for row in df.itertuples(index=False):
        key = (row.rank, row.op_type, row.op)
        if row.phase == "start":
            if key in active:
                raise RuntimeError(
                    f"Double start without end: rank={row.rank} op_type={row.op_type} op={row.op}")
            active[key] = row
        else:  # end
            if key not in active:
                raise RuntimeError(
                    f"end without start: rank={row.rank} op_type={row.op_type} op={row.op}")
            start_row = active.pop(key)
            completed.append({
                "rank": row.rank,
                "op_type": row.op_type,
                "op": row.op,
                "start": start_row.timestamp,
                "end": row.timestamp,
                "duration_ms": (row.timestamp -
                                start_row.timestamp).total_seconds() * 1000,
                "extra": start_row.rest,
                "source_start": start_row.source,
                "source_end": row.source,
            })

    if active:
        orphans = ", ".join(
            f"(rank={k[0]}, op_type={k[1]}, op={k[2]})" for k in active.keys())
        raise RuntimeError(f"Unclosed START events: {orphans}")

    events = pd.DataFrame(completed)
    logging.info("Built %d completed events", len(events))
    return events


def gantt(events: pd.DataFrame, outfile: Path) -> None:
    fig = px.timeline(
        events,
        x_start="start",
        x_end="end",
        y="rank",
        color="op_type",
        hover_data={
            "duration_ms": ":.1f",
            "op": True,
            "extra": True,
            "source_start": True,
            "source_end": True,
        },
        title="Operation timeline per rank",
    )
    fig.update_yaxes(autorange="reversed")
    ranks = sorted(events["rank"].unique())
    fig.update_yaxes(tickmode="array",
                     tickvals=ranks,
                     ticktext=[str(r) for r in ranks])

    fig.update_layout(
        height=max(500, len(events["rank"].unique()) * 40),
        legend_title_text="Operation Type",
    )
    fig.write_html(outfile, include_plotlyjs="cdn")
    logging.info("Wrote %s", outfile)


def main(args: Namespace) -> None:
    try:
        assert len(args.rank_logs) == len(
            args.rank_offsets), f"Each rank should have corresponding offset, if don't have offset, just set 0s"
        raw = load_logs(args.rank_logs, args.rank_offsets)
        events = build_events(raw)
        gantt(events, args.out)
    except (ValueError, RuntimeError) as exc:
        logging.error(str(exc))
        sys.exit(1)


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Visualize multi‑rank application logs as an interactive timeline."
    )
    parser.add_argument(
        "--rank-logs",
        nargs="+",
        required=True,
        help=(
            "Log files for each rank, or directories containing all rank logs (searched recursively for *.log). "
            "The number of log files provided should match the number of ranks, and each file should correspond to a single rank to prevent ordering issues."
        )
    )
    parser.add_argument(
        "--rank-offsets",
        nargs="+",
        required=True,
        help="Time offsets for each rank. This argument is required, and the number of offsets must equal the number of ranks. Example format: \"0s 0s 1ms\"."
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("timeline.html"),
        help="Output HTML file (default: timeline.html).",
    )
    args = parser.parse_args()
    main(args)
