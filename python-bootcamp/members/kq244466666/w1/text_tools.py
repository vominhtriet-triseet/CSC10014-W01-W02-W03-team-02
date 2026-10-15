def word_count(text: str) -> dict[str, int]:
    for char in ".,!?;:":
        text = text.replace(char, " ")

    words = text.lower().split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ordered[:max(0, k)]


if __name__ == "__main__":
    print(word_count("Git is fun. Git is fast!"))
    print(top_k("Git is fun. Git is fast!", 2))
