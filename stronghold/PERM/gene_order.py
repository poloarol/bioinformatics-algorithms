### gene_order.py
### Enumerate all permutations a set of genes can have

import os
import math
from typing import List

def permutations(data: List[int]) -> List[List[int]]:
 
    # If lst is empty then there are no permutations
    if len(data) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(data) == 1:
        return [data]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(data)):
       m = data[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = data[:i] + data[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutations(remLst):
           l.append([m] + p)
    return l

def find_permutations(genes: int) -> List[List[int]]:

    family: List[int] = [gene+1 for gene in range(genes)]
    all_list: List[List[int]] = permutations(family)

    results: str = f"{math.factorial(genes)}"
    for a in all_list:
        tmp = " ".join(str(x) for x in a)
        results = "\n".join([results, tmp])

    return results


with open(os.path.join(os.getcwd(), "input/rosalind_perm.txt"), "r") as lines:
    for line in lines:
        data: str = find_permutations(int(line.strip("\n").strip()))

        with open(os.path.join(os.getcwd(), "output/rosalind_perm.txt"), "w") as outs:
            outs.write(data)