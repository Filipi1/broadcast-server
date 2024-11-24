from fastapi import FastAPI
from modules.messages.controllers.message_controller import message_controller_router

app = FastAPI()
app.include_router(message_controller_router)