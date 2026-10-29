import argparse
import sys
from datetime import date
from pathlib import Path

from members.NPTho510.w2.io_utils import load_tasks
from members.NPT510.w2.models import Task


def parse_today(text: str) -> date:
    """Convert a YYYY-MM-DD string into a date."""
    try:
        return date.fromisoformat(text)
    except ValueError as error:
        raise argparse.ArgumentTypeError(
            f"Invalid date: {text}. Use YYYY-MM-DD."
        ) from error


def make_plan(
    tasks: list[Task],
    hours: float,
    today: date,
) -> list[tuple[str, float]]:
    """Allocate study hours to tasks by importance and deadline."""
    ordered = sorted(
        tasks,
        key=lambda task: (
            -task.importance,
            task.days_left(today),
        ),
    )

    remaining = hours
    plan: list[tuple[str, float]] = []

    for task in ordered:
        if remaining <= 0:
            break

        if task.effort_h <= 0:
            continue

        allocated = min(task.effort_h, remaining)
        plan.append((task.title, allocated))
        remaining -= allocated

    return plan


def main(argv: list[str] | None = None) -> int:
    """Parse arguments and print tonight's study plan."""
    parser = argparse.ArgumentParser(
        description="Create a study plan from a CSV file."
    )

    parser.add_argument(
        "filename",
        type=Path,
        help="Path to the CSV file",
    )

    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study hours",
    )

    parser.add_argument(
        "--today",
        type=parse_today,
        default=None,
        help="Reference date (YYYY-MM-DD)",
    )

    args = parser.parse_args(argv)

    if not args.filename.is_file():
        print(
            f"Error: file not found: {args.filename}",
            file=sys.stderr,
        )
        return 1

    if not 0 < args.hours < float("inf"):
        print(
            "Error: --hours must be a finite positive number.",
            file=sys.stderr,
        )
        return 1

    today = args.today if args.today is not None else date.today()

    try:
        tasks = load_tasks(args.filename)
        plan = make_plan(tasks, args.hours, today)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Tonight ({args.hours:.1f} h):")

    for index, (title, allocated) in enumerate(plan, start=1):
        print(f" {index}. {title:.<16} {allocated:.1f} h")

    return 0


if __name__ == "__main__":
    sys.exit(main())