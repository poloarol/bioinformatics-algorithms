
import pytest

from mortal_fib import mortal_fib

@pytest.mark.parametrize("num_rabbits, num_months, expected", [(6, 3, 4)])
def test_mortal_fib(num_rabbits, num_months, expected):
    assert mortal_fib(num_rabbits, num_months) == expected
