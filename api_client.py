import requests
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
        response = requests.get(f"http://127.0.0.1:8000/api/v1/{number}")
        print(response.json())
    if array_args is not None:
        nums_str = "&".join(f"nums_array={num}" for num in array_args)
        response = requests.get(f"http://127.0.0.1:8000/api/v1/array/?{nums_str}")
        print(response.json())
    if range_args is not None:
        nums_str = "&".join(f"nums_range={num}" for num in range_args)
        response = requests.get(f"http://127.0.0.1:8000/api/v1/range/?{nums_str}")
        print(response.json())


if __name__ == "__main__":
    main()
