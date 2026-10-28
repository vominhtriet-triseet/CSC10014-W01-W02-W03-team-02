"""Run the Week 3 study-planner command-line exercise."""

import argparse
import sys
from datetime import date
from math import isfinite
from pathlib import Path

from members.vominhtriet_triseet.w2 import load_tasks
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise


def _parse_date(value: str) -> date:
    """Parse a command-line date in YYYY-MM-DD format."""
    try:
        parsed = date.fromisoformat(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("date must be YYYY-MM-DD") from error
    if parsed.isoformat() != value:
        raise argparse.ArgumentTypeError("date must be YYYY-MM-DD")
    return parsed


def main(argv: list[str] | None = None) -> int:
    """Parse arguments, reuse the Week 2 task loader, and print a study plan."""
    parser = argparse.ArgumentParser(description="Create a study plan from a task CSV.")
    parser.add_argument("csv_path", type=Path, help="task CSV path")
    parser.add_argument("--hours", type=float, required=True, help="available study hours")
    parser.add_argument("--today", type=_parse_date, help="reference date (YYYY-MM-DD)")
    args = parser.parse_args(argv)

    try:
        if not isfinite(args.hours) or args.hours < 0:
            raise ValueError("available hours must be a finite, non-negative number")
        tasks = load_tasks(args.csv_path)
        if not tasks:
            raise ValueError("CSV contains no task rows")
        today = args.today or date.today()
        ordered = prioritise(tasks, today)
        blocks = allocate(ordered, args.hours)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Tonight ({args.hours:.1f} h):")
    if not blocks:
        print("  No tasks fit in the available time.")
    for index, block in enumerate(blocks, start=1):
        print(f"  {index}. {block.task.title} ...... {block.hours:g} h")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
