

import pytest
from typing import Dict
from count_words import count_words

reference: str = "We tried list and we tried dicts also we tried Zen"
ref_results: Dict = {"and": 1, "We": 1, "tried": 3, "dicts": 1, "list": 1, "we": 2, "also": 1, "Zen": 1}

@pytest.mark.parametrize("string, results", [(reference, ref_results)])
def test_count_words(string, results):
    result_dictionary: Dict = count_words(string)
    assert results == result_dictionary