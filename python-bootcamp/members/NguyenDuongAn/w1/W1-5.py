def by_day(courses):
    result = {}
    for course, day in courses:
        result.setdefault(day, []).append(course)
    
    for day in result:
        result[day].sort()
        
    return result

data = [("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]
print(by_day(data))