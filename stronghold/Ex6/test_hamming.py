
import pytest

from hamming import hamming_distance


@pytest.mark.parametrize('sequence_one, sequence_two, distance', 
                    [("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT", 7)])
def test_hamming_distance(sequence_one, sequence_two, distance):
    assert hamming_distance(sequence_one, sequence_two) == distance