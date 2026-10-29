from collections import Counter, defaultdict
from collections.abc import Iterable
from math import ceil
from typing import TypedDict

Latency = int | float
RequestPair = tuple[str, Latency]


class AnalysisResult(TypedDict):
    """Statistics calculated from route and latency pairs."""

    counts: Counter[str]
    p95: dict[str, Latency]
    slowest: str | None


def analyse(pairs: Iterable[RequestPair]) -> AnalysisResult:
    """Count requests and calculate each route's 95th-percentile latency.

    Args:
        pairs: Iterable of ``(route, latency_ms)`` pairs.

    Returns:
        A dictionary containing route counts, p95 latencies, and the route
        with the highest p95 latency. ``slowest`` is ``None`` if no pairs
        are provided.
    """
    counts: Counter[str] = Counter()
    latencies: defaultdict[str, list[Latency]] = defaultdict(list)

    for route, latency_ms in pairs:
        counts[route] += 1
        latencies[route].append(latency_ms)

    p95: dict[str, Latency] = {}
    for route, values in latencies.items():
        values.sort()
        index = ceil(0.95 * len(values)) - 1
        p95[route] = values[index]

    slowest = max(p95, key=p95.get) if p95 else None

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest,
    }
