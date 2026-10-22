import csv
import json
from dataclasses import asdict
from datetime import date

from .models import Task

EXPECTED_HEADER = ["title", "importance", "effort_h", "deadline"]


def load_tasks(path) -> list[Task]:
    tasks: list[Task] = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != EXPECTED_HEADER:
            raise ValueError(f"line 1: header phải là {','.join(EXPECTED_HEADER)}")
        for row in reader:
            line = reader.line_num  # số dòng thật trong file
            if None in row or None in row.values():
                raise ValueError(f"line {line}: sai số cột")
            try:
                title = row["title"].strip()
                if not title:
                    raise ValueError("title rỗng")
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = date.fromisoformat(row["deadline"].strip())
                if effort_h < 0:
                    raise ValueError("effort_h âm")
            except ValueError as e:
                raise ValueError(f"line {line}: {e}") from e
            tasks.append(Task(title, importance, effort_h, deadline))
    return tasks


def save_json(tasks: list[Task], path) -> None:
    data = [{**asdict(t), "deadline": t.deadline.isoformat()} for t in tasks]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)