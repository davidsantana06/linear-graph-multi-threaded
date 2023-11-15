from abc import ABC, abstractmethod
from typing import Dict, List, Tuple
from random import randint, uniform
import json

from .path_solver import LinearPathSolver, PathSolver


class Graph(ABC):
    @abstractmethod
    def _generate_path(self) -> List[Dict[str, object]]:
        ...

    @abstractmethod
    def generate( self,  paths: int, min_edges: int, max_edges: int, min_distance: int, max_distance: int,  output_file: str) -> None:
        ...

    def _create_path_log(self, id: int, total_distance: float, nodes: List[object]) -> Dict[str, object]:
        return {'id': id, 'distance': total_distance, 'nodes': nodes}

    @abstractmethod
    def _evaluate_paths(self) -> Tuple[Dict[str, object], ...]:
        ...

    @abstractmethod
    def read_graph(self, graph_file: str) -> Dict[str, object]:
        ...

    def _create_solution_log(self, best_path: Dict[str, object], worst_path: Dict[str, object]) -> Dict[str, object]:
        return {'best': best_path, 'worst': worst_path}

    @abstractmethod
    def write_solution(self, path_solvers: List[PathSolver], output_file: str) -> None:
        ...


class LinearGraph(Graph):
    def _generate_path(self, min_edges: int, max_edges: int, min_distance: int, max_distance: int) -> List[Dict[str, object]]:
        return [
            {'node': i + 1, 'distance': uniform(min_distance, max_distance)}
            for i in range(randint(min_edges, max_edges))
        ]
    
    def generate(self, paths: int, min_edges: int, max_edges: int, min_distance: int, max_distance: int, output_file: str) -> None:
        with open(output_file, 'w') as graph_file:
            json.dump({'paths': [
                self._generate_path(min_edges, max_edges, min_distance, max_distance) 
                for _ in range(paths)
            ]}, graph_file, indent=4)
    
    def _evaluate_paths(self, path_solvers: List[LinearPathSolver]) -> Tuple[Dict[str, object], ...]:
        best_path = self._create_path_log(-1, float('inf'), [])
        worst_path = self._create_path_log(-1, float('-inf'), [])

        for path_solver in path_solvers:
            id, total_distance, nodes = path_solver['id'], path_solver['total_distance'], path_solver['nodes']

            if total_distance < best_path.get('distance'):
                best_path.update(self._create_path_log(id, total_distance, nodes))
            elif total_distance > worst_path.get('distance'):
                worst_path.update(self._create_path_log(id, total_distance, nodes))

        return (best_path, worst_path)
    
    def read_graph(self, graph_file: str) -> Dict[str, object]:
        with open(graph_file, 'r') as g_file:
            graph = json.load(g_file)

        return graph

    def write_solution(self, path_solvers: List[LinearPathSolver], output_file: str) -> None:
        best_path, worst_path = self._evaluate_paths(path_solvers)

        with open(output_file, 'w') as output_file:
            json.dump(self._create_solution_log(best_path, worst_path), output_file, indent=4)
