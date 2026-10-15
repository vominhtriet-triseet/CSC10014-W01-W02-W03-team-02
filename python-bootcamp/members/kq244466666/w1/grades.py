def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("scores cannot be empty")

    ordered = sorted(scores)
    n = len(ordered)

    if n % 2 == 0:
        median = (ordered[n // 2 - 1] + ordered[n // 2]) / 2
    else:
        median = ordered[n // 2]

    return {
        "min": min(scores),
        "max": max(scores),
        "mean": round(sum(scores) / n, 2),
        "median": round(median, 2)
    }


if __name__ == "__main__":
    print(summary([7.5, 9, 6, 8]))
