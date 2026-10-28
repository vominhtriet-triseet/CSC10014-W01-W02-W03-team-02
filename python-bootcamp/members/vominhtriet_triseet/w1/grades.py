import statistics


def summary(scores: list[float]) -> dict[str, int | float]:
    """Return minimum, maximum, mean, and median scores."""
    if not scores:
        raise ValueError("no values provided")
    
    return {
        "min": min(scores),
        "max": max(scores),
        "mean": round(statistics.mean(scores), 2),
        "median": round(statistics.median(scores), 2)
    }
