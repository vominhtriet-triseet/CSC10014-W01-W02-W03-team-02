
from datetime import date

import pytest

from shared.contract import Task, Block
from shared.study_planner.allocate import allocate


@pytest.fixture
def tasks():
    return [
        Task("Math", 5, 3.0, date(2026, 10, 30)),
        Task("Python", 4, 2.0, date(2026, 10, 27)),
        Task("English", 3, 2.0, date(2026, 11, 5)),
    ]


def test_allocate_enough_hours(tasks):
    blocks = allocate(tasks, 7.0)

    assert blocks == [
        Block(tasks[0], 3.0),
        Block(tasks[1], 2.0),
        Block(tasks[2], 2.0),
    ]


def test_allocate_limited_hours(tasks):
    blocks = allocate(tasks, 4.0)

    assert blocks == [
        Block(tasks[0], 3.0),
        Block(tasks[1], 1.0),
    ]


def test_allocate_zero_hours(tasks):
    assert allocate(tasks, 0) == []


def test_allocate_empty_tasks():
    assert allocate([], 5.0) == []


def test_allocate_negative_hours(tasks):
    with pytest.raises(ValueError, match="hours cannot be negative"):
        allocate(tasks, -1.0)


def test_allocated_hours_never_exceed_available_hours(tasks):
    blocks = allocate(tasks, 4.5)

    assert sum(block.hours for block in blocks) <= 4.5


def test_block_hours_do_not_exceed_task_effort(tasks):
    blocks = allocate(tasks, 4.5)

    for block in blocks:
        assert 0 < block.hours <= block.task.effort_h
