from pathlib import Path
import subprocess
import sys

BOOTCAMP = Path(__file__).resolve().parents[1]


def test_shared_study_planner_cli_runs_sample_csv() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "shared.study_planner",
            "samples/tasks.csv",
            "--hours",
            "2",
            "--today",
            "2026-10-26",
        ],
        cwd=BOOTCAMP,
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "Study Plan" in result.stdout
    assert "Assignment" in result.stdout
    assert "Unscheduled / remaining work" in result.stdout
    assert "Traceback" not in result.stderr
