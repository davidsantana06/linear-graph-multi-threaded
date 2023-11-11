from typing import Dict, List
from random import randint, uniform
import json


class LinearGraphGenerator:
    def __init__(self, paths: int, min_edges: int, max_edges: int, min_distance: int, max_distance: int):
        self.paths = paths
        self.min_edges = min_edges
        self.max_edges = max_edges
        self.min_distance = min_distance
        self.max_distance = max_distance

    def generate_linear_path(self) -> List[Dict[str, object]]:
        return [
            {
                'node': i + 1,
                'distance': uniform(self.min_distance, self.max_distance)
            }
            for i in range(randint(self.min_edges, self.max_edges))
        ]

    def generate_graph(self, output_file: str) -> None:
        with open(output_file, 'w') as graph_file:
            json.dump(
                {'paths': [self.generate_linear_path() for _ in range(self.paths)]},
                graph_file, indent=4
            )
