import asyncio
import websockets
from typing import List
import json
from graph.path_solver import PathSolver

class SocketHandler:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.server = None
        self.clients = set()
        self.path_solvers: List[PathSolver] = []

    async def handle_client(self, websocket, path):
        self.clients.add(websocket)
        try:
            async for message in websocket:
                data = json.loads(message)
                print(f"O caminho {data['id']} foi resolvido pelo cliente com sucesso!")
                self.path_solvers.append(data)
        finally:
            self.clients.remove(websocket)

    async def send_message(self, message):
        if self.clients:
            print("Enviando caminho para o cliente...")
            await asyncio.gather(*[client.send(message) for client in self.clients])

    def start_server(self):
        start_server = websockets.serve(self.handle_client, self.host, self.port)

        self.server = asyncio.get_event_loop().run_until_complete(start_server)
        print(f"🚀  Servidor WebSocket iniciou em ws://{self.host}:{self.port}...")

    def get_path_solvers(self):
        return self.path_solvers

    def stop_server(self):
        if self.server:
            self.server.close()
            asyncio.get_event_loop().run_until_complete(self.server.wait_closed())
            print("Servidor WebSocket foi interrompido.")
