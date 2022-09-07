### connected_components.py
### Find the number of connected components in a given undirected graph

import os
from collections import defaultdict
from typing import Dict, List, Set

def build_graph(graph: Dict, node_one: int, node_two: int) -> Dict:
    graph[node_one].append(node_two)
    graph[node_two].append(node_one)

    return graph

def dfs(graph: Dict, node: int, visited: Set = set()):
    pass

def find_cc(graph: Dict) -> int:
    pass