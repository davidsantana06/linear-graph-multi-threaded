from os import path
from sys_config import *
from src.graph_solver import LinearGraphSolver


GRAPH_FILE = path.join(ROOT_FOLDER, 'output', 'graph.json')
OUTPUT_FILE = path.join(ROOT_FOLDER, 'output', 'solution.json')


if __name__ == '__main__':
    graph_solver = LinearGraphSolver(GRAPH_FILE)
    graph_solver.solve_graph(OUTPUT_FILE)
