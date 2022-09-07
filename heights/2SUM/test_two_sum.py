

import pytest
from typing import List
from two_sum import two_sum

data: List[List[int]] = [[2, -3, 4, 10, 5], [8, 2, 4, -2, -8], [-5, 2, 3, 2, -4], [5, 4, -5, 6, 8]]
expected_results: List[List[int]] = [[-1], [2, 4], [-1], [1, 3]]

@pytest.mark.parametrize("sequences, expected", 
            [(data, expected_results)])
def test_two_sum(sequences: List[int], expected: List[List[int]]):
    results: List[List[int]] = []
    for sequence in sequences:
        results.append(two_sum(sequence))
    assert expected == results