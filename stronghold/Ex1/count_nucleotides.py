### count_nucleotides.py
### Given a DNA sequence, count the occurence of each nucleotide in the sequence

import os
from typing import Dict, Set

def count_nucleotides(sequence: str) -> Dict[str, int]:
    """
    Given a DNA sequence, count the occurence of each nucleotide in the sequence

    Parameters
    ----------
    sequence: str
        A DNA sequence

    Returns
    -------
    Dict[str, int]

    """

    sequence = sequence.replace(' ', '')
    nt_set: Set[str] = ("A", "G", "C", "T")
    nucleotides: Dict[str, int] = {"A": 0, "C": 0, "G": 0, "T": 0}

    for nt in sequence:
        if nt in nt_set:
            if "A" == nt:
                nucleotides["A"] += 1
            elif "C" == nt:
                nucleotides["C"] += 1
            elif "G" == nt:
                nucleotides["G"] += 1
            elif "T" == nt:
                nucleotides["T"] += 1
        # else:
            # raise ValueError("Non-Nucleotide character found in sequence")
    return nucleotides


if __name__ == "__main__":
    with open(os.path.join(os.getcwd(), "input/rosalind_dna.txt"), "r") as lines:
        for line in lines:
            nt_counts: Dict[str, int] = count_nucleotides(line)

            with open(os.path.join(os.getcwd(), "output/rosalind_dna.txt"), "a") as outs:
                out_line: str = "{0} {1} {2} {3}".format(nt_counts["A"], nt_counts["C"], nt_counts["G"], nt_counts["T"])
                outs.write(f"{out_line}\n")


