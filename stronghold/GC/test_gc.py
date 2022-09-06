
import os
import pytest

from typing import Dict
from gc_content import calculate_gc_content


path: str = os.path.join(os.getcwd(), 'input/test.txt')

@pytest.mark.parametrize('path, expected', [(path, "Rosalind_0808 60.919540")])
def test_calculate_gc_content(path, expected):
    sequence_content: Dict[str, float] = {}
    with open(path, 'r') as lines:
        key: str = ''
        nucleotide: str = ''
        for line in lines:
            if line.startswith('>'):
                if key:
                    sequence_content[key] = nucleotide.replace('\n', '')
                    key = line.strip('\n').replace('>','')
                    nucleotide = ""
                else:
                    key = line.strip('\n').replace('>','')
            else:
                nucleotide = ''.join([nucleotide, line])
        sequence_content[key] = nucleotide.replace('\n', '') # add last key, value pair
    
    for key, value in sequence_content.items():
        sequence_content[key] = calculate_gc_content(value)

    highest_gc: str = max(sequence_content, key=sequence_content.get)

    assert f"{highest_gc}{sequence_content[highest_gc]: .6f}" == expected

