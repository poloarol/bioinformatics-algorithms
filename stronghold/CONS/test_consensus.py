
import os
import pytest

from consensus import create_matrix, create_profile_matrix, get_consensus

path: str = os.path.join(os.getcwd(), 'input/test.txt')

matrix: str = """ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6"""

@pytest.mark.parametrize("path, matrix", [(path, matrix)])
def test_building_consensus(path: str, matrix: str):
    first_matrix = create_matrix(path)
    second_matrix = create_profile_matrix(first_matrix)
    consensus_seq = get_consensus(second_matrix)

    final_matrix: str = f"{consensus_seq}\n"

    for seq in second_matrix:
        final_matrix = final_matrix + " ".join(x for x in seq) + "\n"
    
    assert(final_matrix.strip("\n") == matrix)