

import pytest

from fib_rabbits import fib

@pytest.mark.parametrize("a, b, c", [(5, 3, 19)])
def test_fib(a, b, c):
    assert fib(a, b) == c