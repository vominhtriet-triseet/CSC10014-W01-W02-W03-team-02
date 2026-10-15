PUNCT = ".,!?;:"

def word_count(text: str) -> dict[str, int]:
    table = str.maketrans("", "", PUNCT)       
    words = text.lower().translate(table).split()
    counts: dict[str, int] = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    # count giảm dần, bằng nhau thì theo thứ tự chữ cái
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return ordered[:k]

print( top_k("Git is fun. Git is fast!", 2))