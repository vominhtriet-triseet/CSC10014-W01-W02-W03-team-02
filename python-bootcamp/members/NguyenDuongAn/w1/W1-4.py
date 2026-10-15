def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Python's zip makes it easy to transpose rows without manual indexing."""
    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    print(transpose(matrix))
