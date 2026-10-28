"""Parse the small set of due-date phrases required for Week 3."""

import re
from datetime import date, timedelta

_WEEKDAYS = {
    "mon": 0,
    "monday": 0,
    "tue": 1,
    "tuesday": 1,
    "wed": 2,
    "wednesday": 2,
    "thu": 3,
    "thursday": 3,
    "fri": 4,
    "friday": 4,
    "sat": 5,
    "saturday": 5,
    "sun": 6,
    "sunday": 6,
}
_ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}\Z")
_IN_DAYS = re.compile(r"in\s+(\d+)\s+days?\Z", re.IGNORECASE)


def parse_due(value: str, today: date) -> date:
    """Parse an ISO date, relative phrase, or the next named weekday.

    A weekday name means its next occurrence; naming today's weekday refers to
    seven days from today.
    """
    if not isinstance(value, str):
        raise TypeError("due date must be text")
    if not isinstance(today, date):
        raise TypeError("today must be a date")

    text = value.strip()
    normalized = text.casefold()
    if normalized == "tomorrow":
        days_ahead = 1
    else:
        match = _IN_DAYS.fullmatch(normalized)
        if match:
            days_ahead = int(match.group(1))
        elif normalized in _WEEKDAYS:
            days_ahead = (_WEEKDAYS[normalized] - today.weekday()) % 7 or 7
        else:
            if not _ISO_DATE.fullmatch(text):
                raise ValueError(f"unsupported due date: {value!r}")
            try:
                return date.fromisoformat(text)
            except ValueError as error:
                raise ValueError(f"unsupported due date: {value!r}") from error

    try:
        return today + timedelta(days=days_ahead)
    except OverflowError as error:
        raise ValueError("due date is outside the supported date range") from error
