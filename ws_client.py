import asyncio
from websockets.sync.client import connect
import argparse


def create_argparse():
    parser = argparse.ArgumentParser(description="Send request to server")
    parser.add_argument("-n", "--number", type=int, help="Number for processing")
    parser.add_argument(
        "-a", "--array", nargs="+", type=int, help="Array for processing"
    )
    parser.add_argument(
        "-r", "--range", nargs="+", type=int, help="Range for processing"
    )
    return parser


def main():
    parser = create_argparse()
    args = parser.parse_args()
    number = args.number
    array_args = args.array
    range_args = args.range

    if number is not None:
        with connect("ws://127.0.0.1:8000/ws/v1/single") as websocket:
            websocket.send(str(number))
            message = websocket.recv()
            print(message)
    if array_args is not None:
        with connect("ws://127.0.0.1:8000/ws/v1/array") as websocket:
            transform = ",".join([str(num) for num in array_args])
            websocket.send(transform)
            message = websocket.recv()
            print(message)
    if range_args is not None:
        with connect("ws://127.0.0.1:8000/ws/v1/range") as websocket:
            transform = ",".join([str(num) for num in range_args])
            websocket.send(transform)
            message = websocket.recv()
            print(message)


if __name__ == "__main__":
    main()
