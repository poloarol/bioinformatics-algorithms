### double_degree.py
### Calculate the double degree of each node in a graph

import os
from collections import defaultdict
from typing import Dict, List
from degree_array import build_graph


def calculate_double_degree(graph: Dict[int, List]) -> str:
    """
    Calculate the double degree of each node in a graph
    :param graph:
    :return:
    """
    
    ddeg: Dict[int, int] = {k:0 for k in graph.keys()}
    for vertex in graph:
        for n in graph[vertex]:
            ddeg[vertex] = ddeg[vertex] + len(graph[n])
    
    results: str = ""

    for key, value in ddeg.items():
        results = " ".join([results, str(value)]).strip()
    
    return results

if __name__ == '__main__':
    g: Dict[str, List] = defaultdict(list)
    num_nodes: int
    num_edges: int

    with open(os.path.join(os.getcwd(), 'input/rosalind_ddeg.txt'), 'r') as lines:
        num_nodes, num_edges = lines.readline().strip().split(" ")
        for line in lines:
            node, node2 = line.strip("\n").split(" ")
            g = build_graph(g, int(node), int(node2))
    
    edges: int = 0
    degrees: str = ""

    g = dict(sorted(g.items()))
    double_degree = calculate_double_degree(g)

    max_key = max(g.keys())

    while max_key < int(num_nodes):
        max_key = max_key + 1
        double_degree = " ".join([double_degree, "0"]).strip()
    
    with open(os.path.join(os.getcwd(), "output/rosalind_ddeg.txt"), "w") as output:
        output.write(double_degree)