from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session

from ..schemas.listing import ListingCreate, ListingItem, ListingOut
from ..models.sqlalchemy import Listing
from ..config.database import get_db


router = APIRouter(
    prefix="/listing",
    tags=["listing"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[ListingOut])
async def get_listings(db: Session = Depends(get_db)):
    listings = db.query(Listing).all()
    return listings


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ListingItem)
def create_listing(listing: ListingCreate, db: Session = Depends(get_db)):
    new_listing = Listing(**listing.model_dump())
    db.add(new_listing)
    db.commit()
    db.refresh(new_listing)

    return new_listing
