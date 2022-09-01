
import pytest

from slice_string import slice_string

@pytest.mark.parametrize("string, a, b, c, d", [
    ("HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain", 22, 27, 97, 102)])
def test_slice_string(string: str, a: int, b: int, c: int, d: int):
    new_string: str = slice_string(string, a, b, c, d)
    assert new_string == "Humpty Dumpty"