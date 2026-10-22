
from shared.contract import Task, Block


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    """Phân bổ số giờ học cho các task theo kiểu greedy."""
    if hours < 0:
        raise ValueError("hours cannot be negative")

    blocks: list[Block] = []
    remaining_hours = hours

    for task in tasks:
        if remaining_hours <= 0:
            break

        if task.effort_h <= 0:
            continue

        allocated = min(task.effort_h, remaining_hours)

        blocks.append(Block(task=task, hours=allocated))
        remaining_hours -= allocated

    return blocks
