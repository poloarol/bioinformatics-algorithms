
import pytest

from translation import translate

@pytest.mark.parametrize("rna_seq, protein_seq", 
                [("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA", "MAMAPRTEINSTRING")])
def test_translate(rna_seq, protein_seq):
    assert translate(rna_seq) == protein_seq

