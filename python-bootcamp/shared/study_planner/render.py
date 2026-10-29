"""Render allocated study blocks as readable text."""

from collections.abc import Sequence

from shared.contract import Block, Task


def render(
    blocks: Sequence[Block],
    tasks: Sequence[Task] = (),
    warning: str | None = None,
) -> str:
    """Return a schedule and any work that did not fit in the available time."""
    if not blocks and not tasks and warning is None:
        return "Study Plan\n=========="

    task_list = list(tasks) if tasks else [block.task for block in blocks]
    allocated: dict[int, float] = {}
    for block in blocks:
        key = id(block.task)
        allocated[key] = allocated.get(key, 0.0) + block.hours

    lines = ["Study Plan", "==========", "", "Scheduled"]
    if not blocks:
        lines.append("- None")
    else:
        for block in blocks:
            lines.append(f"- {block.task.title}: {block.hours:g} h")

    remaining = [
        (task, max(0.0, task.effort_h - allocated.get(id(task), 0.0)))
        for task in task_list
        if task.effort_h - allocated.get(id(task), 0.0) > 1e-9
    ]
    if remaining:
        lines.extend(["", "Unscheduled / remaining work"])
        for task, hours in remaining:
            lines.append(f"- {task.title}: {hours:g} h")

    if warning:
        lines.extend(["", f"Note: {warning}"])

    return "\n".join(lines)
