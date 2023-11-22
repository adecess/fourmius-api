from pydantic import BaseModel, ConfigDict


class ListingBase(BaseModel):
    title: str
    location: str
    type: str
    latest_price: int
    surface: int
    rooms: int
    listing_url: str


class ListingCreate(ListingBase):
    pass


class ListingItem(ListingBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class ListingOut(ListingBase):
    model_config = ConfigDict(from_attributes=True)
