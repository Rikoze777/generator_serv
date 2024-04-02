from fastapi import FastAPI
from src.routes import rest_router, websocket_router

app = FastAPI()

app.include_router(rest_router.router, tags=["REST"])
app.include_router(websocket_router.router, tags=["WEBSOCKET"])
