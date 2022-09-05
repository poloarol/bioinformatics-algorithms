
import pytest
from typing import List, Dict, Set
from collections import defaultdict
from degree_array import build_graph

input_data: str = """6 7
1 2
2 3
6 3
5 6
2 5
2 4
4 1"""

@pytest.mark.parametrize("input_data, results", [(input_data, "2 4 2 2 2 2")])
def test_build_graph(input_data, results):
    data: List = input_data.split("\n")
    g: Dict[str, List] = defaultdict(list)

    for i in range(1, len(data)):
        node1, node2 = data[i].strip('\n').split(" ")
        g = build_graph(g, node1, node2)
    
    dict(sorted(g.items()))
    
    vertices: int = 0
    degrees: str = ""

    for key, value in g.items():
        degrees = " ".join([degrees, str(len(value))]).strip()
        vertices = vertices + len(value)
    
    assert degrees == results
    assert len(g.keys()) == int(data[0].split(" ")[0])
    assert vertices/2 == int(data[0].strip('\n').split(" ")[1])
