class InfeasiblePlan(Exception):
    """Kế hoạch không khả thi: tổng giờ cần > số giờ có sẵn."""

    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(needed_h, available_h)

    def __str__(self) -> str:
        return (
            f"Kế hoạch không khả thi: cần {self.needed_h:g}h "
            f"nhưng chỉ có {self.available_h:g}h "
            f"(thiếu {self.needed_h - self.available_h:g}h)"
        )


def check_feasible(tasks, available_h: float) -> None:
    needed = sum(t.effort_h for t in tasks)
    if needed > available_h:
        raise InfeasiblePlan(needed, available_h)