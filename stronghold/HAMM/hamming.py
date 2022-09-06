### hamming.py
### Calculate the hamming distance between two strings
### https://en.wikipedia.org/wiki/Hamming_distance


import os

def hamming_distance(string_one, string_two) -> int:
    """
    Calculate the hamming distance between two strings
    :param string_one: first string
    :param string_two: second string
    :return: hamming distance
    """
    
    if len(string_one) != len(string_two):
        return "Cannot be calculated"
    
    if len(string_one) == 0 or len(string_two) == 0:
        return "Cannot be calculated"
    
    hamming: int = 0

    for char_one, char_two in zip(string_one, string_two):
        if char_one != char_two:
            hamming += 1

    return hamming


if __name__ == "__main__":
    with open(os.path.join(os.getcwd(), "input/rosalind_hamm.txt"), "r") as lines:
        for line in lines:
            sequence_one, sequence_two = line.strip().split(" ")
            ham_dist: int = hamming_distance(sequence_one, sequence_two)

            with open(os.path.join(os.getcwd(), "output/rosalind_hamm.txt"), "a") as outs:
                outs.write(f"{ham_dist}\n")
