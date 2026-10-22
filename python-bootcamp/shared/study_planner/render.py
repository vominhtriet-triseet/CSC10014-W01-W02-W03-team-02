def render(blocks) -> str:
    if not blocks:
        return "Study Plan\n=========="

    lines = ["Study Plan", "=========="]

    current_day = None

    for block in blocks:
        day = block["day"]
        subject = block["subject"]
        duration = block["duration"]

        if day != current_day:
            lines.append("")
            lines.append(day)
            current_day = day

        lines.append(f"- {subject}: {duration} minutes")

    return "\n".join(lines)
