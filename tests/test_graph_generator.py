from os import path
from sys_config import *
from src.graph_generator import LinearGraphGenerator


OUTPUT_FILE_PATH = path.join(ROOT_FOLDER, 'output', 'graph.json')


if __name__ == '__main__':
    graph_generator = LinearGraphGenerator(
        paths=10,
        min_edges=200,
        max_edges=5000,
        min_distance=1,
        max_distance=10
    )
    graph_generator.generate_graph(OUTPUT_FILE_PATH)