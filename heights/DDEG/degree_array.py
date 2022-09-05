### degree_array.py
### Determine the degree of each node in a graph

import os
from collections import defaultdict
from typing import Dict, List

def build_graph(graph, node1, node2):
    graph[node1].append(node2)
    graph[node2].append(node1)

    return graph


# TODO: Output is wront. Check again later

if __name__ == '__main__':
    g: Dict[str, List] = defaultdict(list)
    num_nodes: int
    num_edges: int

    with open(os.path.join(os.getcwd(), 'input/rosalind_deg.txt'), 'r') as lines:
        num_nodes, num_edges = lines.readline().strip().split(" ")
        for line in lines:
            node, node2 = line.strip("\n").split(" ")
            g = build_graph(g, int(node), int(node2))
    
    edges: int = 0
    degrees: str = ""

    g = dict(sorted(g.items()))


    with open(os.path.join(os.getcwd(), 'output/rosalind_deg.txt'), 'w') as outs:
        for key, value in g.items():
            degrees = " ".join([degrees, str(len(value))]).strip()
            edges = edges + len(value)
        
        outs.write(degrees)

    print(num_nodes, num_edges, len(g.keys()), edges//2) 