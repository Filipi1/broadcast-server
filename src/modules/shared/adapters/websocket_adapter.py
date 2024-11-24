from abc import ABC, abstractmethod
from modules.shared.exceptions import NotImplementedException
from typing import TypeVar, Generic

T = TypeVar('T')

class WebSocketOptions:
    def __init__(self, port: int):
        self.port = port

class WebSocketAdapter(ABC, Generic[T]):
    def __init__(self, options: WebSocketOptions):
        self.__options = options
        super().__init__()

    def current_port(self) -> int:
        """Retorna a porta utilizada para conexão ao websocket."""
        return self.__options.port

    @abstractmethod
    async def connect(self, socket: T):
        """Deve conectar um cliente ao servidor websocket."""
        raise NotImplementedException("connect")
    
    @abstractmethod
    async def disconnect(self, socket: T):
        """Deve desconectar um cliente ao servidor websocket."""
        raise NotImplementedException("disconnect")
    
    @abstractmethod
    async def send_message(self, socket: T, message: str):
        """Deve desconectar um cliente ao servidor websocket."""
        raise NotImplementedException("send_message")