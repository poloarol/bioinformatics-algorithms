
import pytest

from typing import List, Set
from orf import translation, find_orf, reverse_complement

dna: str = """>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"""

protein: str = """MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE"""

@pytest.mark.parametrize("sequence, expected", [(dna, protein)])
def test_orfs(sequence, expected):
    protein_seq: Set[str] =set()
    seq: List[str] = sequence.split("\n")
    for i in range(len(seq)):
        if ">" not in seq[i]:
            start_one, start_two = find_orf(seq[i]), find_orf(reverse_complement(seq[i]))
            start: List[int] = start_one if len(start_one) < len(start_two) else start_two

            for s, t in zip(start_one, start_two):
                tmp_one: str = translation(s, seq[i])
                tmp_two: str = translation(t, reverse_complement(seq[i]))
                print(s, t)
                protein_seq.add(tmp_two)
                protein_seq.add(tmp_one)

    print(protein_seq)

    assert expected == protein_seq