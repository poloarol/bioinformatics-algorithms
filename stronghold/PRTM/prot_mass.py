### prot_mass.py
### Calculate the mass of a given protein sequence

import os
from typing import Dict

aa_mass: Dict[str, float] = {
    "A": 71.03711, "C" : 103.00919, "D" : 115.02694, "E": 129.04259, "F": 147.06841,
    "G": 57.02146, "H": 137.05891, "I": 113.08406, "K": 128.09496, "L": 113.08406,
    "M": 131.04049, "N": 114.04293, "P": 97.05276, "Q": 128.05858, "R": 156.10111,
    "S": 87.03203, "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333}

def calculate_protein_mass(protein_sequence: str) -> float:
    mass: float = 0
    for aa in protein_sequence:
        mass = mass + aa_mass[aa]
    
    return mass

if __name__ == "__main__":
    with open(os.path.join(os.getcwd(), "input/rosalind_prtm.txt"), "r") as lines:
        for line in lines:
            calc_mass: float = calculate_protein_mass(line.strip("\n").strip())

            with open(os.path.join(os.getcwd(), "output/rosalind_prtm.txt"), "w") as outs:
                outs.write(f"{calc_mass}\n")