from collections import Counter, defaultdict
from math import ceil


def analyse(pairs: list[tuple[str, float]]) -> dict[str, object]:
    counts: Counter[str] = Counter()
    latencies: defaultdict[str, list[float]] = defaultdict(list)

    for route, latency_ms in pairs:
        counts[route] += 1
        latencies[route].append(latency_ms)

    p95: dict[str, float] = {}

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