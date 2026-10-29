# Shared study planner

The shared planner uses the `Task` and `Block` dataclasses in `shared/contract.py`.

## Pipeline

```text
CSV → parse_csv → prioritise → allocate → render