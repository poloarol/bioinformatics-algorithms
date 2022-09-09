
import pytest
from typing import Tuple, Set

from restriction_sites import find_palindromes

expected_results: Set[Tuple[int, int]] = {(4, 6), (5, 4), (6, 6), (7, 4), (17, 4), (18, 4), (20, 6), (21, 4)}

@pytest.mark.parametrize("dna_sequence, expected_result", [("TCAATGCATGCGGGTCTATATGCAT", expected_results)])
def test_find_palindromes(dna_sequence, expected_result):
    assert find_palindromes(dna_sequence) == expected_result
