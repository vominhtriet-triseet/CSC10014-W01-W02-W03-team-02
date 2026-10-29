import argparse
import sys
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise


def main() -> int:
    """Parse command-line arguments and print a study plan."""
    parser = argparse.ArgumentParser(
        description="Create a study plan from a CSV task list."
    )
    parser.add_argument(
        "csv_file",
        type=Path,
        help="Path to the tasks CSV file",
    )
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study time in hours",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        help="Today's date in YYYY-MM-DD format",
    )

    args = parser.parse_args()
    today = args.today or date.today()

    if args.hours < 0:
        print("Error: --hours cannot be negative.", file=sys.stderr)
        return 1

    if not args.csv_file.is_file():
        print(
            f"Error: CSV file not found: {args.csv_file}",
            file=sys.stderr,
        )
        return 1

    try:
        tasks = parse_csv(args.csv_file)
        ordered_tasks = prioritise(tasks, today)
        blocks = allocate(ordered_tasks, args.hours)
    except (OSError, ValueError, ZeroDivisionError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Tonight ({args.hours:.1f} h):")
    if not blocks:
        print("No tasks to study.")
        return 0

    for index, block in enumerate(blocks, start=1):
        prefix = f"{index}. {block.task.title}"
        dots = "." * max(3, 22 - len(prefix))
        print(f"{prefix} {dots} {block.hours:.1f} h")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
