def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("scores must not be empty")

    scores.sort()
    n = len(scores)

    minimum = min(scores)
    maximum = max(scores)
    mean = round(sum(scores) / n, 2)
    if n % 2 == 1:
        median = scores[n // 2]
    else:
        median = (scores[n // 2 - 1] + scores[n // 2]) / 2
    median = round(median, 2)

    return {"min": minimum, "max": maximum, "mean": mean, "median": median}

result = summary([6, 7.5, 8, 9])
print(result)