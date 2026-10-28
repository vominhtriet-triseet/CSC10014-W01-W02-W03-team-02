from collections import Counter, defaultdict
from collections.abc import Iterable
from math import ceil


def analyse(
    pairs: Iterable[tuple[str, float]],
) -> dict[str, dict[str, int] | dict[str, float] | str | None]:
    """Count requests and calculate the p95 latency for each route."""
    counts: Counter[str] = Counter()
    latencies: defaultdict[str, list[float]] = defaultdict(list)

    for route, latency_ms in pairs:
        if latency_ms < 0:
            raise ValueError("Latency cannot be negative")

        counts[route] += 1
        latencies[route].append(float(latency_ms))

    p95: dict[str, float] = {}

    for route, values in latencies.items():
        ordered = sorted(values)
        index = ceil(0.95 * len(ordered)) - 1
        p95[route] = ordered[index]

    slowest = max(p95, key=p95.get) if p95 else None

    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": slowest,
    }
