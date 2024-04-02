from fastapi import APIRouter, Depends, Query
from src.schemas import schemas
from src.service.service import Service
from typing import Annotated, List

router = APIRouter(
    tags=["rest"],
    prefix="/api/v1",
)


@router.get(
    "/{number}",
    responses={404: {"model": schemas.NotFoundError}},
    name="Answer on number",
)
async def answer_on_number(
    num: schemas.Number = Depends(), service: Service = Depends()
):
    return await service.process_single(num.number)


@router.get(
    "/array/",
    responses={404: {"model": schemas.NotFoundError}},
    name="Answer on array",
)
async def answer_on_array(
    nums_array: Annotated[List[int], Query()] = [],
    service: Service = Depends(),
):
    return await service.process_array(nums_array)


@router.get(
    "/range/",
    responses={404: {"model": schemas.NotFoundError}},
    name="Answer on range",
)
async def answer_on_range(
    nums_range: Annotated[List[int], Query()] = [], service: Service = Depends()
):
    return await service.process_range(nums_range)
