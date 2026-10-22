
import pytest

from members.vominhtriet_triseet.w1.grades import summary
from members.vominhtriet_triseet.w1.rules import (
    can_register_thesis,
    missing,
)
from members.vominhtriet_triseet.w1.text_tools import (
    word_count,
    top_k,
)
from members.vominhtriet_triseet.w1.timetable import by_day


# ---------- grades.py ----------

def test_summary_normal_scores():
    result = summary([7, 8, 9, 10])

    assert result == {
        "min": 7,
        "max": 10,
        "mean": 8.5,
        "median": 8.5,
    }


def test_summary_empty_scores():
    # Edge case: empty list
    with pytest.raises(ValueError, match="no values provided"):
        summary([])


def test_summary_single_score():
    # Edge case: only one score
    assert summary([8.5]) == {
        "min": 8.5,
        "max": 8.5,
        "mean": 8.5,
        "median": 8.5,
    }


# ---------- rules.py ----------

def test_can_register_thesis_at_minimum_requirements():
    # Edge case: exactly meets both thresholds
    assert can_register_thesis(120, 2.0) is True


def test_can_register_thesis_below_credit_requirement():
    assert can_register_thesis(119, 3.5) is False


def test_missing_both_requirements():
    assert missing(100, 1.5) == [
        "need 20 more credits",
        "need 0.5 more GPA",
    ]


# ---------- text_tools.py ----------

def test_word_count_ignores_case_and_punctuation():
    assert word_count("Hello, hello! WORLD.") == {
        "hello": 2,
        "world": 1,
    }


def test_top_k_tie_breaks_alphabetically():
    # Edge case: words with equal frequencies
    assert top_k("banana apple cherry", 2) == [
        ("apple", 1),
        ("banana", 1),
    ]


def test_top_k_non_positive_k():
    # Edge case: k is zero
    assert top_k("apple banana", 0) == []


# ---------- timetable.py ----------

def test_by_day_groups_courses_and_sorts_them():
    schedule = [
        ("Math", "Monday"),
        ("Physics", "Monday"),
        ("English", "Tuesday"),
        ("Biology", "Monday"),
    ]

    assert by_day(schedule) == {
        "Monday": ["Biology", "Math", "Physics"],
        "Tuesday": ["English"],
    }


def test_by_day_empty_schedule():
    # Edge case: empty schedule
    assert by_day([]) == {}
