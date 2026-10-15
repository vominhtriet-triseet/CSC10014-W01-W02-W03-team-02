from statistics import median
from typing import List, Dict

def summary(scores: List[float]) -> Dict[str, float]:
    if not scores:
        return ValueError("Invalid list")

    min_val = min(scores)
    max_val = max(scores)
    mean_val = round(sum(scores)/ len(scores), 2)
    median_val = round(median(scores), 2)

    return {
        'min': min_val,
        'max':  max_val,
        'mean': mean_val,
        'median': median_val
    }

print(summary([7.5, 6, 8, 9]))




    