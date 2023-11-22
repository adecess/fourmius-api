from typing import List, Type

from app.services.main import AppService
from app.models.sqlalchemy import Listing
from app.schemas.listing import ListingPayload


class ListingService(AppService):
    def get_listing(self) -> List[Type[Listing]]:
        listings = self.db.query(Listing).all()
        return listings

    def create_listing(self, listing: ListingPayload) -> Listing:
        new_listing = Listing(**listing.model_dump())
        self.db.add(new_listing)
        self.db.commit()
        self.db.refresh(new_listing)

        return new_listing
