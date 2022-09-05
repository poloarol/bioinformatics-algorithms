### fib.py
### Calculate the fibonacci coefficient of a number

import math
import argparse

# fibonacci coefficient
def fib_recursive(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


# fibonacci coefficient
def fib_binet(n: int) -> int:
    numerator: float = (1 + math.sqrt(5))**n - (1 - math.sqrt(5))**n
    denominator: float = (2**n) * math.sqrt(5)

    return int(numerator // denominator)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, required=True)
    parser.add_argument('--method', type=str, default='recursive', choices=['binet', 'recursive'])
    args = parser.parse_args()

    results: int

    if args.method == 'recursive':
        results = fib_recursive(args.n)
    if args.method == 'binet':
        results = fib_binet(args.n)

    print(results)