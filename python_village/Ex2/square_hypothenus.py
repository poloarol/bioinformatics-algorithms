### square_hypothenus.py 
### Calculates the squared value of the Hypothenus given the base and height

from genericpath import isfile
import os



def calc_square_hypothenus(base: float, height: float) -> float:
    base_square: float = base**2
    height_square: float = height**2
    hypothenus_square: float = base_square + height_square

    return hypothenus_square


if __name__ == "__main__":
    csv_file = os.path.join(os.getcwd(), 'input/rosalind_ini2.txt')

    if os.path.isfile(csv_file):
        with open(csv_file, 'r') as lines:
            for line in lines:
                base, height = line.split(" ")

                with open(os.path.join(os.getcwd(), "output/rosalind_out2.txt"), 'w') as outs:
                    hypothenus: float = calc_square_hypothenus(float(base), float(height))
                    outs.write(f"{hypothenus}\n")