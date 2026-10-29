# T-W3 demo

Run from the `python-bootcamp/` directory:

```bash
python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26
```

Expected output (spacing may vary):

```text
Study Plan
==========

Scheduled
- Assignment: 1.5 h
- DS exam: 0.5 h

Unscheduled / remaining work
- DS exam: 5.5 h

Note: The tasks need 7.5 hours, but only 2 hours are available. Remaining work is listed below.
```

The plan keeps within the two-hour limit. It makes the incomplete allocation visible instead of treating it as a complete schedule.

To check the missing-file path:

```bash
python -m shared.study_planner samples/not-found.csv --hours 2
```

This prints a short error to stderr and exits with status `1`. A valid partial plan exits with status `0`.
