from pydantic import BaseModel


class BaseError(BaseModel):
    detail: str
