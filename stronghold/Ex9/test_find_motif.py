
import pytest

from find_motif import find_motif

@pytest.mark.parametrize("sequence, motif, expected", 
                [("GATATATGCATATACTT", "ATAT", "2 4 10")])
def test_find_motif(sequence, motif, expected):
    result = find_motif(sequence, motif)
    assert result == expected

