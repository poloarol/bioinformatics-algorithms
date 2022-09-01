### summation.py
### Calculate the sum of all intergers between between a and b inclusively
### a < b < 10000

import os
from typing import List


def sum_all_integers(number: float) -> int:
    """ Calculates the sum of all integers between 0 and number """

    my_sum: float = sum([x for x in range(0, number) if x % 2 != 0])
    return my_sum


def summation(first_number: float, second_number: float) -> int:

    first_sum: float = sum_all_integers(first_number)
    second_sum: float = sum_all_integers(second_number+1)
    adjusted_sum: float = second_sum - first_sum

    return adjusted_sum

if __name__ == "__main__":
    with open(os.path.join(os.getcwd(), "input/rosalind_ini4.txt"), 'r') as lines:
        for line in lines:
            smallest, largest = line.split(" ")
            odd_number_sum: str = summation(int(smallest), int(largest))

            with open(os.path.join(os.getcwd(), "output/rosalind_out4.txt"), 'w') as out:
                out.write(f"{odd_number_sum}\n")