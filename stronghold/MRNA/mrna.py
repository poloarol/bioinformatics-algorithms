### mrna.py
###
###
###
### Goal to return number of possible mRNA strings which could have translated
### the given protein, modulo 1000000.
### This approach creates a new codon table with counts of possible rna/dna
### sequences. Since we are not actually going to back translate, the specific table
### is unneccesary and one can just use the generic codon table from Biopython.


import os
import math

from typing import List

codons = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
CAA Q      AAA K      GAA E      CAG Q      
AAG K      GAG E      UGU C      CGU R      
AGU S      GGU G      UGC C      CGC R      
AGC S      GGC G      CGA R      AGA R      
GGA G      UGG W      CGG R      AGG R      
GGG G"""

trans = codons.split()
table = dict(zip(trans[0::2], trans[1::2]))

def get_rna(x):                                                              # return all possible RNA of each protein
    return len([key for key, value in table.items() if x in value])

if __name__ == "__main__":
    with open(os.path.join(os.getcwd(), "input/rosalind_mrna.txt"), "r") as lines:
        count: List[float] = []
        for line in lines:
            amino_acids: str = line.strip("\n").strip("")

            for aa in amino_acids:
                count.append(get_rna(aa))
            
        num_rna: float = 3*math.prod(count)%1000000


        with open(os.path.join(os.getcwd(), "output/rosalind_mrna.txt"), "w") as outs:
            outs.write(str(num_rna))
        
