### find_motif.py
### Find the beginning of a sequence motif in a string. (Substring == Motif)


import os

def find_motif(sequence: str, motif: str) -> str:
    """
    Find the beginning of a sequence motif in a string.

    Args:
        sequence (str): The string to be searched.
        motif (str): The substring to find.

    Returns:
        str: The beginning of the sequence motif 
    """

    ln_motif = len(motif)
    starts: str = ""
    for i in range(0, (len(sequence)-ln_motif+1)):
        if sequence[i:i+ln_motif] == motif:
            starts = " ".join([starts, str(i+1)])
    
    return starts.rstrip().lstrip()


with open(os.path.join(os.getcwd(), 'input/rosalind_subs.txt'), 'r') as lines:
    for line in lines:
        sequence, motif = line.split(' ')

        motif = motif.rstrip("").upper().replace(' ', '').strip("\n")
        sequence = sequence.rstrip("").upper().replace(' ', '')

        starts = find_motif(sequence, motif)

        with open(os.path.join(os.getcwd(), 'output/rosalind_subs.txt'), 'w') as outs:
            outs.write(starts + '\n')

