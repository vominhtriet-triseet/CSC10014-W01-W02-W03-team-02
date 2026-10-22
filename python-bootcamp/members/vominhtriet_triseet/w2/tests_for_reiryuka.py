from members.reiryuka.w1.translate import binary_search


def test_finds_middle_element() -> None:
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_finds_first_element() -> None:
    assert binary_search([1, 3, 5, 7, 9], 1) == 0


def test_finds_last_element() -> None:
    assert binary_search([1, 3, 5, 7, 9], 9) == 4


def test_returns_minus_one_when_key_is_missing() -> None:
    assert binary_search([1, 3, 5, 7, 9], 4) == -1


def test_empty_list_returns_minus_one() -> None:
    assert binary_search([], 5) == -1


def test_single_element_list() -> None:
    assert binary_search([5], 5) == 0
    assert binary_search([5], 2) == -1
