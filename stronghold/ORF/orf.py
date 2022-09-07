
### orf.py
### Find all open reading frames

import os
from typing import List, Dict

codons: Dict[str, str] = {
    "TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V", "TTC": "F",
    "CTC": "L", "ATC": "I", "GTC": "V", "TTA": "L", "CTA": "L",
    "ATA": "I", "GTA": "V", "TTG": "L", "CTG": "L", "ATG": "M",
    "GTG": "V", "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
    "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A", "TCA": "S",
    "CCA": "P", "ACA": "T", "GCA": "A", "TCG": "S", "CCG": "P",
    "ACG": "T", "GCG": "A", "TAT": "Y", "CAT": "H", "AAT": "N",
    "GAT": "D", "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "TAA": "","CAA": "Q","AAA": "K", "GAA": "E", "TAG": "",
    "CAG": "Q", "AAG": "K", "GAG": "E", "TGT": "C", "CGT": "R",
    "AGT": "S", "GGT": "G", "TGC": "C", "CGC": "R", "AGC": "S",
    "GGC": "G", "TGA": "", "CGA": "R", "AGA": "R", "GGA": "G",
    "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G" 
}

pair: Dict[str, str] = {"A": "T", "C": "G", "G": "C", "T": "A"}

def find_orf(sequence: str) -> int:
    start_codons: List[int] = []
    for i in range(0, len(sequence)-2):
        if "ATG" == sequence[i:i+3]:
            start_codons.append(i)
    
    return start_codons

def translation(start: int, sequence: str) -> str:
    protein: str = ""

    for i in range(start, len(sequence), 3):
        if codons[sequence[i:i+3]]:
            protein = "".join([protein, codons[sequence[i:i+3]]])
        else:
            break
    
    return protein

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

# TODO: Output is wrong

if __name__ == "__main__":
    with open(os.path.join(os.getcwd(), "input/rosalind_orf.txt"), "r") as lines:
        for line in lines:
            if ">" not in line:
                starts: List[int] = find_orf(line.strip("\n"))
                
                with open(os.path.join(os.getcwd(), "output/rosalind_orf.txt"), "w") as outs:
                    for start in starts:
                        protein_sequence: str = translation(start, line)
                        outs.write(protein_sequence)
