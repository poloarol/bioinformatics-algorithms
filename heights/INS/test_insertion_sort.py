

import pytest

from insertion_sort import insertion_sort


@pytest.mark.parametrize("length, data, expected", [(6, [6, 10, 4, 5, 1, 2], 12)])
def test_insertion_sort(length, data, expected):
    assert len(data) == length
    assert insertion_sort(data) == expected
