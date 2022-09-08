

import pytest
from typing import Set, List
from signed_permutation import signed_permutations

expected: Set[int] = {(-1,-2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)}

@pytest.mark.parametrize("data, expected", [(2, expected)])
def test_signed_perm(data, expected):
    sign_perms: List[int] = [x for x in range(1, data+1)] + [x for x in range(-data, 0)]
    perms = set(signed_permutations(sign_perms, r=2))

    assert expected == perms
    assert len(expected) == len(perms)
