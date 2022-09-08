### lcsm.py
### Given a set of protein sequences, find the longest common substring (motif)

import os
import re
from typing import Set, List

def find_motif(sequences: Set[str]) -> str:
    lcs = ""
    # Go through each DNA sequence in the list.
    for i in range(len(sequences)):
        sequence = sequences[i]
        seq_length = len(sequence)
        # Iterate through all possible substrings.
        for index1 in range(seq_length+1):
            for index2 in range(index1, seq_length):
                test_seq = sequence[index1:index2+1]
                # print(f"index1 is {index1}, index2+1 is {index2+1}")
                matches_all_lines = False

                # Iterate through all other DNA sequences in the list and see if the current substring is found in all
                # of them.
                for test_line in range(i+1, len(sequences)):
                    comp_seq = sequences[test_line]
                    # comp_seq = comp_fasta.get_seq()
                    # print(test_seq, comp_seq, lcs)
                    x = re.search(test_seq, comp_seq)
                    # print(x)
                    if x is not None:
                        # print(test_seq, comp_seq)
                        matches_all_lines = True
                    else:
                        matches_all_lines = False
                        break
                if matches_all_lines is True and len(test_seq) >= len(lcs):
                    lcs = test_seq
    return lcs[::-1]

# TODO: Too slow

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

    longest_common_seq: str = find_motif(list(sequence_content))

    print(longest_common_seq)

    with open(os.path.join(os.getcwd(), "output/rosalind_lcsm.txt"), "w") as outs:
        outs.write(str(longest_common_seq))