from fastapi import APIRouter, Depends, Query, HTTPException
from src.schemas import schemas
from src.service.service import Service
from typing import Annotated, List
from pydantic import ValidationError


router = APIRouter(
    prefix="/api/v1",
)


@router.get(
    "/single/",
    responses={
        400: {"model": schemas.BaseError},
        403: {"model": schemas.BaseError},
        404: {"model": schemas.BaseError},
    },
    name="Answer on number",
)
async def answer_on_number(num: int, service: Service = Depends()):
    try:
        answer = await service.process_single(num)
    except ValueError:
        raise HTTPException(
            status_code=400, detail="Wrong number. Please write number from 1 to 1000"
        )
    except TypeError:
        raise HTTPException(
            status_code=400, detail="Wrong type. Please enter the number"
        )
    except ValidationError:
        raise HTTPException(
            status_code=403, detail="Wrong format. Need  number from 1 to 1000"
        )
    except Exception:
        raise HTTPException(status_code=404, detail="Not found")
    return answer


@router.get(
    "/array/",
    responses={
        400: {"model": schemas.BaseError},
        403: {"model": schemas.BaseError},
        404: {"model": schemas.BaseError},
    },
    name="Answer on array",
)
async def answer_on_array(
    nums_array: Annotated[List[int], Query()] = [],
    service: Service = Depends(),
):
    try:
        answer = await service.process_array(nums_array)
    except ValueError:
        raise HTTPException(
            status_code=404, detail="Wrong number. Please write numbers from 1 to 1000"
        )
    except TypeError:
        raise HTTPException(
            status_code=400, detail="Wrong type. Need array with numbers from 1 to 1000"
        )
    except ValidationError:
        raise HTTPException(
            status_code=403,
            detail="Wrong format. Need array with numbers from 1 to 1000",
        )
    except Exception:
        raise HTTPException(status_code=404, detail="Not found")
    return answer


@router.get(
    "/range/",
    responses={
        400: {"model": schemas.BaseError},
        403: {"model": schemas.BaseError},
        404: {"model": schemas.BaseError},
    },
    name="Answer on range",
)
async def answer_on_range(
    nums_range: Annotated[List[int], Query()] = [], service: Service = Depends()
):
    try:
        answer = await service.process_range(nums_range)
    except ValueError:
        raise HTTPException(
            status_code=404, detail="Wrong number. Please write numbers from 1 to 1000"
        )
    except TypeError:
        raise HTTPException(
            status_code=400, detail="Wrong type. Please enter the numbers"
        )
    except ValidationError:
        raise HTTPException(
            status_code=403,
            detail="Wrong format. Need array with numbers from 1 to 1000",
        )
    except Exception:
        raise HTTPException(status_code=404, detail="Not found")
    return answer
