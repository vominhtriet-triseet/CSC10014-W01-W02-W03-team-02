import json
from datetime import date

import pytest

from members.vominhtriet_triseet.w2 import (
    InfeasiblePlan,
    Task,
    check_feasible,
    load_tasks,
    save_json,
)


def test_task_days_left_never_goes_below_zero() -> None:
    task = Task("Exam", 5, 2.0, date(2026, 10, 30))

    assert task.days_left(date(2026, 10, 27)) == 3
    assert task.days_left(date(2026, 10, 30)) == 0
    assert task.days_left(date(2026, 10, 31)) == 0


def test_task_rejects_importance_outside_range() -> None:
    with pytest.raises(ValueError, match="importance must be between 1 and 5"):
        Task("Exam", 6, 2.0, date(2026, 10, 30))


def test_load_tasks_reads_csv(tmp_path) -> None:
    csv_path = tmp_path / "tasks.csv"
    csv_path.write_text(
        "title,importance,effort_h,deadline\nExam,5,2.5,2026-10-30\n",
        encoding="utf-8",
    )

    tasks = load_tasks(csv_path)

    assert tasks == [Task("Exam", 5, 2.5, date(2026, 10, 30))]


def test_load_tasks_reports_invalid_row_number(tmp_path) -> None:
    csv_path = tmp_path / "tasks.csv"
    csv_path.write_text(
        "title,importance,effort_h,deadline\n"
        "Exam,5,2,2026-10-30\n"
        "Essay,high,1,2026-10-31\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="line 3:"):
        load_tasks(csv_path)


def test_save_json_writes_iso_dates(tmp_path) -> None:
    json_path = tmp_path / "tasks.json"
    tasks = [Task("Exam", 5, 2.5, date(2026, 10, 30))]

    save_json(tasks, json_path)

    data = json.loads(json_path.read_text(encoding="utf-8"))
    assert data[0]["deadline"] == "2026-10-30"
    assert data[0]["effort_h"] == 2.5


def test_check_feasible_allows_exact_capacity() -> None:
    check_feasible([Task("Exam", 5, 2.0, date(2026, 10, 30))], 2.0)


def test_check_feasible_raises_with_hour_totals() -> None:
    tasks = [
        Task("Exam", 5, 2.0, date(2026, 10, 30)),
        Task("Essay", 3, 1.5, date(2026, 10, 31)),
    ]

    with pytest.raises(InfeasiblePlan) as error:
        check_feasible(tasks, 3.0)

    assert error.value.needed_h == 3.5
    assert error.value.available_h == 3.0
    assert "3.5 hours" in str(error.value)
