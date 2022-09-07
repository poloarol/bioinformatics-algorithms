
import os
import pytest

from only_even_lines import extract_even_lines

in_file = os.path.join(os.getcwd(), 'input\\test_input.txt')
out_file = os.path.join(os.getcwd(), 'output\\test_output.txt')

@pytest.mark.parametrize("file, result_file", [(in_file, out_file)])
def test_extract_even_lines(file, result_file):
    result: str = ""
    even_lines: str = extract_even_lines(in_file)
    with open(result_file, 'r') as lines:
        result = "".join([line for line in lines])
    
    assert even_lines == result
        

