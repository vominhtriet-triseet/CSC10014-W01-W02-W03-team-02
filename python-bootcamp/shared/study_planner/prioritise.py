"""Order tasks by importance and deadline urgency."""

from datetime import date

from shared.contract import Task


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    """Return tasks from highest to lowest score without changing the input list."""
    return sorted(
        tasks,
        key=lambda task: task.importance / max((task.deadline - today).days, 1),
        reverse=True,
    )
