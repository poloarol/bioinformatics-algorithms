
### splice_sites.py
### Goal to return translated protein of a dna strand after removing a list of introns.

import os
from typing import Dict, Set, List

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

def index_of_first_start_codon(sequence: str) -> int:
    for i in range(0, len(sequence)):
        if sequence[i:i+3] == "ATG":
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


def remove_introns(dna_sequence: str, introns: List[str]) -> str:
    for intron in introns:
        dna_sequence = dna_sequence.replace(intron, "")
    return dna_sequence


with open(os.path.join(os.getcwd(), "input/rosalind_splc.txt"), "r") as lines:
    key: int = ''
    nucleotide: str = ''
    sequence_content: Dict[str, str] = dict()

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

    sequences: List[str] = list(sequence_content.values())
    dna_sequence: str = remove_introns(sequences[0], sequences[1:])

    # starts: List[int] = index_of_first_start_codon(dna_sequence)

    protein: str = translate(dna_sequence)

    with open(os.path.join(os.getcwd(), "output/rosalind_splc.txt"), "w") as outs:
        outs.write(protein + "\n")