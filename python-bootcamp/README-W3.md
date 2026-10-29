# Week 3 — study planner and individual exercises

This companion documents the Week 3 work without replacing the repository's existing bootcamp README.

## Shared T-W3 demo

From the `python-bootcamp/` directory:

```bash
python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26
```

The CSV schema is `title,importance,effort_h,deadline`, with importance from 1 to 5 and deadline in `YYYY-MM-DD`. Tasks are ordered by `importance / max(days_until_deadline, 1)` and allocated greedily. If the available hours cannot cover every task, the command prints a partial plan, a warning, and remaining work. It does not claim the plan is optimal.

## Individual CLI

From `python-bootcamp/`:

```bash
python -m members.vominhtriet_triseet.w3.cli samples/tasks.csv --hours 2 --today 2026-10-26
python -m pytest members/vominhtriet_triseet/w3 -q
```

Each member should replace `vominhtriet_triseet` with their own member folder.

## Test all Week 3 work

```bash
python -m pytest -q
```

A valid partial plan returns `0`. Missing files, empty CSVs, malformed task data, or invalid available hours return `1` with a concise error on stderr. Invalid command-line syntax is handled by `argparse` and returns `2`.

## T-W3 team handoff

The four assigned contributors are `NPTho510`, `NguyenDuongAn`, `reiryuka`, and `kq244466666`. Download and extract [`T-W3-member-packages.zip`](T-W3-member-packages.zip), then follow the README in the matching username folder. Each member owns a separate set of files and should submit those files through their own branch and PR.

The ZIP is a local distribution bundle, not a substitute for source files in Git. Regenerate it after changing any assignment files with:

```bash
python tools/build_t_w3_member_packs.py
```

## Personal submission reminder

`vominhtriet_triseet`'s individual W3 files are under `members/vominhtriet_triseet/w3/`. Review and test that folder, then stage only those files for the personal PR. Do not include the shared T-W3 integration changes in the individual PR unless the group explicitly assigns those changes to you.
