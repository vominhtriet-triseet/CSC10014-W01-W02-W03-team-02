
import argparse
import sys
from datetime import date
from pathlib import Path

from ..w2.io_utils import load_tasks


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Plan which tasks to work on tonight."
    )
    parser.add_argument("csv_file", help="Path to the tasks CSV file")
    parser.add_argument("--hours", type=float, required=True)
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Today's date in YYYY-MM-DD format",
    )

    args = parser.parse_args()
    csv_path = Path(args.csv_file)

    if not csv_path.is_file():
        print(f"Error: file not found: {csv_path}", file=sys.stderr)
        return 1

    if args.hours < 0:
        print("Error: --hours must be non-negative.", file=sys.stderr)
        return 1

    try:
        tasks = load_tasks(csv_path)
    except (OSError, ValueError) as exc:
        print(f"Error loading tasks: {exc}", file=sys.stderr)
        return 1

    eligible_tasks = [
        task for task in tasks
        if task.deadline >= args.today
    ]

    eligible_tasks.sort(
        key=lambda task: (task.deadline, -task.importance)
    )

    selected_tasks = []
    remaining_hours = args.hours

    for task in eligible_tasks:
        if task.effort_h <= remaining_hours:
            selected_tasks.append(task)
            remaining_hours -= task.effort_h

    print(f"Tonight ({args.hours:.1f} h):")

    if not selected_tasks:
        print("No tasks selected.")
    else:
        for index, task in enumerate(selected_tasks, start=1):
            print(
                f"{index:2}. {task.title} ...... "
                f"{task.effort_h:.1f} h"
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
