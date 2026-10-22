from datetime import date

import pytest

from shared.contract import Task
from shared.study_planner.parse import parse_csv


def test_parse_valid_csv(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n"
        "Math homework,5,2.5,2026-10-30\n"
        "English essay,3,1.5,2026-11-02\n",
        encoding="utf-8",
    )

    assert parse_csv(path) == [
        Task("Math homework", 5, 2.5, date(2026, 10, 30)),
        Task("English essay", 3, 1.5, date(2026, 11, 2)),
    ]


def test_parse_empty_csv(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n",
        encoding="utf-8",
    )

    assert parse_csv(path) == []


def test_parse_invalid_importance(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n"
        "Math homework,6,2.5,2026-10-30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        parse_csv(path)


def test_parse_invalid_date(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n"
        "Math homework,5,2.5,30/10/2026\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        parse_csv(path)


def test_parse_missing_column(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,deadline\n"
        "Math homework,5,2026-10-30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        parse_csv(path)
