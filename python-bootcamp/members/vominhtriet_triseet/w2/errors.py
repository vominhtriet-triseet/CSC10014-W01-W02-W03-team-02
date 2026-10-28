from collections.abc import Iterable

from .models import Task


class InfeasiblePlan(Exception):
    """Describe a study plan that exceeds the available hours."""
    def __init__(self, needed_h: float, available_h: float) -> None:
        """Store the required and available study-hour totals."""
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        """Return a readable explanation of the capacity mismatch."""
        return (
            f"plan needs {self.needed_h:g} hours, "
            f"but only {self.available_h:g} hours are available"
        )


def check_feasible(tasks: Iterable[Task], available_h: float) -> None:
    """Raise InfeasiblePlan when task effort exceeds available study time."""
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
