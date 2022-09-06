### offspring.py
### Calculate the number of Expected Offspring

import os

from typing import List

def calc_expected_offspring(probabilities: List[int]) -> float:
    """
    Calculate the number of Expected Offspring expressing the dominant phenotype
    :param probailities:
    :return: expected_number
    """

    expected_number: float = 0
    prob_offspring: List[float] = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]

    for i in range(len(probabilities)):
        expected_number = expected_number + (prob_offspring[i] * probabilities[i])
    
    return 2*expected_number


if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), "input/rosalind_iev.txt"), "r") as lines:
        for line in lines:
            data: List[int] = [int(x) for x in line.strip("\n").split(" ")]
            results: float = calc_expected_offspring(data)

            with open(os.path.join(os.getcwd(), "output/rosalind_iev.txt"), "a") as outs:
                outs.write(str(results) + "\n")
