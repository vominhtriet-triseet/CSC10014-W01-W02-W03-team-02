from render import render

def test_render_empty_blocks():
    assert render([]) == "Study Plan\n=========="


def test_render_one_block():
    blocks = [
        {
            "day": "Monday",
            "subject": "Python",
            "duration": 60,
        }
    ]
    expected = (
        "Study Plan\n"
        "==========\n"
        "\n"
        "Monday\n"
        "- Python: 60 minutes"
    )

    assert render(blocks) == expected


def test_render_multiple_blocks_same_day():
    blocks = [
        {
            "day": "Monday",
            "subject": "Python",
            "duration": 60,
        },
        {
            "day": "Monday",
            "subject": "Math",
            "duration": 90,
        },
    ]
    expected = (
        "Study Plan\n"
        "==========\n"
        "\n"
        "Monday\n"
        "- Python: 60 minutes\n"
        "- Math: 90 minutes"
    )

    assert render(blocks) == expected


def test_render_multiple_days():
    blocks = [
        {
            "day": "Monday",
            "subject": "Python",
            "duration": 60,
        },
        {
            "day": "Tuesday",
            "subject": "Math",
            "duration": 90,
        },
    ]

    result = render(blocks)

    assert result.index("Monday") < result.index("Tuesday")
    assert "Python: 60 minutes" in result
    assert "Math: 90 minutes" in result