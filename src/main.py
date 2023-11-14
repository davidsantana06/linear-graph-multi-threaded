import asyncio
from colorama import (init as init_colorama, Fore)
from os import path
from graph import LinearGraph
from socket_handler import SocketHandler
import json
import nest_asyncio

nest_asyncio.apply()
OUTPUT_FOLDER = path.abspath(path.join(path.dirname(__file__),'..', 'output'))
GRAPH_FILE = path.join(OUTPUT_FOLDER, 'graph.json')
SOLUTION_FILE = path.join(OUTPUT_FOLDER, 'solution.json')

async def main():
    init_colorama(autoreset=True)
    print(
        '| ----------------------------|\n'
        '| Linear Graph Multi-Threaded |\n'
        '| davidsantana06 -- alissonfr |\n'
        '| --------------------------- |'
    )
    linear_graph = LinearGraph()

    linear_graph.generate(paths=6, min_edges=500, max_edges=1000, min_distance=1, max_distance=10, output_file=GRAPH_FILE)
    print(f'O grafo foi gerado em {Fore.CYAN}"{GRAPH_FILE}"')

    socket_handler = SocketHandler()
    socket_handler.start_server()

    input('\nPressione qualquer tecla para resolver o grafo...')
    graph = linear_graph.get_graph(GRAPH_FILE)

    try:
        for path in enumerate(graph['paths']):
            await socket_handler.send_message(json.dumps(path))
            await asyncio.sleep(1)
        linear_graph.get_solution(socket_handler.get_path_solvers(), SOLUTION_FILE)
        print(f'A solução foi gerada em {Fore.CYAN}"{SOLUTION_FILE}"')
    finally:
        socket_handler.stop_server()

if __name__ == '__main__':
    asyncio.run(main())