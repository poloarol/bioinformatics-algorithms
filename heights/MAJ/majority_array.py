### majority_array.py
### Find the majority element of an array i.e. 
### One with more than half its elements being the same

import os
from typing import List, Dict

def majority_element(sequence: List[int]) -> int:
    """
    Find the majority element of an array
    :param sequence: A list of integers
    :return: The majority element of the array
    """

    data: Dict[int, int] = {}
   
    for element in sequence:
        if element not in data:
            data[element] = 1
        else:
            data[element] = data[element] + 1
    
    max_element: int = max(data, key=data.get)

    return -1 if data[max_element] <= (len(sequence)//2) else max_element


if __name__ == "__main__":

    with open(os.path.join(os.getcwd(), 'input/rosalind_maj.txt'), 'r') as lines:
        num_sequences, len_sequences = lines.readline().strip().split(" ")

        results: str = ""
        
        for line in lines:
            datum = list(map(int, line.strip("\n").split(" ")))
            # results = str(majority_element(datum))
            results = " ".join([results, str(majority_element(datum))]).strip()
    
    with open(os.path.join(os.getcwd(), 'output/rosalind_maj.txt'), 'w') as output:
        output.write(results)
