### merge_sort.py
### use merge sort to insert a list of unsorted elements into anothe list of sorted elements

import os
from typing import List

def merge_sort(sequence: List[int]) -> List[int]:

    left: List[int]
    right: List[int]

    if len(sequence) > 1:
        mid: int = len(sequence)//2

        left, right = sequence[:mid], sequence[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sequence[k] = left[i]
                i += 1
            else:
                sequence[k] = right[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(left):
            sequence[k] = left[i]
            i += 1
            k += 1
  
        while j < len(right):
            sequence[k] = right[j]
            j += 1
            k += 1

    return sequence

if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), 'input/rosalind_mer.txt'), 'r') as lines:
        a = int(lines.readline().strip("\n"))
        sorted_array: List[int] = list(map(int, lines.readline().strip("\n").split(" ")))
        b = int(lines.readline().strip("\n"))
        unsorted_array: List[int] = list(map(int, lines.readline().strip("\n").split(" ")))

        for element in unsorted_array:
            sorted_array.append(element)
            sequence = merge_sort(sorted_array)

        with open(os.path.join(os.getcwd(), 'output/rosalind_mer.txt'), 'w') as outs:
            data: str = " ".join(sorted_array).strip()
            outs.write(data)