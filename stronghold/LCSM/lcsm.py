### lcsm.py
### Given a set of protein sequences, find the longest common substring (motif)

import os
from typing import Set, List

def find_motif(shortest_sequence: str, sequences: Set[str]) -> str:
    """
    Given a set of protein sequences, find the longest common substring (motif)
    :param seq_one:
    :param sequences:
    :return: motif(str)
    """

    lcs: str = ""
    print(shortest_sequence)

    for start in range(len(shortest_sequence)):
        for end in range(len(shortest_sequence), start, -1):
            if len(shortest_sequence[start:end]) > len(lcs):
                matches: List[bool] = []
                for sequence in sequences:
                    if shortest_sequence[start:end] in sequence:
                        matches.append(True)
                    else:
                        matches.append(False)
                if all(matches):
                    lcs = shortest_sequence[start:end]
            else:
                break
    return lcs

# TODO: Output is wrong. Needs revisiting

if __name__ == "__main__":
    sequence_content: Set[str] = set()
    with open(os.path.join(os.getcwd(), 'input/rosalind_lcsm.txt'), "r") as lines:
        key: str = ''
        nucleotide: str = ''
        for line in lines:
            if line.startswith('>'):
                if key:
                    sequence_content.add(nucleotide)
                    key = line.strip('\n').replace('>','')
                    nucleotide = ""
                else:
                    key = line.strip('\n').replace('>','')
            else:
                nucleotide = ''.join([nucleotide, line])
        sequence_content.add(nucleotide.replace('\n', '')) # add last key, value pair
    
    shortest_sequence = min(sequence_content, key=len)
    sequence_content.remove(shortest_sequence)

    longest_common_seq: str = find_motif(shortest_sequence, sequence_content)

    print(longest_common_seq)

    with open(os.path.join(os.getcwd(), "output/rosalind_lcsm.txt"), "w") as outs:
        outs.write(str(longest_common_seq))