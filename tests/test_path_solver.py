from sys_config import *
from src.path_solver import LinearPathSolver


GRAPH_PATH = [
    {'node': 'A', 'distance': 1},
    {'node': 'B', 'distance': 2},
    {'node': 'C', 'distance': 3},
    {'node': 'D', 'distance': 4},
    {'node': 'E', 'distance': 5},
    {'node': 'F', 'distance': 6}
]


if __name__ == '__main__':
    path_solver = LinearPathSolver(GRAPH_PATH)
    path_solver.start()
    path_solver.join()
    
    print(path_solver.total_distance, path_solver.nodes)
