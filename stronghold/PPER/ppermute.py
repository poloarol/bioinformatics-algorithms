### ppermute.py
### Calculate all the partial permutations of P(n,r)

import os
import math

def partial_permutation(n: int, r: int) -> int:
    # numerator: int = math.factorial(n)
    # denominator: int = math.factorial(n-r)

    return int(math.factorial(n) / math.factorial(n-r)) % 1000000


if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), "input/rosalind_pper.txt"), "r") as lines:
        n, k = lines.readline().strip("\n").split(" ")
        pper: int = partial_permutation(int(n), int(k))

        with open(os.path.join(os.getcwd(), "output/rosalind_lower.txt"), "w") as outs:
            outs.write(str(pper))