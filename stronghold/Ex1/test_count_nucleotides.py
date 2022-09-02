

import pytest

from count_nucleotides import count_nucleotides


@pytest.mark.parametrize("nucleotides, count", 
            [("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC", "20 12 17 21")])
def test_count_nucleotides(nucleotides, count):
    nt_counts = count_nucleotides(nucleotides)
    results: str = "{0} {1} {2} {3}".format(nt_counts["A"], nt_counts["C"], nt_counts["G"], nt_counts["T"])

    assert results == count