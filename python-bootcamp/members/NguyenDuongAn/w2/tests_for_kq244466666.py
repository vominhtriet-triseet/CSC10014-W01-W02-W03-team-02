from translate import sieve


def test_negative_input():
    assert sieve(-10) == []


def test_input_zero():
    assert sieve(0) == []


def test_input_one():
    assert sieve(1) == []


def test_smallest_prime():
    assert sieve(2) == [2]


def test_primes_and_composites():
    assert sieve(10) == [2, 3, 5, 7]


def test_perfect_square_boundary():
    assert sieve(49) == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47
    ]


def test_larger_input():
    assert sieve(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]