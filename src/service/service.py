from src.repository.repository import NumberRepository
from fastapi import Depends


class Service:
    def __init__(self, repository: NumberRepository = Depends()):
        self.repository = repository

    async def process_single(self, input_data: int) -> str:
        return self.repository.get_value(input_data)

    async def process_array(self, input_data: list) -> list:
        proccessed_data = []
        for number in input_data:
            proccessed_data.append(self.repository.get_value(number))
        return proccessed_data

    async def process_range(self, input_data: list) -> list:
        proccessed_data = []
        for number in range(input_data[0], input_data[1] + 1):
            proccessed_data.append(self.repository.get_value(number))
        return proccessed_data
