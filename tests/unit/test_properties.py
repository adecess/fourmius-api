from src.domain.model import (
    Property,
    PropertyCharacteristics,
    PropertyPrice,
    PropertyType,
)
from uuid import uuid4, UUID
from datetime import date


def make_property(
    id: UUID,
    address: str,
    postcode: str,
    city: str,
    type: PropertyType,
    surface: int,
    rooms: int,
    price: int,
    price_date: date,
) -> Property:
    propertyCharacteristics = PropertyCharacteristics(
        address, postcode, city, type, surface, rooms
    )
    propertyPrice = PropertyPrice(price, price_date)
    listing = "legroscoin.fr/grosappartsamere"

    return Property(id, propertyCharacteristics, [propertyPrice], listing)


def test_adding_new_price_updates_latest_price():
    property = make_property(
        uuid4(),
        "75 rue de la Boétie",
        "75001",
        "Paris",
        PropertyType.APARTMENT,
        170,
        6,
        2760000,
        date(2022, 1, 14),
    )
    new_price = PropertyPrice(3220000, date.today())
    old_price = property.latest_price

    property.add_price_entry(new_price)

    assert property.prices == [old_price, new_price]
    assert property.latest_price == new_price
    assert property.change_since_previous_price == new_price.price / old_price.price
