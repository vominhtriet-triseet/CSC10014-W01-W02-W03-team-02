"""Validation helpers for the shared study planner."""

from math import isfinite
from collections.abc import Sequence

from shared.contract import Task


class EmptyTaskFileError(ValueError):
    """Raised when a CSV contains a header but no task rows."""


def validate_plan_request(tasks: Sequence[Task], available_h: float) -> str | None:
    """Validate task inputs and describe a plan that needs more available time."""
    if not isfinite(available_h) or available_h < 0:
        raise ValueError("available hours must be a finite, non-negative number")
    if not tasks:
        raise EmptyTaskFileError("CSV contains no task rows")

    for task in tasks:
        if not task.title.strip():
            raise ValueError("task title cannot be empty")
        if not isfinite(task.effort_h) or task.effort_h < 0:
            raise ValueError(f"task effort must be finite and non-negative: {task.title}")

    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        return (
            f"The tasks need {needed_h:g} hours, but only {available_h:g} "
            "hours are available. Remaining work is listed below."
        )
    return None
