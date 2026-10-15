def can_register_thesis(credits: int, gpa: float) -> bool:
    if credits >= 120 and gpa >= 2.0:
        return True
    return False

def missing(credits: int, gpa: float) -> list[str]:
    result = []
    if not can_register_thesis(credits, gpa):
        if credits < 120:
            result.append(f"need {120 - credits} more credits")
        if gpa < 2.0:
            result.append("gpa needs to be 2.0")
    return result

a = missing(119, 1.9)
print(a)