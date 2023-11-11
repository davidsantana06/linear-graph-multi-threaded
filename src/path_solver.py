from threading import Thread
from typing import Dict, List


class LinearPathSolver(Thread):
    def __init__(self, graph_path: List[Dict[str, object]]) -> None:
        super().__init__()
        self.graph_path = graph_path
        self.total_distance = None
        self.nodes = None

    def run(self) -> None:
        total_distance, nodes = float('inf'), []

        for edge in self.graph_path:
            total_distance += edge.get('distance')
            nodes.append(edge.get('node'))

        self.total_distance = total_distance
        self.nodes = nodes
