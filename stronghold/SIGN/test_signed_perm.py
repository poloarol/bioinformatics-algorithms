

import pytest
from typing import List
from signed_permutation import signed_permutations

expected: str = """8
-1 -2
-1 2
1 -2
1 2
-2 -1
-2 1
2 -1
2 1"""

@pytest.mark.parametrize("data, expected", [(2, expected)])
def test_signed_perm(data, expected):
    sign_perms: List[int] = [x for x in range(1, data+1)] + [x for x in range(-data, 0)]
    perms = list(signed_permutations(sign_perms, r=2))

    results = f"{len(perms)}"
    perms.sort(key=lambda x: sum(x) and x[0])
    
    for perm in perms:
        tmp = " ".join(str(x) for x in perm)
        results = "\n".join([results, tmp])

    print(results)

    assert expected == results.strip("\n").strip()
