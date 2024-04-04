from fastapi import APIRouter, Depends, WebSocketException, status
from src.service.service import Service
from fastapi import WebSocket, WebSocketDisconnect

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
            try:
                number = int(data)
            except ValueError:
                raise WebSocketException(
                    code=status.WS_1008_POLICY_VIOLATION,
                    reason="Wrong type. Please enter the number",
                )
            if number < 0 or number > 1000:
                raise WebSocketException(
                    code=status.WS_1008_POLICY_VIOLATION,
                    reason="Wrong number. Please write number from 1 to 1000",
                )
            response = await service.process_single(int(data))
            await websocket.send_text(str(response))
    except WebSocketDisconnect:
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
            try:
                list_array = [int(num) for num in data.split(",")]
            except ValueError:
                raise WebSocketException(
                    code=status.WS_1008_POLICY_VIOLATION,
                    reason="Wrong type. Please enter the number",
                )
            if min(list_array) < 0 or max(list_array) > 1000:
                raise WebSocketException(
                    code=status.WS_1008_POLICY_VIOLATION,
                    reason="Wrong number. Please write number from 1 to 1000",
                )
            response = await service.process_array(list_array)
            str_response = ",".join([str(num) for num in response])
            await websocket.send_text(str_response)
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
            try:
                list_array = [int(num) for num in data.split(",")]
            except ValueError:
                raise WebSocketException(
                    code=status.WS_1008_POLICY_VIOLATION,
                    reason="Wrong type. Please enter the number",
                )
            if min(list_array) < 0 or max(list_array) > 1000:
                raise WebSocketException(
                    code=status.WS_1008_POLICY_VIOLATION,
                    reason="Wrong number. Please write number from 1 to 1000",
                )
            response = await service.process_range(list_array)
            str_list = ",".join([str(num) for num in response])
            await websocket.send_text(str_list)
    except WebSocketDisconnect:
        await websocket.close()
