import csv
import json
from collections.abc import Iterable
from datetime import date
from pathlib import Path

from .models import Task

_REQUIRED_COLUMNS = ("title", "importance", "effort_h", "deadline")


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from CSV, reporting malformed data with its line number."""
    tasks = []
    with Path(path).open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None:
            raise ValueError("line 1: missing CSV header")

        missing = [column for column in _REQUIRED_COLUMNS if column not in reader.fieldnames]
        if missing:
            raise ValueError(f"line 1: missing required column(s): {', '.join(missing)}")

        for line_number, row in enumerate(reader, start=2):
            try:
                if None in row:
                    raise ValueError("unexpected extra field")
                title = (row["title"] or "").strip()
                if not title:
                    raise ValueError("title is required")
                tasks.append(
                    Task(
                        title=title,
                        importance=int(row["importance"]),
                        effort_h=float(row["effort_h"]),
                        deadline=date.fromisoformat(row["deadline"]),
                    )
                )
            except (TypeError, ValueError) as error:
                raise ValueError(f"line {line_number}: {error}") from error

    return tasks


def save_json(tasks: Iterable[Task], path: str | Path) -> None:
    """Write tasks as readable JSON with ISO-formatted deadlines."""
    data = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]
    with Path(path).open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")
