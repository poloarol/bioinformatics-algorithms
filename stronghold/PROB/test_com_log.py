

import pytest

from common_log import calc_common_log

@pytest.mark.parametrize("sequence, probabilities,expected", 
            [("ACGATACAA", [0.129, 0.287, 0.423, 0.476, 0.641, 0.742, 0.783], 
                    [-5.737, 5.217, -5.263, -5.360, -5.958, -6.628, -7.009])])
def test_calc_common_log(sequence, probabilities, expected):
    results = calc_common_log(sequence, probabilities)
    assert expected == results