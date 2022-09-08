

from typing import Set
from lcsm import find_motif

import pytest

sequences: str = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""

@pytest.mark.parametrize("fasta, expected_sequence", [(sequences, "AC")])
def test_find_motif(fasta: str, expected_sequence: str) -> None:
    sequence_content: Set[str] = set()

    key: str = ''
    nucleotide: str = ''
    for line in fasta.split("\n"):
        if line.startswith('>'):
            if key:
                sequence_content.add(nucleotide)
                key = line.strip('\n').replace('>','')
                nucleotide = ""
            else:
                key = line.strip('\n').replace('>','')
        else:
            nucleotide = ''.join([nucleotide, line]).strip().strip("\n")
        sequence_content.add(nucleotide.replace('\n', '')) # add last key, value pair
    
    while "" in sequence_content:
        sequence_content.remove("")

    # shortest_sequence = min(sequence_content, key=len)
    # sequence_content.remove(shortest_sequence)

    longest_common_seq: str = find_motif(list(sequence_content))

    assert expected_sequence == longest_common_seq


