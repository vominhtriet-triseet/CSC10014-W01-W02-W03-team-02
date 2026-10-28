def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return whether the student meets both thesis registration rules."""
    return credits >= 120 and gpa >= 2.0

def missing(credits: int, gpa: float) -> list[str]:
    """List the thesis registration requirements the student still lacks."""
    reasons = []
    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reasons.append(f"need {round(2.0 - gpa, 2)} more GPA") 
    return reasons
