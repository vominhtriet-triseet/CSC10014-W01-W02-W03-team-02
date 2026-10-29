from datetime import date, timedelta

WEEKDAYS = {
    "mon": 0,
    "tue": 1,
    "wed": 2,
    "thu": 3,
    "fri": 4,
    "sat": 5,
    "sun": 6,
}


def parse_due(text: str, today: date) -> date:
    text = text.strip().lower()

    if text == "tomorrow":
        return today + timedelta(days=1)

    if text in WEEKDAYS:
        target = WEEKDAYS[text]
        delta = (target - today.weekday()) % 7
        if delta == 0:
            delta = 7
        return today + timedelta(days=delta)

    parts = text.split()

    if (len(parts) == 3 and parts[0] == "in" and parts[2] == "days"):
        try:
            days = int(parts[1])
        except ValueError as exc:
            raise ValueError(f"Invalid date: {text}") from exc

        if days < 0:
            raise ValueError(f"Invalid date: {text}")

        return today + timedelta(days=days)

    try:
        return date.fromisoformat(text)
    except ValueError as exc:
        raise ValueError(f"Invalid date: {text}") from exc