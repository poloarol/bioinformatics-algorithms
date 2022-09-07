### slice_string.py
### Subset part of a string given 4 integers (a, b, c, d)

import os

def slice_string(string: str, index_1: int, index_2: int, index_3: int, index_4: int) -> str:
    first: str = string[index_1:index_2+1]
    second: str = string[index_3:index_4+1]

    return f"{first} {second}"

if __name__ == "__main__":
    with open(os.path.join(os.getcwd(), "input/rosalind_ini3.txt"), 'r') as lines:
        for line in lines:
            strg, index1, index2, index3, index4 = line.split(" ")
            if " " in line:
                strg = strg.replace(" ", "")
            if len(strg) <= 200:
                new_string: str = slice_string(strg, int(index1), int(index2), int(index3), int(index4))

                with open(os.path.join(os.getcwd(), "output/rosalind_out3.txt"), 'w') as out:
                    out.write(new_string)
