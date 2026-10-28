import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

from members.vominhtriet_triseet.w3.dates import parse_due
from members.vominhtriet_triseet.w3.log_stats import analyse

BOOTCAMP = Path(__file__).resolve().parents[3]
CLI_MODULE = "members.vominhtriet_triseet.w3.cli"


def test_parse_due_accepts_supported_formats() -> None:
    today = date(2026, 10, 6)

    assert parse_due("2026-10-30", today) == date(2026, 10, 30)
    assert parse_due(" tomorrow ", today) == date(2026, 10, 7)
    assert parse_due("in 3 days", today) == date(2026, 10, 9)
    assert parse_due("Fri", today) == date(2026, 10, 9)
    assert parse_due("Tuesday", today) == date(2026, 10, 13)


def test_parse_due_same_weekday_means_next_week() -> None:
    today = date(2026, 10, 6)

    assert parse_due("Tue", today) == date(2026, 10, 13)


def test_parse_due_rejects_unknown_or_invalid_dates() -> None:
    today = date(2026, 10, 6)

    for value in ("someday", "2026-02-30", "20261030", "2026-W44-5"):
        with pytest.raises(ValueError, match="unsupported due date"):
            parse_due(value, today)


def test_parse_due_rejects_invalid_types_and_date_overflow() -> None:
    with pytest.raises(TypeError, match="must be text"):
        parse_due(3, date(2026, 10, 6))
    with pytest.raises(ValueError, match="supported date range"):
        parse_due("tomorrow", date.max)


def test_analyse_counts_and_ranks_p95_by_route() -> None:
    result = analyse(
        [("api", latency) for latency in range(1, 21)]
        + [("slow", 100), ("slow", 200)]
    )

    assert result == {
        "counts": {"api": 20, "slow": 2},
        "p95": {"api": 19, "slow": 200},
        "slowest": "slow",
    }


def test_analyse_preserves_large_integer_precision() -> None:
    first = 2**53
    second = first + 1

    assert analyse([("first", first), ("second", second)]) == {
        "counts": {"first": 1, "second": 1},
        "p95": {"first": first, "second": second},
        "slowest": "second",
    }


def test_analyse_empty_input() -> None:
    assert analyse([]) == {"counts": {}, "p95": {}, "slowest": None}


@pytest.mark.parametrize(
    "pairs",
    [
        [("", 1)],
        [("api", -1)],
        [("api", float("nan"))],
        [("api", float("inf"))],
    ],
)
def test_analyse_rejects_invalid_values(pairs: list[tuple[object, object]]) -> None:
    with pytest.raises(ValueError):
        analyse(pairs)


def test_analyse_rejects_wrong_types() -> None:
    with pytest.raises(TypeError, match="route must be a string"):
        analyse([(42, 1)])
    with pytest.raises(TypeError, match="latency must be a number"):
        analyse([("api", True)])


def run_cli(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", CLI_MODULE, *arguments],
        cwd=BOOTCAMP,
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )


def test_cli_creates_reproducible_plan_from_sample_csv() -> None:
    result = run_cli(
        "samples/tasks.csv",
        "--hours",
        "2",
        "--today",
        "2026-10-26",
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout.startswith("Tonight (2.0 h):")
    assert result.stdout.index("Assignment") < result.stdout.index("DS exam")
    assert "1. Assignment ...... 1.5 h" in result.stdout
    assert "2. DS exam ...... 0.5 h" in result.stdout
    assert "Traceback" not in result.stderr


def test_cli_reports_missing_csv_without_traceback() -> None:
    result = run_cli("samples/missing.csv", "--hours", "2")

    assert result.returncode == 1
    assert "Error:" in result.stderr
    assert "Traceback" not in result.stderr


def test_cli_reports_empty_csv(tmp_path: Path) -> None:
    csv_path = tmp_path / "empty.csv"
    csv_path.write_text("title,importance,effort_h,deadline\n", encoding="utf-8")

    result = run_cli(str(csv_path), "--hours", "2")

    assert result.returncode == 1
    assert "CSV contains no task rows" in result.stderr
    assert "Traceback" not in result.stderr


def test_cli_rejects_invalid_hours_without_traceback() -> None:
    result = run_cli("samples/tasks.csv", "--hours", "nan")

    assert result.returncode == 1
    assert "finite, non-negative" in result.stderr
    assert "Traceback" not in result.stderr


def test_cli_rejects_invalid_today_date() -> None:
    result = run_cli("samples/tasks.csv", "--hours", "2", "--today", "2026-02-30")

    assert result.returncode == 2
    assert "date must be YYYY-MM-DD" in result.stderr
    assert "Traceback" not in result.stderr
