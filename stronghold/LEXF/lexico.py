### lexico.py
### Enumerate all genes by lexicographic order

import os
import itertools

from typing import List


with open(os.path.join(os.getcwd(), "input/rosalind_lexf.txt"), "r") as lines:
    sequence: List[str] = list(lines.readline().strip("\n").split(" "))
    k = int(lines.readline().strip("\n"))

    permutations: List[str] = itertools.product(sequence, repeat=k)

    with open(os.path.join(os.getcwd(), "output/rosalind_lexf.txt"), "w") as outs:
        data: List[str] = []

        for permutation in permutations:
            data.append("".join(x for x in permutation))
        
        data = sorted(data, key=str.upper)

        for datum in data:
            outs.write(datum + "\n")