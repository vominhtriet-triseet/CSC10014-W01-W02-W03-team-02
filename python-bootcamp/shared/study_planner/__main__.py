"""Run the shared study planner from a task CSV."""

import argparse
from datetime import date
from pathlib import Path
import sys

from shared.study_planner.allocate import allocate
from shared.study_planner.errors import validate_plan_request
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build a study plan from a task CSV.")
    parser.add_argument("csv_path", type=Path, help="CSV with title, importance, effort_h, deadline")
    parser.add_argument("--hours", type=float, default=2.0, help="available study hours (default: 2)")
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="reference date in YYYY-MM-DD format (default: today)",
    )
    args = parser.parse_args(argv)

    try:
        tasks = parse_csv(args.csv_path)
        warning = validate_plan_request(tasks, args.hours)
        ordered = prioritise(tasks, args.today)
        blocks = allocate(ordered, args.hours)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(render(blocks, tasks=ordered, warning=warning))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
