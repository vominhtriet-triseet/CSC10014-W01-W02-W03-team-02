#W1-1
def summary(scores: list[float]) -> dict:
    if len(scores) == 0:
        raise ValueError("Scores cannot be empty")

    min_score = min(scores)
    max_score = max(scores)

    mean = round(sum(scores) / len(scores), 2)

    sorted_scores = sorted(scores)
    n = len(sorted_scores)

    if n % 2 == 1:
        median = sorted_scores[n // 2]
    else:
        median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2
        median = round(median, 2)

    return {
        "min": min_score,
        "max": max_score,
        "mean": mean,
        "median": median
    }


print(summary([7.5, 9, 6, 8]))