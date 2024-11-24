from fastapi import WebSocket

from modules.shared.adapters import WebSocketAdapter
from modules.shared.adapters.websocket_adapter import WebSocketOptions

class WebSocketService(WebSocketAdapter[WebSocket]):
    __active_connections: list[WebSocket] = []

    def __init__(self, port: int = 3001):
        super().__init__(WebSocketOptions(
            port=port
        ))

    async def connect(self, socket):
        await socket.accept()
        self.__active_connections.append(socket)

    async def disconnect(self, socket):
        self.__active_connections.remove(socket)

    async def send_message(self, socket, message):
        await socket.send_text(message)
    
    async def broadcast(self, message: str):
        for connection in self.__active_connections:
            await self.send_message(connection, message)