
import pytest

from transcription import transcribe

@pytest.mark.parametrize("dna, rna", 
                [("GATGGAACTTGACTACGTAAATT", "GAUGGAACUUGACUACGUAAAUU")])
def test_transcribe(dna, rna):
    rna_seq: str = transcribe(dna)
    assert rna_seq == rna