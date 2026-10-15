#W1-2
def word_count(text: str) -> dict[str, int]:
    text = text.lower()

    for punctuation in ".,!?;:":
        text = text.replace(punctuation, "")

    words = text.split()
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)

    sorted_words = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    return sorted_words[:k]


print(word_count("Git is fun. Git is fast!"))
print(top_k("Git is fun. Git is fast!", 2))
