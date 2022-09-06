### mortal_fib.py
### Calculate the fibonacci rabbits after taking death into consideration


import os

def mortal_fib(rabbits: int, months: int) -> int:
    """
    Calculate the fibonacci rabbits after taking death into consideration
    :param rabbits: Number of rabbits
    :param months: Number of months the rabbits are alive
    :return: fibonacci rabbits after taking death into consideration
    """

    if rabbits == 0 or months == 1:
        return 0
    if rabbits == 1 or months == 2 or months == 2:
        return 1

    rabbit_pairs = [0, 1]

    for i in range(2, rabbits+1):
        if i <= months:
            # before rabbits die, the number of pairs is equal to the standard fibonacci number
            rabbit_pairs.append(rabbit_pairs[i - 1] + rabbit_pairs[i - 2])
        elif i == months + 1:
            # initial rabbit pair death
            rabbit_pairs.append(rabbit_pairs[i - 1] + rabbit_pairs[i - 2] - 1)
        else:
            # rabbits pairs are now F_n-1 + F_n-12 - F_n-(m+1)
            rabbit_pairs.append(rabbit_pairs[i - 1] + rabbit_pairs[i - 2] - rabbit_pairs[i - (months + 1)])
    return rabbit_pairs[rabbits]

if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), 'input\\rosalind_fibd.txt'), 'r') as lines:
        for line in lines:
            num_rabbits, num_months = line.strip("\n").split(" ")
            remaining_rabbits = mortal_fib(int(num_rabbits), int(num_months))

            with open(os.path.join(os.getcwd(), 'output\\rosalind_fibd.txt'), 'w') as outs:
                outs.write(f"{remaining_rabbits}\n")