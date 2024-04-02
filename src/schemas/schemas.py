from pydantic import BaseModel


class Number(BaseModel):
    number: int


class NotFoundError(BaseModel):
    detail: int
