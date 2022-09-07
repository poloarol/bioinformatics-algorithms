### merge_sort.py
### use merge sort to insert a list of unsorted elements into anothe list of sorted elements

import os
from typing import List

def merge_sort(sequence_one: List[int], len_one: int, sequence_two: List[int], len_two: int) -> List[int]:
    sequence: List[int] = [None] * (len_one + len_two)

    i, j, k = 0, 0, 0

    while i < len_one and j < len_two:
        if sequence_one[i] < sequence_two[j]:
            sequence[k] = sequence_one[i]
            k = k + 1
            i = i + 1
        else:
            sequence[k] = sequence_two[j]
            k = k + 1
            j = j + 1
 
    while i < len_one:
        sequence[k] = sequence_one[i]
        k = k + 1
        i = i + 1
 
    while j < len_two:
        sequence[k] = sequence_two[j]
        k = k + 1
        j = j + 1

    return sequence

if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), 'input/rosalind_mer.txt'), 'r') as lines:
        a = int(lines.readline().strip("\n"))
        array_one: List[int] = list(map(int, lines.readline().strip("\n").split(" ")))
        b = int(lines.readline().strip("\n"))
        array_two: List[int] = list(map(int, lines.readline().strip("\n").split(" ")))

        new_array: List[int] = merge_sort(array_one, a, array_two, b)

        with open(os.path.join(os.getcwd(), 'output/rosalind_mer.txt'), 'w') as outs:
            data: str = " ".join(str(x) for x in new_array).strip()
            outs.write(data)