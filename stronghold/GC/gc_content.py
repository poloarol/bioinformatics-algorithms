### gc.py
### Calculate the GC content of a DNA/RNA sequence

import os

from typing import Dict

def calculate_gc_content(sequence: str) -> float:
    """
    Calculate the GC content of a DNA/RNA sequence

    Parameters
    ----------
    dna_sequence : str
        DNA sequence

    Returns
    -------
    float
        GC content
    """
    # gc: int = 0
    # total: int = 0
    # for nt in sequence:
    #     if nt in ("G", "C"):
    #         gc += 1
    #     total += 1


    sequence = sequence.upper().replace(' ','')
    count_gc: int = sequence.count("G") + sequence.count("C")
    atgc: int = sequence.count("A") + sequence.count("T") + count_gc
    return ((count_gc/atgc) *100)


if __name__ == "__main__":
    sequence_content: Dict[str, float] = {}
    with open(os.path.join(os.getcwd(), 'input/rosalind_gc.txt'), "r") as lines:
        key: str = ''
        nucleotide: str = ''
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
        sequence_content[key] = nucleotide.replace('\n', '') # add last key, value pair
    
    for key, value in sequence_content.items():
        sequence_content[key] = calculate_gc_content(value)
    

    highest_gc: str = max(sequence_content, key=sequence_content.get)

    with open(os.path.join(os.getcwd(), 'output/rosalind_gc.txt'), 'w') as outs:
        outs.write(f"{highest_gc}\n{sequence_content[highest_gc]: .6f}")
