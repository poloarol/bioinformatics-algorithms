
import pytest
from collections import defaultdict
from typing import List, Dict
from degree_array import build_graph
from double_degree import calculate_double_degree


input_data: str = """5 4
1 2
2 3
4 3
2 4"""

@pytest.mark.parametrize("input_data, results", [(input_data, "3 5 5 5 0")])
def test_build_graph(input_data, results):
    data: List = input_data.split("\n")
    g: Dict[str, List] = defaultdict(list)

    for i in range(1, len(data)):
        node1, node2 = data[i].strip('\n').split(" ")
        g = build_graph(g, int(node1), int(node2))
    
    max_key = max(g.keys())

    g = dict(sorted(g.items()))
    ddeg: str = calculate_double_degree(g)

    while max_key < int(data[0].split(" ")[0]):
        max_key = max_key + 1
        ddeg = " ".join([ddeg, "0"]).strip()
    
    vertices: int = 0
    # degrees: str = ""

    for key, value in g.items():
        # degrees = " ".join([degrees, str(len(value))]).strip()
        vertices = vertices + len(value)
    
    assert ddeg == results
    assert max_key == int(data[0].split(" ")[0])
    assert vertices/2 == int(data[0].strip('\n').split(" ")[1])
