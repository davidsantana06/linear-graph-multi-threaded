from sys_config import *
from src.graph import LinearPathSolver


GRAPH_PATH_1 = [
    {'node': 'A', 'distance': 1},
    {'node': 'B', 'distance': 2},
    {'node': 'C', 'distance': 3},
    {'node': 'D', 'distance': 4},
    {'node': 'E', 'distance': 5},
    {'node': 'F', 'distance': 6}
]
GRAPH_PATH_2 = [
    {'node': 'A', 'distance': 3},
    {'node': 'B', 'distance': 9},
    {'node': 'C', 'distance': 15},
]


if __name__ == '__main__':
    path_solver_1 = LinearPathSolver(GRAPH_PATH_1)
    path_solver_1.solve_path()
    print(path_solver_1.get_total_distance(), path_solver_1.get_nodes())

    path_solver_2 = LinearPathSolver(GRAPH_PATH_2)
    path_solver_2.start()
    path_solver_2.join()
    print(path_solver_2.get_total_distance(), path_solver_2.get_nodes())
