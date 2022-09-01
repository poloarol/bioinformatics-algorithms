### only_even_lines.py
### Extract all even lines from a file and write them to a new file

import os


def extract_even_lines(path_to_file: str) -> str:
    new_lines: str = ""
    with open(path_to_file, 'r') as lines:
        for count, line in enumerate(lines):
            if count % 2 != 0:
                new_lines = "".join([new_lines, line])

    return new_lines

if __name__ == "__main__":
    path: str = os.path.join(os.getcwd(), 'input/rosalind_ini5.txt')
    with open(os.path.join(os.getcwd(), "output/rosalind_out5.txt"), 'w') as outs:
        extracted_lines = extract_even_lines(path)

        for line in extracted_lines:
            outs.write(line)
