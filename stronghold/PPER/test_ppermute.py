
import pytest

from ppermute import partial_permutation

@pytest.mark.parametrize("n, k, expected", [(21, 7, 51200)])
def test_partial_permutation(n, k, expected):
    pper: int = partial_permutation(n, k)

    assert pper == expected
