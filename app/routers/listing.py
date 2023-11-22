from fastapi import APIRouter, Depends, status
from typing import Annotated, List

from ..schemas.listing import ListingPayload, ListingResponse
from ..services.listing import ListingService

router = APIRouter(
    prefix="/listings",
    tags=["listings"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[ListingResponse])
async def get_listings(
    listing_service: Annotated[ListingService, Depends(ListingService)]
):
    return listing_service.get_listings()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ListingResponse)
def create_listing(
    listing: ListingPayload,
    listing_service: Annotated[ListingService, Depends(ListingService)],
):
    return listing_service.create_listing(listing)
