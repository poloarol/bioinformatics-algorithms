
import os
import pytest

from majority_array import majority_element

path: str = os.path.join(os.getcwd(), "input/test.txt")

@pytest.mark.parametrize("path, expected", [(path, "5 7 -1 -1")])
def test_majority_element(path: str, expected: str):
    with open(path, 'r') as f:
        num_sequences, len_sequences = f.readline().strip("\n").split(" ")
        count: int = 0
        results: str = ""

        for line in f:
            datum = list(map(int, line.strip("\n").split(" ")))
            count += 1

            assert len(datum) == int(len_sequences)
            element = majority_element(datum)
            results = " ".join([results, str(element)]).strip()

        assert count == int(num_sequences)
        assert results == expected
