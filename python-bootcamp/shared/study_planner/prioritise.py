from datetime import date

from shared.contract import Task


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    return sorted(
        tasks,
        key=lambda task: task.importance
        / (task.deadline - today).days,
        reverse=True,
    )