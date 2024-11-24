import random
import sys
from websockets.sync.client import connect
from threading import Thread
from modules.shared.services import LoggerService

class ConnectChat():
    def __init__(self):
        LoggerService.setup()
        self.connection_id = random.randint(100000, 900000)
        self.uri = f"ws://localhost:3000/message/ws/{self.connection_id}"

    def receive_messages(self, websocket):
        while True:
            try:
                message = websocket.recv()
                if str(self.connection_id) in message:
                    LoggerService.info(f"{message}")
                else:
                    LoggerService.warn(f"{message}")
            except TimeoutError:
                pass

    def send_messages(self, websocket):
        while True:
            message = input("")
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            if message.lower() == "exit":
                LoggerService.info("Saindo do chat...")
                break
            websocket.send(message)

    def open(self):
        with connect(self.uri) as websocket:
            receiver_thread = Thread(target=self.receive_messages, args=(websocket,), daemon=True)
            sender_thread = Thread(target=self.send_messages, args=(websocket,))
            receiver_thread.start()
            sender_thread.start()
            sender_thread.join()

if __name__ == "__main__":
    ConnectChat().open()