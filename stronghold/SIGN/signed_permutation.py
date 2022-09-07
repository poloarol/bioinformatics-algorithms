### signed_permutation.py
### Goal to return number of and all signed permutations of length 'n'.
### This means, for example, that [1, -1] is not acceptable.

import os
import itertools

from typing import List

def signed_permutations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indicies in itertools.product(range(n), repeat=r):
        check = tuple(abs(pool[i]) for i in indicies)
        # set checks for duplicates of absolute values
        if len(set(check)) == r:
            yield tuple(pool[i] for i in indicies)


# TODO: Output is wrong, since order matters

if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), "input/rosalind_sign.txt"), "r") as lines:
        for line in lines:
            n: int = int(line.strip("\n").strip())
            sign_perms: List[int] = range(1, n+1) + range(-n, 0)

            perms = list(signed_permutations(sign_perms, r=n))

            with open(os.path.join(os.getcwd(), "output/rosalind_sign.txt"), "a") as outs:
                data = " ".join(str(x) for x in perms) + "\n"
                outs.write(data)