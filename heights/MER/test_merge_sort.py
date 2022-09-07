

import pytest

from merge_sort import merge_sort

@pytest.mark.parametrize("unsorted_array, unsorted_len, sorted_array, sorted_len, result",
                [([2, 4, 10, 18], 4, [-5, 11, 12], 3, [-5, 2 ,4, 10, 11, 12, 18])])
def test_merge_sort(sorted_array, sorted_len, unsorted_array, unsorted_len, result):
    assert len(sorted_array) == sorted_len
    assert len(unsorted_array) == unsorted_len

    # for element in unsorted_array:
    #     sorted_array.append(element)
    #     sorted_array = merge_sort(sorted_array)

    new_array = merge_sort(unsorted_array, unsorted_len, sorted_array, sorted_len)
    
    assert new_array == result

