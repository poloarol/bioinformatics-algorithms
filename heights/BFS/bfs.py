### bfs.py
### Given a directed graph, perform breath-first search to identify 
### the shortes path from vertes 1 to all other vertices.

import os
from typing import Dict, List, Set
from collections import defaultdict

def build_graph(graph: Dict[int, List[int]], node1: int, node2:int) -> Dict[int, List[int]]:
    """
    """

    graph[node1].append(node2)
    return graph

def bfs(graph: Dict[int, List[int]]) -> List[int]:
    """
    """

    nodes: List[int] = len(graph.keys()) + 1
    # All min_dist set at -1 unless possible to reach
    min_dist = [0] + [-1]*(nodes-1)

    vertices: List[int] = list(range(2, nodes+1))
    queue: List[int] = [1]

    while queue:
        # check all connections for current node
        current: int = queue.pop(0)
        if current in graph:
            edges: List[int] = graph[current]
            for edge in edges:
                # check if edge hasn't been discovered yet
                if edge in vertices:
                    # add new edge
                    queue.append(edge)
                    # discard edge that has been visited
                    vertices.remove(edge)
                    # Rosalind is 1-based indexing
                    min_dist[edge-1] = min_dist[current-1] + 1
    return min_dist

### TODO: Test set work, but fails on given data. Need revisiting

with open(os.path.join(os.getcwd(), 'input/rosalind_bfs.txt'), 'r') as lines:
    g: Dict[int, List] = defaultdict(list)
    number_nodes, number_edges =  lines.readline().strip().split(" ")
    
    for line in lines:
        entry_node, exit_node = line.strip("\n").split(" ")
        g = build_graph(g, int(entry_node), int(exit_node))
    
    edges: int = 0
    nodes: Set = set()
    distances: List[int] = bfs(g)

    for key, value in g.items():
        edges = edges + len(value)
        nodes.add(key)
        nodes.update(value)
    
    print(number_nodes, len(nodes), number_edges, edges)

    # g = dict(sorted(g.items()))
    distances = bfs(g)

    with open(os.path.join(os.getcwd(), 'output/rosalind_bfs.txt'), 'w') as outs:
        results: str = " ".join(str(x) for x in distances)
        outs.write(results.strip() + "\n")