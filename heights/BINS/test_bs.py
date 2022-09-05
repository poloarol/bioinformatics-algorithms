
import pytest
from typing import List
from binary_search import binary_search

@pytest.mark.parametrize("a, b, sorted, unsorted, expected", 
            [(5, 6, [10, 20, 30, 40,50], [40, 10, 35, 15, 40, 20], [4, 1,-1,-1, 4, 2])])
def test_binary_search(a, b, sorted, unsorted, expected):
    results: List = []
    for element in unsorted:
        res: int = binary_search(element, sorted)
        results.append(res)
    assert expected == results