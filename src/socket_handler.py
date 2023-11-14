from colorama import Fore
from os import environ
from typing import List
from websockets import WebSocketServerProtocol
import asyncio
import json
import websockets

from graph import PathSolver


class SocketHandler:
    def __init__(self):
        self.__host = environ.get('HOST')
        self.__port = int(environ.get('PORT'))
        self.__server = None
        self.__clients: List[WebSocketServerProtocol] = []
        self.__path_solvers: List[PathSolver] = []

    @property
    def path_solvers(self):
        return self.__path_solvers

    async def handle_client(self, websocket: WebSocketServerProtocol):
        self.__clients.append(websocket)

        try:
            async for message in websocket:
                data = json.loads(message)
                self.__path_solvers.append(data)
                print(f'O caminho {data["id"]} foi resolvido pelo cliente com sucesso!')
        finally:
            self.__clients.remove(websocket)

    async def send_message(self, message: str):
        if self.__clients:
            print('\nEnviando caminho para o cliente...')
            await asyncio.gather(*[client.send(message) for client in self.__clients])

    def start_server(self):
        start_server = websockets.serve(self.handle_client, self.__host, self.__port)
        self.__server = asyncio.get_event_loop().run_until_complete(start_server)
        print(f'O servidor WebSocket iniciou em {Fore.GREEN}ws://{self.__host}:{self.__port}')

    def stop_server(self):
        if self.__server:
            self.__server.close()
            asyncio.get_event_loop().run_until_complete(self.__server.wait_closed())
            print(f'\nO servidor WebSocket foi interrompido')
