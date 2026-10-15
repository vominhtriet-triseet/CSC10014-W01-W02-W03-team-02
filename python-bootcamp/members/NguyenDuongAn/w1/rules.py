def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    reasons = []
    
    if credits < 120:
        needed_credits = 120 - credits
        reasons.append(f"need {needed_credits} more credits")

    
    if gpa < 2.0:
        reasons.append(f"need higher GPA (current is {gpa}, need at least 2.0)")
        
    return reasons

print(can_register_thesis(125, 2.5))
print(missing(125, 2.5))

print(can_register_thesis(118, 1.8))
print(missing(118, 1.8))
