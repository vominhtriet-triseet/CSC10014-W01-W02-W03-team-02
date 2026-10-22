from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def days_left(self, today: date) -> int:
        """Số ngày còn lại đến deadline (không bao giờ nhỏ hơn 0)."""
        return max(0, (self.deadline - today).days)