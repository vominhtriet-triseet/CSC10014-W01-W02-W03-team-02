from datetime import date
from pathlib import Path
import subprocess
import sys

import pytest

from shared.contract import Task
from shared.study_planner.allocate import allocate
from shared.study_planner.errors import EmptyTaskFileError, validate_plan_request
from shared.study_planner.render import render

BOOTCAMP = Path(__file__).resolve().parents[1]


def test_empty_task_rows_are_rejected() -> None:
    with pytest.raises(EmptyTaskFileError, match="no task rows"):
        validate_plan_request([], 2.0)


def test_infeasible_workload_is_reported_and_partial_plan_is_kept() -> None:
    tasks = [
        Task("Assignment", 4, 1.5, date(2026, 10, 27)),
        Task("DS exam", 5, 6.0, date(2026, 10, 30)),
    ]

    warning = validate_plan_request(tasks, 2.0)
    blocks = allocate(tasks, 2.0)
    output = render(blocks, tasks=tasks, warning=warning)

    assert sum(block.hours for block in blocks) == 2.0
    assert "DS exam" in output
    assert "5.5 h" in output
    assert "only 2 hours are available" in output


def test_cli_reports_missing_csv_without_traceback() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "shared.study_planner",
            "samples/does-not-exist.csv",
            "--hours",
            "2",
        ],
        cwd=BOOTCAMP,
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )

    assert result.returncode == 1
    assert "Error:" in result.stderr
    assert "Traceback" not in result.stderr


def test_cli_reports_header_only_csv_without_traceback(tmp_path: Path) -> None:
    csv_path = tmp_path / "empty.csv"
    csv_path.write_text("title,importance,effort_h,deadline\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "shared.study_planner",
            str(csv_path),
            "--hours",
            "2",
        ],
        cwd=BOOTCAMP,
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )

    assert result.returncode == 1
    assert "CSV contains no task rows" in result.stderr
    assert "Traceback" not in result.stderr
