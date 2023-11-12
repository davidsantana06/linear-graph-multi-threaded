from abc import ABC, abstractmethod
from overrides import override
from threading import Thread
from typing import Dict, List


class PathSolver(ABC, Thread):
    def __init__(self, graph_path: List[Dict[str, object]]) -> None:
        Thread.__init__(self)
        self._graph_path = graph_path
        self._total_distance = 0
        self._nodes = []

    def get_total_distance(self) -> float:
        return self._total_distance
    
    def get_nodes(self) -> List[object]:
        return self._nodes

    @abstractmethod
    def solve_path(self) -> None:
        ...


class LinearPathSolver(PathSolver):
    def solve_path(self) -> None:
        for edge in self._graph_path:
            self._total_distance += edge['distance']
            self._nodes.append(edge['node'])

    @override
    def run(self) -> None:
        self.solve_path()
