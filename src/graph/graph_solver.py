from typing import Dict, List
import json

from .path_solver import LinearPathSolver


class LinearGraphSolver:
    def __init__(self, graph_file: str) -> None:
        self.path_solvers = self.prepare_path_solvers(graph_file)

    def prepare_path_solvers(self, graph_file: str) -> List[LinearPathSolver]:
        with open(graph_file, 'r') as g_file:
            graph: Dict[str, object] = json.load(g_file)

        return [
            LinearPathSolver(graph_path)
            for graph_path in graph.get('paths')
        ]

    def solve_graph(self, output_file: str) -> None:
        best_path = {'distance': float('inf'), 'nodes': []}
        worst_path = {'distance': float('-inf'), 'nodes': []}

        for path_solver in self.path_solvers:
            path_solver.start()

        for path_solver in self.path_solvers:
            path_solver.join()
            total_distance, nodes = path_solver.total_distance, path_solver.nodes

            if total_distance < best_path.get('distance'):
                best_path['distance'], best_path['nodes'] = total_distance, nodes
            elif total_distance > worst_path.get('distance'):
                worst_path['distance'], worst_path['nodes'] = total_distance, nodes

        with open(output_file, 'w') as output_file:
            json.dump(
                {'best': best_path, 'worst': worst_path},
                output_file, indent=4
            )
