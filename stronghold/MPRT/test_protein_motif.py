
import re
import pytest
from typing import Dict, List
from urllib.request import urlopen
from protein_motif import motif_starts

accessions: str ="""A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST"""

expected: str = """B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614"""

@pytest.mark.parametrize("accessions, expected", [(accessions, expected)])
def test_protein_motif(accessions, expected):
    motif = re.compile('(?=N[^P][ST][^P])')
    motif_locations: Dict[str, List[int]] = {}
    for line in accessions.split("\n"):
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

    for key, value in motif_locations.items():
        if motif_locations[key]:
            results = results + "\n" + key
            tmp: str = " ".join(str(x) for x in value)
            results = results + "\n" + tmp
    
    assert expected == results.strip("\n")


    