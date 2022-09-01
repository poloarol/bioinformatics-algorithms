
import pytest

from summation import summation

@pytest.mark.parametrize("first_number, second_number, expected", 
                            [(100, 200, 7500), (1, 100, 2500)])
def test_summation(first_number: float, second_number: float, expected: float):
    assert first_number < second_number < 10000
    sum: float = summation(first_number, second_number)
    assert sum == expected