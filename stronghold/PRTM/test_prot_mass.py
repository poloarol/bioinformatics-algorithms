
import pytest

from prot_mass import calculate_protein_mass

@pytest.mark.parametrize("sequence, expected", [("SKADYEK", 821.392)])
def test_calculate_protein_mass(sequence, expected):
    mass: float = calculate_protein_mass(sequence)
    assert mass == pytest.approx(expected)