from w1.translate import insertion_sort


def test_sort_unsorted_list():
    assert insertion_sort([3, 1, 2]) == [1, 2, 3]


def test_sort_empty_list():
    assert insertion_sort([]) == []


def test_sort_already_sorted_list():
    assert insertion_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_sort_reverse_order():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_sort_with_duplicates():
    assert insertion_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]


def test_sort_negative_numbers():
    assert insertion_sort([-3, 2, -1, 0]) == [-3, -1, 0, 2]


def test_sort_single_element():
    assert insertion_sort([7]) == [7]


def test_sort_does_not_change_original_list():
    original = [3, 1, 2]
    expected = original.copy()

    insertion_sort(original)

    assert original == expected
