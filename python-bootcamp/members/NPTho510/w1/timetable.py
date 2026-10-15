def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = {}

    for course, day in courses:
        result.setdefault(day, []).append(course)
    for day in result:
        result[day].sort()

    return result

print(by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]))