### translation.py
### Given a RNA sequence obtain the protein sequence

# Input:
#  1. The RNA sequence

# Output:
#  1. The Protein sequence

import os
from typing import Dict, Set

codons: Dict[str, str] = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F",
    "CUC": "L", "AUC": "I", "GUC": "V", "UUA": "L", "CUA": "L",
    "AUA": "I", "GUA": "V", "UUG": "L", "CUG": "L", "AUG": "M",
    "GUG": "V", "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A", "UCA": "S",
    "CCA": "P", "ACA": "T", "GCA": "A", "UCG": "S", "CCG": "P",
    "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N",
    "GAU": "D", "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "","CAA": "Q","AAA": "K", "GAA": "E", "UAG": "",
    "CAG": "Q", "AAG": "K", "GAG": "E", "UGU": "C", "CGU": "R",
    "AGU": "S", "GGU": "G", "UGC": "C", "CGC": "R", "AGC": "S",
    "GGC": "G", "UGA": "", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G" 
}

def index_of_first_start_codon(sequence: str) -> int:
    for i in range(0, len(sequence)):
        if sequence[i:i+3] == "AUG":
            return i


def translate(rna_seq: str) -> str:
    """
    Translates a RNA sequence to a string.

    Parameters
    ----------
    rna_seq : str
        The RNA sequence to translate.

    Returns
    -------
    str
    """

    if not rna_seq:
        raise ValueError("Empty string")

    if not isinstance(rna_seq, str):
        raise ValueError("RNA sequence must be a string")
    
    characters: Set = set(rna_seq)
    rna_seq = rna_seq.replace(" ", "").strip("\n").upper()

    # if not {"A", "C", "G", "U"} == characters:
    #     raise ValueError("RNA sequence contains invalid characters")
    
    protein_seq: str = ""
    start_index = index_of_first_start_codon(rna_seq)

    for i in range(start_index, len(rna_seq), 3):
        protein_seq = "".join([protein_seq, codons[rna_seq[i:i+3]]])
    
    return protein_seq


if __name__ == "__main__":
    with open(os.path.join(os.getcwd(), "input/rosalind_prot.txt"), "r") as lines:
        for line in lines:
            with open(os.path.join(os.getcwd(), "output/rosalind_prot.txt"), "w") as outs:
                seq: str = translate(line)
                outs.write(f"{seq}\n")

