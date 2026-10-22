def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    reasons = []

    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")

    if gpa < 2.0:
        reasons.append(f"need GPA {2.0 - gpa:.2f} more")

    return reasons


if __name__ == "__main__":
    print(can_register_thesis(118, 2.5))
    print(missing(118, 1.8))
