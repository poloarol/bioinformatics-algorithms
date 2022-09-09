
import pytest
from collections import defaultdict
from typing import Dict, List

from bfs import build_graph
from bfs import bfs

data: str = """6 6
4 6
6 5
4 3
3 5
2 1
1 4"""

@pytest.mark.parametrize("data, num_nodes, num_edges, expected", [(data, 6, 6, "0 -1 2 1 3 2")])
def test_bfs(data, num_nodes, num_edges, expected):
    data = data.split("\n")
    g: Dict[str, List] = defaultdict(list)

    for i in range(1, len(data)):
        node1, node2 = data[i].strip("\n").split(" ")
        g = build_graph(g, int(node1), int(node2))
    
    g = dict(sorted(g.items()))
    results: List[int] = bfs(g)

    edges: int = 0
    all_nodes: List[int] = set()

    for node, value in g.items():
        all_nodes.add(node)
        all_nodes.update(g[node])
        edges = edges + len(value)

    assert expected == " ".join(str(x) for x in results)
    assert len(all_nodes) == num_nodes
    assert edges == num_edges