### overlay_graph.py
### return adjacency list corresponding to k-edges

from distutils.command import build
import os
from typing import Dict

def build_overlay_graph(k: int, sequences: Dict[str, str]) -> None:
    with open(os.path.join(os.getcwd(), 'output/rosalind_grph.txt'), 'w') as outs:
        for key_one in sequences.keys():
            for key_two in sequences.keys():
                if sequences[key_one] != sequences[key_two]:
                    # check if sequences contain overlap
                    if sequences[key_one][-k:] == sequences[key_two][:k]:
                        # save just the sequence id's
                        outs.write(" ".join([key_one, key_two]) + "\n")
                else:
                    continue


if __name__ == "__main__":
    with open(os.path.join(os.getcwd(), "input/rosalind_grph.txt"), "r") as lines:
        key: int = ''
        nucleotide: str = ''
        sequence_content: Dict[str, str] = {}

        k: int = 3

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

        build_overlay_graph(k, sequence_content)

