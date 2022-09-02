
import os

from typing import Dict


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


if __name__ == "__main__":
    with open(os.path.join(os.getcwd(), "input/rosalind_revc.txt"), "r") as lines:
        for line in lines:
            dna_complement: str = reverse_complement(line)

            with open(os.path.join(os.getcwd(), "output/rosalind_revc.txt"), 'a') as outs:
                outs.write(dna_complement)