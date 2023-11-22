from fastapi import Depends

from typing import List, Type, Annotated

from app.services.main import AppService, AppCRUD
from app.models.sqlalchemy import Listing
from app.schemas.listing import ListingPayload


class ListingCRUD(AppCRUD):
    def get_listings(self) -> List[Type[Listing]]:
        listings = self.db.query(Listing).all()
        return listings

    def create_listing(self, listing: ListingPayload) -> Listing:
        new_listing = Listing(**listing.model_dump())
        self.db.add(new_listing)
        self.db.commit()
        self.db.refresh(new_listing)

        return new_listing


class ListingService(AppService):
    def get_listings(self) -> List[Type[Listing]]:
        return ListingCRUD(self.db).get_listings()

    def create_listing(self, listing: ListingPayload) -> Listing:
        return ListingCRUD(self.db).create_listing(listing)
