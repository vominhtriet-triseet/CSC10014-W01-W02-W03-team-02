from pathlib import Path

from . import load_tasks

CSV_PATH = Path(__file__).parent / "tasks.csv"

for task in load_tasks(CSV_PATH):
    print(task)