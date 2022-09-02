### mendel.py
### Detemine the probability of choosing having dominant offspring


import pytest

from mendel import calc_probability_dominant

@pytest.mark.parametrize("dominant, heterozygous, recessive, expected", [(2, 2, 2, 0.78333)])
def test_calc_dominant_probability(dominant, heterozygous, recessive, expected):
    probability: float = calc_probability_dominant(dominant, heterozygous, recessive)

    assert round(probability, 5) == expected
