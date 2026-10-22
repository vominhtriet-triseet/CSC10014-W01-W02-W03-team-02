import csv
import json
from dataclasses import dataclass, asdict
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self):
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        return max(0, (self.deadline - today).days)


def load_tasks(path) -> list[Task]:
    tasks = []

    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        expected = ["title", "importance", "effort_h", "deadline"]
        if reader.fieldnames != expected:
            raise ValueError("Invalid CSV header")

        for line_num, row in enumerate(reader, start=2):
            try:
                if None in row or any(
                    row.get(key) is None or not row[key].strip()
                    for key in expected
                ):
                    raise ValueError("Missing or extra fields")

                task = Task(
                    title=row["title"].strip(),
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"])
                )

                tasks.append(task)

            except (ValueError, TypeError) as e:
                raise ValueError(
                    f"Invalid row at line {line_num}: {e}"
                ) from e

    return tasks


def save_json(tasks, path):
    data = []

    for task in tasks:
        item = asdict(task)
        item["deadline"] = task.deadline.isoformat()
        data.append(item)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)