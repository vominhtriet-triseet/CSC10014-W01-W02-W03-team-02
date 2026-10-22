from typing import Iterable

from .models import Task


class InfeasiblePlan(Exception):
    """Ngoại lệ được quăng ra khi tổng thời gian cần thiết lớn hơn thời gian hiện có."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        return (
            f"Infeasible plan: need {self.needed_h} hours, "
            f"but only {self.available_h} hours available."
        )


def check_feasible(tasks: Iterable[Task], available_h: float) -> bool:
    """Kiểm tra kế hoạch có khả thi không. Quăng InfeasiblePlan nếu không đủ giờ."""
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h=needed_h, available_h=available_h)
    return True
