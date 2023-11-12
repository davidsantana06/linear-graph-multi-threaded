from colorama import (
    init as init_colorama,
    Fore
)
from os import path

from graph import LinearGraph


OUTPUT_FOLDER = path.abspath(
    path.join(
        path.dirname(__file__),
        '..', 'output'
    )
)
GRAPH_FILE = path.join(OUTPUT_FOLDER, 'graph.json')
SOLUTION_FILE = path.join(OUTPUT_FOLDER, 'solution.json')


if __name__ == '__main__':
    init_colorama(autoreset=True)
    print(
        '| ----------------------------|\n'
        '| Linear Graph Multi-Threaded |\n'
        '| davidsantana06 -- alissonfr |\n'
        '| --------------------------- |'
    )

    graph = LinearGraph()

    input('\nPressione qualquer tecla para gerar o grafo...')
    graph.generate_graph(
        paths=5, min_edges=500, max_edges=1000, min_distance=1, max_distance=10, 
        output_file=GRAPH_FILE
    )
    print(f'O grafo foi gerado em {Fore.CYAN}"{GRAPH_FILE}"')

    input('\nPressione qualquer tecla para resolver o grafo...')
    graph.solve_graph(GRAPH_FILE, SOLUTION_FILE)
    print(f'A solução foi gerada em {Fore.CYAN}"{SOLUTION_FILE}"')
