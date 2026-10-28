"""Summarize request counts and p95 latency by route."""

from collections import Counter
from collections.abc import Iterable
from math import ceil, isfinite


def analyse(pairs: Iterable[tuple[str, int | float]]) -> dict[str, object]:
    """Return request counts, nearest-rank p95 latencies, and the slowest route."""
    counts: Counter[str] = Counter()
    latencies: dict[str, list[int | float]] = {}
    for route, latency_ms in pairs:
        if not isinstance(route, str):
            raise TypeError("route must be a string")
        if not route.strip():
            raise ValueError("route must be a non-empty string")
        if isinstance(latency_ms, bool) or not isinstance(latency_ms, (int, float)):
            raise TypeError("latency must be a number")
        if latency_ms < 0 or (isinstance(latency_ms, float) and not isfinite(latency_ms)):
            raise ValueError("latency must be a finite, non-negative number")
        counts[route] += 1
        latencies.setdefault(route, []).append(latency_ms)

    p95 = {
        route: sorted(values)[ceil(0.95 * len(values)) - 1]
        for route, values in latencies.items()
    }
    slowest = max(p95, key=p95.__getitem__) if p95 else None
    return {"counts": counts, "p95": p95, "slowest": slowest}
