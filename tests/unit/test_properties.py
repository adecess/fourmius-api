import pytest
from uuid import uuid4
from datetime import date
from src.domain.property import (
    Property,
    PropertyCharacteristics,
    PropertyPrice,
    PropertyType,
)


@pytest.fixture
def property() -> Property:
    propertyCharacteristics = PropertyCharacteristics(
        "75 rue de la Boétie",
        "75001",
        "Paris",
        PropertyType.APARTMENT,
        170,
        6,
    )
    propertyPrice = PropertyPrice(2760000, date(2022, 1, 14))
    listing = "legroscoin.fr/grosappartsamere"

    return Property(uuid4(), propertyCharacteristics, [propertyPrice], listing)


def test_adding_new_price_updates_latest_price(property):
    new_price = PropertyPrice(3220000, date.today())
    old_price = property.latest_price

    property.add_price_entry(new_price)

    assert property.prices == [old_price, new_price]
    assert property.latest_price == new_price
    assert property.change_since_previous_price == new_price.price / old_price.price


def test_updating_with_lower_price_sets_price_drop_flag(property):
    new_price = PropertyPrice(700000, date.today())

    property.add_price_entry(new_price)

    assert property.is_price_decreasing()
