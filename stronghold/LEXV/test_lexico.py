

import pytest

from lexico import permute

expected_results = """D
DD
DDD
DDN
DDA
DN
DND
DNN
DNA
DA
DAD
DAN
DAA
N
ND
NDD
NDN
NDA
NN
NND
NNN
NNA
NA
NAD
NAN
NAA
A
AD
ADD
ADN
ADA
AN
AND
ANN
ANA
AA
AAD
AAN
AAA"""

@pytest.mark.parametrize("seq, k, expected", [("DNA", 3, expected_results)])
def test_permute(seq, k, expected):
    results = permute(seq, k)
    assert results == expected.split("\n")