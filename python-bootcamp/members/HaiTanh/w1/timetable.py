def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for course, day in entries:
        result.setdefault(day, []).append(course)
    return {day: sorted(courses) for day, courses in result.items()}
print(by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")])
)