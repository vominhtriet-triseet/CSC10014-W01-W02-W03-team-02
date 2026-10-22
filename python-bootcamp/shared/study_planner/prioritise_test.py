from datetime import date

from shared.contract import Task
from shared.study_planner.prioritise import prioritise


def test_prioritise_orders_by_score():
    today = date(2026, 10, 22)

    tasks = [
        Task("DS exam", 5, 6.0, date(2026, 10, 30)),
        Task("Assignment", 4, 1.5, date(2026, 10, 27)),
        Task("Read Python", 2, 2.0, date(2026, 10, 25)),
    ]

    result = prioritise(tasks, today)

    assert [task.title for task in result] == [
        "Assignment",
        "Read Python",
        "DS exam",
    ]


def test_prioritise_empty_list():
    assert prioritise([], date(2026, 10, 22)) == []


def test_prioritise_does_not_modify_input():
    today = date(2026, 10, 22)

    tasks = [
        Task("A", 1, 1.0, date(2026, 10, 30)),
        Task("B", 5, 1.0, date(2026, 10, 25)),
    ]

    original = tasks.copy()

    prioritise(tasks, today)

    assert tasks == original
