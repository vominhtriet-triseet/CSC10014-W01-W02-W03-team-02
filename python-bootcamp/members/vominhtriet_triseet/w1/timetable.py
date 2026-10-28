def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and sort each day's course list."""
    result = {}
    for course, day in schedule:
        result.setdefault(day, []).append(course)
    
    for courses in result.values():
        courses.sort()
        
    return result
