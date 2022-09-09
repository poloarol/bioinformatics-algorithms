### restriction_sites.py
### Given a DNA sequence, find all the restriction sites
### NB: Restricition sites are palindromic

### Not my solution: https://www.techiedelight.com/find-possible-palindromic-substrings-string/

import os
from typing import Dict, List, Tuple, Set

pair: Dict[str, str] = {"A": "T", "C": "G", "G": "C", "T": "A"}

def reverse_complement(nucletodides: str) -> str:
    """
    Reverse complement a DNA sequence.

    Parameters
    ----------
    dna_sequence : str
        DNA sequence

    Returns
    -------
    str
        Reverse complement of DNA sequence
    """

    if nucletodides and len(nucletodides) <= 1000:
        complement_sequence: str = ""
        nucletodides = nucletodides.upper().replace(" ", "")
        for nt in nucletodides:
            complement_sequence = "".join([complement_sequence, pair[nt]])
        
        return complement_sequence[::-1]


def find_palindromes(sequence: str) -> List[Tuple[int, int]]:
    palindromes: Set = set()

    for size in range(4,13):
        for i in range(len(sequence) - size + 1):
            sc = reverse_complement(sequence[i:i+size])
            if sequence[i:i+size] == sc:
                palindromes.add((i+1, size))
    
    return palindromes


if __name__ == "__main__":
    sequence_content: Dict[str, str] = {}

    with open(os.path.join(os.getcwd(), "input/rosalind_revp.txt"), "r") as lines:
        key: int = ''
        nucleotide: str = ''

        k: int = 3

        for line in lines:
            if line.startswith('>'):
                if key:
                    sequence_content[key] = nucleotide.replace('\n', '')
                    key = line.strip('\n').replace('>','')
                    nucleotide = ""
                else:
                    key = line.strip('\n').replace('>','')
            else:
                nucleotide = ''.join([nucleotide, line])
        sequence_content[key] = nucleotide.replace('\n', '')
    
    for key, value in sequence_content.items():
        with open(os.path.join(os.getcwd(), "output/rosalind_revp.txt"), "w") as outs:
            for pairs in find_palindromes(value):
                outs.write(" ".join(str(pair) for pair in pairs) + "\n")