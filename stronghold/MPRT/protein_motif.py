### protein_motif.py
### Identify a protein motif in a given protein sequence

import os
import re
import urllib

from typing import Dict, List, Set
from urllib.request import urlopen


def motif_starts(motif, sequence: str) -> List[int]:
    if re.search(motif, sequence):
        location: List[int] = []
        for loc in re.finditer(motif, sequence):
            location.append(loc.start()+1)
        return location


if __name__ == "__main__":
    motif = re.compile('(?=N[^P][ST][^P])')
    motif_locations: Dict[str, List[int]] = {}
    with open(os.path.join(os.getcwd(), 'input/rosalind_mprt.txt'), "r") as lines:
        for line in lines:
            line = line.strip("\n").strip()
            accession: str
            if '_' in line:
                accession = line.split('_')[0]
            else:
                accession = line.strip("\n").strip()
            handle: str = f"http://www.uniprot.org/uniprot/{accession}.fasta"

            html = urlopen(handle)
            protein_seq: str = "".join(x.decode().strip().strip("\n") for x in html.readlines() if ">" not in x.decode())
            motif_locations[line.strip("\n")] = motif_starts(motif, protein_seq)

    results: str = ""
                
    with open(os.path.join(os.getcwd(), 'output/rosalind_mprt.txt'), "w") as outs:
        for key, value in motif_locations.items():
            if motif_locations[key]:
                results = results + "\n" + key
                tmp: str = " ".join(str(x) for x in value)
                results = results + "\n" + tmp
        
        outs.write(results.strip("\n"))






