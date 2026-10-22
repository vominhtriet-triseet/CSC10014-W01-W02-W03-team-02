import csv
import json
from datetime import date
from pathlib import Path
from typing import Iterable

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Đọc file CSV và trả về danh sách Task. Dòng lỗi sẽ raise ValueError kèm số dòng."""
    tasks: list[Task] = []

    with open(path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        # Dòng 1 là header nên dữ liệu bắt đầu từ dòng 2
        for line_num, row in enumerate(reader, start=2):
            try:
                if row is None or any(
                    row.get(col) is None or str(row.get(col)).strip() == ""
                    for col in ("title", "importance", "effort_h", "deadline")
                ):
                    raise ValueError("Missing required fields")

                title = row["title"].strip()
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = date.fromisoformat(row["deadline"].strip())

                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
                tasks.append(task)
            except (ValueError, KeyError, TypeError) as err:
                raise ValueError(f"Invalid row at line {line_num}: {err}") from err

    return tasks


def save_json(tasks: Iterable[Task], path: str | Path) -> None:
    """Lưu danh sách Task ra file JSON."""
    data = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
