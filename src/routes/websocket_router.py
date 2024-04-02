from fastapi import APIRouter, Depends, Query
from src.service.service import Service
from fastapi import WebSocket, WebSocketDisconnect
from typing import Annotated, List
from src.schemas import schemas

router = APIRouter(
    prefix="/ws/v1",
)


@router.websocket(
    "/single",
    name="Answer on number",
)
async def answer_on_number(websocket: WebSocket, service: Service = Depends()):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            print(data)
            response = await service.process_single(int(data))
            await websocket.send_text(str(response))
    except WebSocketDisconnect:
        await websocket.close()
    except ValueError:
        print("Not a number")
        await websocket.close()


@router.websocket(
    "/array",
    name="Answer on array",
)
async def answer_on_array(
    websocket: WebSocket,
    service: Service = Depends(),
):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            list_array = [int(num) for num in data.split(",")]
            response = await service.process_array(list_array)
            str_list = ",".join([str(num) for num in response])
            await websocket.send_text(str_list)
    except WebSocketDisconnect:
        await websocket.close()


@router.websocket(
    "/range",
    name="Answer on number",
)
async def answer_on_range(
    websocket: WebSocket,
    service: Service = Depends(),
):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            list_array = [int(num) for num in data.split(",")]
            response = await service.process_range(list_array)
            str_list = ",".join([str(num) for num in response])
            await websocket.send_text(str_list)
    except WebSocketDisconnect:
        await websocket.close()
