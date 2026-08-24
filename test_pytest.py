import pytest


def add(a, b):
    return a + b


def test_add():
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    assert add(a, b) == 5


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (10, 20, 30),
    ]
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.skip(reason="Feature not implemented yet")
def test_something():
    assert 1 == 2


class TestCalculator:

    def test_add(self):
        assert 2 + 3 == 5

    def test_subtract(self):
        assert 5 - 3 == 2

    def test_multiply(self):
        assert 3 * 4 == 12


def divide(a, b):
    return a / b


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
