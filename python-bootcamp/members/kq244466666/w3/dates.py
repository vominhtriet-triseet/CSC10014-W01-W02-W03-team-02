import re
from datetime import date, timedelta

_WEEKDAYS = {
    "mon": 0,
    "tue": 1,
    "wed": 2,
    "thu": 3,
    "fri": 4,
    "sat": 5,
    "sun": 6,
}


def parse_due(text: str, today: date) -> date:
    """Parse a due-date expression relative to today."""
    value = text.strip().lower()

    if value == "tomorrow":
        return today + timedelta(days=1)

    match = re.fullmatch(r"in\s+(\d+)\s+days?", value)
    if match:
        return today + timedelta(days=int(match.group(1)))

    if value in _WEEKDAYS:
        target_weekday = _WEEKDAYS[value]
        days_ahead = (target_weekday - today.weekday()) % 7

        if days_ahead == 0:
            days_ahead = 7

        return today + timedelta(days=days_ahead)

    try:
        return date.fromisoformat(value)
    except ValueError:
        raise ValueError(f"Invalid due date: {text!r}") from None
