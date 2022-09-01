### count_words.py
### Count the occurence of words in a string

import os
from typing import Dict, List

def count_words(string: str) -> Dict:

    word_occurence: Dict = dict()
    words: List = string.split(" ")

    for word in words:
        if word not in word_occurence:
            word_occurence[word] = 1
        else:
            word_occurence[word] = word_occurence[word] + 1

    return word_occurence

if __name__ == "__main__":
    infile = os.path.join(os.getcwd(), 'input/rosalind_ini6.txt')
    outfile = os.path.join(os.getcwd(), 'output/rosalind_out6.txt')

    with open(infile, "r") as lines:
        for line in lines:
            results = count_words(line)

            with open(outfile, 'w') as outs:
                for word, occurence in results.items():
                    outs.write(f"{word} {occurence}\n")
