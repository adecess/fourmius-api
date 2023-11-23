from fastapi import HTTPException

from typing import Sequence

from app.services.main import AppService, AppCRUD
from sqlalchemy.sql.expression import select
from app.models.sqlalchemy import Listing
from app.schemas.listing import ListingPayload


class ListingCRUD(AppCRUD):
    def get_listings(self) -> Sequence[Listing]:
        return self.db.execute(select(Listing)).scalars().all()

    def get_listing(self, _id: int) -> Listing:
        listing = self.db.scalars(select(Listing).filter_by(id=_id).limit(1)).first()

        if not listing:
            raise HTTPException(status_code=404, detail="Listing not found")

        return listing

    def create_listing(self, listing: ListingPayload) -> Listing:
        new_listing = Listing(**listing.model_dump())
        self.db.add(new_listing)
        self.db.commit()
        self.db.refresh(new_listing)

        return new_listing


class ListingService(AppService):
    def get_listings(self) -> Sequence[Listing]:
        return ListingCRUD(self.db).get_listings()

    def get_listing(self, _id: int) -> Listing:
        return ListingCRUD(self.db).get_listing(_id)

    def create_listing(self, listing: ListingPayload) -> Listing:
        return ListingCRUD(self.db).create_listing(listing)
