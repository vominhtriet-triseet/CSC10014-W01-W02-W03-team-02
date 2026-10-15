def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("scores must not be empty")

    s = sorted(scores)
    n = len(s)
    mid = n // 2
    median = s[mid] if n % 2 == 1 else (s[mid - 1] + s[mid]) / 2

    return {
        "min": s[0],
        "max": s[-1],
        "mean": round(sum(s) / n, 2),
        "median": round(median, 2),
    }
print([])
print(7.5, 9, 6, 8)