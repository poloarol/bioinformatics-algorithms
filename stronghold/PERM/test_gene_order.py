
import pytest

from gene_order import find_permutations

expected_results: str = """6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1"""

@pytest.mark.parametrize("genes, expected", [(3, expected_results)])
def test_find_permutations(genes: int, expected: str):
    results = find_permutations(genes)
    print(results)
    assert results == expected
