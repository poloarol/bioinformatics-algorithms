
import pytest

from reverse_complement import reverse_complement

@pytest.mark.parametrize("dna, cdna", 
                [("AAAACCCGGT", "ACCGGGTTTT")])
def test_reverse_complement(dna, cdna):
    cdna_seq: str = reverse_complement(dna)
    assert cdna_seq == cdna