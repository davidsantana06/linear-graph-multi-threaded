from colorama import (
    init as init_colorama,
    Fore
)
from os import path

from graph import LinearGraphGenerator, LinearGraphSolver


OUTPUT_FOLDER = path.abspath(
    path.join(
        path.dirname(__file__),
        '..', 'output'
    )
)
GRAPH_FILE = path.join(OUTPUT_FOLDER, 'graph.json')
SOLUTION_FILE = path.join(OUTPUT_FOLDER, 'solution.json')


def generate_graph() -> None:
    graph_generator = LinearGraphGenerator(
        paths=4,
        min_edges=5000,
        max_edges=9999,
        min_distance=1,
        max_distance=10
    )
    graph_generator.generate_graph(GRAPH_FILE)


def solve_graph() -> None:
    graph_solver = LinearGraphSolver(GRAPH_FILE)
    graph_solver.solve_graph(SOLUTION_FILE)


if __name__ == '__main__':
    init_colorama(autoreset=True)

    print(
        '| ----------------------------|\n'
        '| Linear Graph Multi-Threaded |\n'
        '| davidsantana06 -- alissonfr |\n'
        '| --------------------------- |'
    )

    input('\nPressione qualquer tecla para gerar o grafo...')
    generate_graph()
    print(f'O grafo foi gerado em {Fore.CYAN}"{GRAPH_FILE}"')

    input('\nPressione qualquer tecla para resolver o grafo...')
    solve_graph()
    print(f'A solução foi gerada em {Fore.CYAN}"{SOLUTION_FILE}"')
