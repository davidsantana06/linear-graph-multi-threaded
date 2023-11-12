from abc import ABC, abstractmethod
from typing import Dict, List, Tuple
from random import randint, uniform
import json

from .path_solver import PathSolver, LinearPathSolver


class Graph(ABC):
    def __init__(self) -> None:
        self._path_solvers: List[PathSolver] = []

    @abstractmethod
    def generate_path(self) -> List[Dict[str, object]]:
        ...

    @abstractmethod
    def generate_graph(
        self, 
        paths: int, min_edges: int, max_edges: int, min_distance: int, max_distance: int, 
        output_file: str
    ) -> None:
        ...

    @abstractmethod
    def _start_path_solvers(self, graph_file: str) -> None:
        ...

    @abstractmethod
    def _join_path_solvers(self) -> Tuple[Dict[str, object], ...]:
        ...

    @abstractmethod
    def solve_graph(self, graph_file: str, output_file: str) -> None:
        ...


class LinearGraph(Graph):
    def generate_path(
            self,
            min_edges: int, max_edges: int, min_distance: int, max_distance: int
        ) -> List[Dict[str, object]]:
        return [
            {'node': i + 1, 'distance': uniform(min_distance, max_distance)}
            for i in range(randint(min_edges, max_edges))
        ]
    
    def generate_graph(
            self, 
            paths: int, min_edges: int, max_edges: int, min_distance: int, max_distance: int,
            output_file: str
        ) -> None:
        with open(output_file, 'w') as graph_file:
            json.dump({'paths': [
                self.generate_path(min_edges, max_edges, min_distance, max_distance) 
                for _ in range(paths)
            ]}, graph_file, indent=4)

    def _start_path_solvers(self, graph_file: str) -> None:
        with open(graph_file, 'r') as g_file:
            graph: Dict[str, object] = json.load(g_file)

        for i, path in enumerate(graph['paths']):
            path_solver = LinearPathSolver(id=i+ 1, path=path)
            path_solver.start()
            self._path_solvers.append(path_solver)
    
    def _join_path_solvers(self) -> Tuple[Dict[str, object], ...]:
        best_path = {'id': -1, 'distance': float('inf'), 'nodes': []}
        worst_path = {'id': -1, 'distance': float('-inf'), 'nodes': []}

        for path_solver in self._path_solvers:
            path_solver.join()
            id, total_distance, nodes = path_solver.id, path_solver.total_distance, path_solver.nodes

            if total_distance < best_path.get('distance'):
                best_path.update({'id': id, 'distance': total_distance, 'nodes': nodes})
            elif total_distance > worst_path.get('distance'):
                worst_path.update({'id': id, 'distance': total_distance, 'nodes': nodes})

        return (best_path, worst_path)
    
    def solve_graph(self, graph_file: str, output_file: str) -> None:
        self._start_path_solvers(graph_file)
        best_path, worst_path = self._join_path_solvers()

        with open(output_file, 'w') as output_file:
            json.dump({'best': best_path, 'worst': worst_path}, output_file, indent=4)
