### common_log.py
### Calculate the common logarithm of the probability that a random string
### constructed with the GC-content found in a sequence

import os
import math
from typing import List

def calc_common_log(nuleotides:str, probs:List[float]) -> List[float]:

    probabilities: List[float] = []
    
    for prob in probs:
        probability: float = 1
        prob_gc: float = prob/2
        prob_at: float = (1-prob)/2

        for nt in nuleotides:
            if nt in ("A", "T"):
                probability = probability * prob_at
            else:
                probability = probability * prob_gc

        probabilities.append(round(math.log10(probability), 3))

    print(probabilities)
    
    return probabilities

### TODO: Test fails for some reason, but assignment was correct


with open(os.path.join(os.getcwd(), "input/rosalind_prob.txt"), "r") as lines:
    sequence: str = lines.readline().strip().strip("\n")
    seq_probs: List[float] = list(map(float, lines.readline().strip("\n").split(" ")))

    results: List[float] = calc_common_log(sequence, seq_probs)
    with open(os.path.join(os.getcwd(), "output/rosalind_prob.txt"), "w") as outs:
        outs.write(" ".join(str(x) for x in results))
