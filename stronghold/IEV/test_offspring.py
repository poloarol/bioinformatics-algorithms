
import pytest

from offspring import calc_expected_offspring


@pytest.mark.parametrize("input_data, expected", [([1, 0, 0, 1, 0, 1], 3.5)])
def test_calc_expected_offspring(input_data, expected):
    results: float = calc_expected_offspring(input_data)
    assert results == pytest.approx(expected)
