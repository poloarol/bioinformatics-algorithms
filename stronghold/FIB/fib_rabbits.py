

import os


def fib(num_rabbits: int, count: int) -> int:
    """
    Fibonacci Rabbits.

    Args:
        num_rabbits (int): Number of rounds.
        count (int): Number of rounds.

    Returns:
        int
    """
    
    if num_rabbits in {0, 1}:
        return 1

    a, b = 1, 1
    final_population: int
    
    for _ in range(2, num_rabbits):
        final_population = a + count * b
        a, b = final_population, a

    return final_population


with open(os.path.join(os.getcwd(), "input\\rosalind_fib.txt"), "r") as lines:
    for line in lines:
        line = line.strip()
        a, b = line.split(" ")

        with open(os.path.join(os.getcwd(), "output\\rosalind_fib.txt"), "a") as outs:
            results: int = fib(int(a), int(b))
            outs.write(f"{results}\n")