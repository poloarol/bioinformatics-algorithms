### lexico.py
### Given a string of n-characters, sort them lexicographically

import os
import itertools
from typing import List

def permute(sequence: List, k:int) -> List[str]:
    alphabet = dict(zip(sequence, range(len(sequence))))
    all_permutations: List[str] = list(itertools.product(sequence, repeat=k))

    for permutation in all_permutations:
        for j in range(k+1):
            if permutation[:j] not in all_permutations:
                all_permutations.append(permutation[:j])
    
    all_permutations = list(filter(None, all_permutations))

    perms: List[str] = []

    for permutation in all_permutations:
        perms.append("".join(x for x in permutation))

    return sorted(perms, key=lambda j: [alphabet[i] for i in j])


if __name__ == "__main__":
    with open(os.path.join(os.getcwd(), "input/rosalind_lexv.txt"), "r") as lines:
        # seq: str = lines.readline().strip(" ").strip("\n")
        # k: int = int(lines.readline().strip("").strip("\n"))

        seq: str = "VNSXAZJHUWOK"
        k: int = 4

        perms: List[str] = permute(seq, k)

        with open(os.path.join(os.getcwd(), "output/rosalind_lexv.txt"), "w") as outs:
            outs.write("\n".join(x for x in perms))