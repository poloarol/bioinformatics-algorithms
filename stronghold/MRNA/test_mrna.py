
import pytest

from mrna import get_rna


@pytest.mark.parametrize("sequence, expected", [("MA", 12)])
def test_num_mrna(sequence, expected):
    value: float = 1.0

    for aa in sequence:
        value = value * get_rna(aa)

    num_rna: float = (3*value) % 1000000

    assert num_rna == expected