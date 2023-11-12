from os import path
from sys_config import *
from src.graph import LinearGraph


GRAPH_FILE = path.join(OUTPUT_FOLDER, 'graph.json')
SOLUTION_FILE = path.join(OUTPUT_FOLDER, 'solution.json')


if __name__ == '__main__':
    graph = LinearGraph()
    graph.generate_graph(
        paths=10,
        min_edges=2000,
        max_edges=5000,
        min_distance=1,
        max_distance=10,
        output_file=GRAPH_FILE
    )
    graph.solve_graph(GRAPH_FILE, SOLUTION_FILE)
