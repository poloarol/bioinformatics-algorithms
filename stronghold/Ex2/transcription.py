
### transcrition.py
### Convert a DNA sequence to an RNA sequence

import os

def transcribe(dna: str) -> str:
    """Convert a DNA sequence to an RNA sequence"""
    rna: str = ""
    if dna:
        tmp_dna: str = dna.upper().replace(" ", "")
        rna = tmp_dna.replace("T", "U")

    return rna


if __name__ == "__main__":
    with open(os.path.join(os.getcwd(), "input/rosalind_rna.txt"), "r") as lines:
        for line in lines:
            rna_seq: str = transcribe(line)

            with open(os.path.join(os.getcwd(), "output/rosalind_rna.txt"), "a") as out:
                out.write(f"{rna_seq}\n")