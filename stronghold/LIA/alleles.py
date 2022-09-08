### alleles.py
### Assuming independent allele's according to Mendel's Second Law,
### What is the probability there will be at least 'N' AaBb organisms
### after 'k' generations (just final, not including parents)?
### k - how many generations to pass
### N - how many AaBb organisms in final generation

import os
import math
from typing import List

def probability_heterozygous(k: int, N: int) -> float:
    hetero_prob: float = 4/16
    probabilities: List[float] = []
    total = 2**k
    # summation of your general binomial probability function
    for r in range(N,(total+1)):
        probabilities.append(nCr(total,r)*(hetero_prob**r)*((1-hetero_prob)**(total-r)))

    return round(sum(probabilities), 3)


# quick combinatorial function
def nCr(n,r):
    return math.factorial(n) / math.factorial(r) / math.factorial(n-r)


if __name__ == '__main__':
    # print(probability_heterozygous(2,1)) # Test provided

    with open(os.path.join(os.getcwd(), 'input/rosalind_lia.txt'), 'r') as lines:
        num_generatons, num_organisms = lines.readline().strip().strip('\n').split(" ")

        with open(os.path.join(os.getcwd(), 'output/rosalind_lia.txt'), 'w') as outs:
            results: float = probability_heterozygous(int(num_generatons), int(num_organisms))
            outs.write(str(results))
