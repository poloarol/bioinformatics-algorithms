### insertion_sort.py
### insert an element into an list and sort it

import os
from typing import List

def insertion_sort(sequence: List[int]) -> List[int]:
    count: int = 0

    for i in range(1, len(sequence)):
        k_element = sequence[i]
        j = i - 1

        while j >= 0 and k_element < sequence[j]:
            sequence[j+1] =sequence[j]
            j -= 1

            count = count + 1
        
        sequence[j+1] = k_element
    
    return count

if __name__ == '__main__':
    num_swaps: int
    with open(os.path.join(os.getcwd(), 'input/rosalind_ins.txt'), 'r') as lines:
        len_sequence: int = int(lines.readline().strip())
        data: List = list(map(int, lines.readline().strip().split(" ")))
        num_swaps = insertion_sort(data)
    
    with open(os.path.join(os.getcwd(), 'output/rosalind_ins.txt'), 'w') as output:
        output.write(str(num_swaps))