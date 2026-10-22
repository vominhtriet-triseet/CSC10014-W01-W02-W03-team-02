def test_transpose_square_matrix(load):
    tr = load("w1", "translate")
    assert tr.transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_transpose_single_row(load):
    tr = load("w1", "translate")
    assert tr.transpose([[1, 2, 3]]) == [[1], [2], [3]]

def test_transpose_single_column(load):
    tr = load("w1", "translate")
    assert tr.transpose([[1], [2], [3]]) == [[1, 2, 3]]

def test_transpose_negative_numbers(load):
    tr = load("w1", "translate")
    assert tr.transpose([[-1, 2], [3, -4]]) == [[-1, 3], [2, -4]]

def test_transpose_single_element(load):
    tr = load("w1", "translate")
    assert tr.transpose([[42]]) == [[42]]

def test_transpose_one_empty_row(load):
    tr = load("w1", "translate")
    assert tr.transpose([[]]) == []