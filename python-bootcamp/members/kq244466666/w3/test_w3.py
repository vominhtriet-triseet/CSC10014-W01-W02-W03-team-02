from datetime import date, timedelta

import pytest

from members.kq244466666.w3.dates import parse_due
from members.kq244466666.w3.log_stats import analyse


def test_parse_iso_date():
    assert parse_due("2026-10-30", date(2026, 10, 26)) == date(2026, 10, 30)


def test_parse_tomorrow():
    assert parse_due("tomorrow", date(2026, 10, 26)) == date(2026, 10, 27)


def test_parse_relative_days():
    assert parse_due("in 3 days", date(2026, 10, 26)) == date(2026, 10, 29)


def test_parse_next_weekday():
    assert parse_due("Fri", date(2026, 10, 26)) == date(2026, 10, 30)


def test_same_weekday_means_next_week():
    friday = date(2026, 10, 30)
    assert parse_due("Fri", friday) == friday + timedelta(days=7)


def test_invalid_date():
    with pytest.raises(ValueError):
        parse_due("someday", date(2026, 10, 26))


def test_analyse():
    result = analyse(
        [
            ("/chat", 100),
            ("/chat", 200),
            ("/login", 50),
        ]
    )

    assert result["counts"] == {"/chat": 2, "/login": 1}
    assert result["p95"] == {"/chat": 200.0, "/login": 50.0}
    assert result["slowest"] == "/chat"


def test_analyse_empty():
    result = analyse([])
    assert result == {"counts": {}, "p95": {}, "slowest": None}


def test_analyse_rejects_negative_latency():
    with pytest.raises(ValueError):
        analyse([("/chat", -1)])
