"""Command-line interface for creating a study plan."""

import argparse
import sys
from collections.abc import Sequence
from datetime import date

from members.kq244466666.w2.io_utils import load_tasks
from members.kq244466666.w2.models import Task


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Create a study plan from a CSV task list."
    )
    parser.add_argument("csv_path", help="Path to the tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study time in hours",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Today's date in YYYY-MM-DD format (default: today)",
    )
    return parser


def create_plan(
    tasks: list[Task],
    hours: float,
    today: date,
) -> list[tuple[str, float]]:
    """Allocate available study hours to tasks by priority and deadline."""
    if hours < 0:
        raise ValueError("Hours cannot be negative")

    ordered_tasks = sorted(
        tasks,
        key=lambda task: (
            -(task.importance / max(task.days_left(today), 1)),
            task.deadline,
        ),
    )

    plan: list[tuple[str, float]] = []
    remaining = hours

    for task in ordered_tasks:
        if remaining <= 0:
            break

        allocated = min(task.effort_h, remaining)
        if allocated > 0:
            plan.append((task.title, allocated))
            remaining -= allocated

    return plan


def main(argv: Sequence[str] | None = None) -> int:
    """Run the study planner CLI and return an exit status."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.hours < 0:
        print("Error: --hours cannot be negative.", file=sys.stderr)
        return 1

    try:
        tasks = load_tasks(args.csv_path)
    except FileNotFoundError:
        print(f"Error: CSV file not found: {args.csv_path}", file=sys.stderr)
        return 1
    except (ValueError, OSError) as exc:
        print(f"Error reading CSV file: {exc}", file=sys.stderr)
        return 1

    plan = create_plan(tasks, args.hours, args.today)

    print(f"Tonight ({args.hours:.1f} h):")
    if not plan:
        print("No tasks to schedule.")
        return 0

    for index, (title, allocated) in enumerate(plan, start=1):
        print(f"{index}. {title:<20} {allocated:.1f} h")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
