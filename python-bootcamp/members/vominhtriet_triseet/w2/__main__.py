from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    samples = Path(__file__).resolve().parents[3] / "samples"
    tasks = load_tasks(samples / "tasks.csv")
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(
            f"{task.title}: importance {task.importance}, "
            f"{task.effort_h:g} h, deadline {task.deadline.isoformat()}"
        )


if __name__ == "__main__":
    main()
