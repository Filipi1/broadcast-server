from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from modules.shared.services import WebSocketService

websocket_manager = WebSocketService()
message_controller_router = APIRouter(
    prefix="/message",
    tags=["Message"]
)

@message_controller_router.websocket("/ws/{client_id}")
async def listen_messages(websocket: WebSocket, client_id: int):
    await websocket_manager.connect(websocket)
    await websocket_manager.broadcast(f"O Cliente # {client_id} entrou no chat!")
    try:
        while True:
            data = await websocket.receive_text()
            await websocket_manager.broadcast(f"O Cliente # {client_id} disse: {data}")
    except WebSocketDisconnect:
        await websocket_manager.disconnect(websocket)
        await websocket_manager.broadcast(f"O Cliente # {client_id} saiu do chat!")