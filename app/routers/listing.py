from fastapi import APIRouter, Depends

from app.config.config import get_settings, Settings


router = APIRouter(
    prefix="/listing",
    tags=["listing"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_listing():
    return {
        "listing": "this is your big house!",
    }
