import pytest

from myapp.app import multiply_by_two, divide_by_two

def test_custom_multiplication():
    assert multiply_by_two(16) == 32  # Adjust based on ID



@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a,b]


class TestApp:
    def test_multiplication(self, numbers):
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        res = divide_by_two(numbers[1])
        assert res == numbers[0]

    def test_custom_multiplication(self):
        assert multiply_by_two(16) == 50 # MY Student ID
