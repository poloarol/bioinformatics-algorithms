
import pytest

from square_hypothenus import calc_square_hypothenus

@pytest.mark.parametrize("test_base, test_height, test_hypothenus", [(3, 5, 34), (0, 0, 0)])
def test_square_hypothenus(test_base: float, test_height: float, test_hypothenus: float):
    hypothenus: float = calc_square_hypothenus(base=test_base, height=test_height)
    assert hypothenus == test_hypothenus
