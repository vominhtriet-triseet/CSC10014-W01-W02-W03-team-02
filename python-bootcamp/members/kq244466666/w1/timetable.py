def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = {}

    for course, day in courses:
        result.setdefault(day, []).append(course)

    return {
        day: sorted(course_list)
        for day, course_list in result.items()
    }


if __name__ == "__main__":
    courses = [
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon")
    ]

    print(by_day(courses))
