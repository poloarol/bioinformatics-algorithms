### two_sum.py


import os

from typing import List

def two_sum(sequence: List[int]) -> List[int]:
    """
    Takes an array A and returns the two
    indices, if any, if the integer values
    stored at those indices sum to 0

    >>> two_sum([2 -3 4 10 5])
    [-1]
    >>> two_sum([8 2 4 -2 -8])
    [2, 4]
    """

    results: List[int] = []

    for i in range(len(sequence)):
        item: int = sequence[i]
        if -item in sequence[i+1:]:
           for j in range(i+1, len(sequence)):
                if (sequence[i] + sequence[j] == 0):
                    results.append([i+1, j+1])
    
    return results if results else [-1]

# TODO: Output is wrong

if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), 'input/rosalind_2sum.txt'), 'r') as lines:
        k, n = lines.readline().strip("\n").split(" ")
        data: List[List[int]] = []
        for line in lines:
            tmp: List[int] = two_sum(list(map(int, line.strip("\n").split(" "))))
            data.append(tmp)
        
        with open(os.path.join(os.getcwd(), 'output/rosalind_2sum.txt'), 'w') as outs:
            for i in range(len(data)):
                tmp: str = " ".join(str(x) for x in data[i]).strip()
                outs.write(tmp)