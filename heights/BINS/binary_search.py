### binary_search.py
### Given two integers a and b, a sorted array of integers and an unsorted array of integers
### find the index of each element in the unsorted array in the sorted array.

import os
from typing import List

def binary_search(target: int, sorted_array: List) -> str:
    """
    :param target: element to search for
    :param sorted_array: sorted array of integers

    :return:
      index of element else -1
    """

    start: int = 0
    end: int = len(sorted_array) - 1

    while(start <= end):
        mid: int = (start + end) // 2
        if sorted_array[mid] > target:
            end = mid - 1
        elif sorted_array[mid] < target:
            start = start + 1
        else:
            return mid + 1
    
    return -1


if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), 'input/rosalind_bins.txt'), 'r') as lines:
        len_a: int = int(lines.readline().strip())
        len_b: int = int(lines.readline().strip())
        sorted_array = list(map(int, lines.readline().strip().split(" ")))
        unsorted_array = list(map(int, lines.readline().strip().split(" ")))

        results: str = ""

        if len_a == len(sorted_array) and len_b == len(unsorted_array):
            for element in unsorted_array:
                res: str = str(binary_search(element, sorted_array))
                results = " ".join([results, res]).strip()
    
    with open(os.path.join(os.getcwd(), "output/rosalind_bins.txt"), "w") as output:
        output.write(results)