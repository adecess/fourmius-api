from pydantic import BaseModel, ConfigDict


class ListingBase(BaseModel):
    title: str
    location: str
    type: str
    latest_price: int
    surface: int
    rooms: int
    listing_url: str


class ListingPayload(ListingBase):
    pass


class ListingResponse(ListingBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
