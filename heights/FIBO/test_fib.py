

import pytest
from fib import fib_recursive, fib_binet


@pytest.mark.parametrize("n, expected", [(6, 8), (1, 1), (10, 55)])
def test_fib(n, expected):
    assert fib_recursive(n) == expected
    assert fib_binet(n) == expected