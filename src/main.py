from colorama import init as init_colorama, Fore
from dotenv import load_dotenv
from nest_asyncio import apply as apply_nest_asyncio
from os import path
from typing import Tuple
import asyncio
import json

from graph import LinearGraph
from socket_handler import SocketHandler


ROOT_FOLDER = path.abspath(path.join(path.dirname(__file__), '..'))
ENV_FILE = path.join(ROOT_FOLDER, '.env')
OUTPUT_FOLDER = path.join(ROOT_FOLDER, 'output')
GRAPH_FILE = path.join(OUTPUT_FOLDER, 'graph.json')
SOLUTION_FILE = path.join(OUTPUT_FOLDER, 'solution.json')


def init() -> Tuple[LinearGraph, SocketHandler]:
    load_dotenv(ENV_FILE)
    apply_nest_asyncio()
    init_colorama(autoreset=True)

    return (LinearGraph(), SocketHandler())


def generate_graph(graph: LinearGraph) -> None:
    graph.generate(
        paths=6, 
        min_edges=500, 
        max_edges=1000, 
        min_distance=1, 
        max_distance=10, 
        output_file=GRAPH_FILE
    )
    print(f'O grafo foi gerado em {Fore.CYAN}"{GRAPH_FILE}"')


async def solve_graph(graph: LinearGraph, socket_handler: SocketHandler) -> None:
    socket_handler.start_server()
    graph_data = graph.read_graph(GRAPH_FILE)

    try:
        for i, path in enumerate(graph_data['paths']):
            await socket_handler.send_message(json.dumps({'id': i, 'path': path}))
            await asyncio.sleep(1)

        graph.write_solution(socket_handler.path_solvers, SOLUTION_FILE)
        print(f'\nA solução foi gerada em {Fore.CYAN}"{SOLUTION_FILE}"')
    finally:
        socket_handler.stop_server()


if __name__ == '__main__':
    graph, socket_handler = init()
    
    input('Pressione qualquer tecla para gerar o grafo...')
    generate_graph(graph)

    input('\nPressione qualquer tecla para resolver o grafo...')
    asyncio.run(solve_graph(graph, socket_handler))
