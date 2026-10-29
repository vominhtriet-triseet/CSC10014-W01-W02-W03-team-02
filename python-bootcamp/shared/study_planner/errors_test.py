from datetime import date

import pytest

from shared.contract import Task
from shared.study_planner.errors import EmptyTaskFileError, validate_plan_request


def test_empty_task_list_is_rejected() -> None:
    with pytest.raises(EmptyTaskFileError):
        validate_plan_request([], 2.0)


def test_infeasible_workload_returns_warning() -> None:
    tasks = [Task("Exam", 5, 3.0, date(2026, 10, 30))]

    warning = validate_plan_request(tasks, 2.0)

    assert warning is not None
    assert "need 3 hours" in warning
    assert "only 2 hours" in warning


def test_invalid_available_hours_are_rejected() -> None:
    tasks = [Task("Exam", 5, 3.0, date(2026, 10, 30))]

    with pytest.raises(ValueError, match="finite, non-negative"):
        validate_plan_request(tasks, -1)
