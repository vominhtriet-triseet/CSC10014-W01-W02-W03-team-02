#W1-3

def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    reasons = []

    if credits < 120:
        need = 120 - credits
        reasons.append(f"need {need} more credits")

    if gpa < 2.0:
        reasons.append("GPA must be at least 2.0")

    return reasons


print(can_register_thesis(118, 2.5))
print(missing(118, 2.5))

print(can_register_thesis(120, 2.0))
print(missing(120, 2.0))
