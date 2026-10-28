from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represent a study task with its priority, effort, and deadline."""
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate that the task importance is in the required 1–5 range."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be between 1 and 5")

    def days_left(self, today: date) -> int:
        """Return the non-negative number of days until the deadline."""
        return max(0, (self.deadline - today).days)
