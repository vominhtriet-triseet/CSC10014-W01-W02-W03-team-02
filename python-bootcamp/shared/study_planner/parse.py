import csv
from datetime import date
from pathlib import Path

from shared.contract import Task


def parse_csv(path: str | Path) -> list[Task]:
    tasks = []

    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        required = {"title", "importance", "effort_h", "deadline"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("CSV is missing required columns")

        for line, row in enumerate(reader, start=2):
            try:
                task = Task(
                    title=row["title"].strip(),
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
                tasks.append(task)

            except (ValueError, TypeError, KeyError) as error:
                raise ValueError(f"Invalid data on line {line}: {error}") from error

    return tasks
