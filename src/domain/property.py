from dataclasses import dataclass
from datetime import date
from typing import List
from uuid import UUID
from enum import Enum


class PropertyType(Enum):
    HOUSE = 1
    APARTMENT = 2


@dataclass(frozen=True)
class PropertyCharacteristics:
    address: str
    postcode: str
    city: str
    type: PropertyType
    surface: int
    rooms: int


@dataclass(frozen=True)
class PropertyPrice:
    price: int
    price_date: date


class Property:
    def __init__(
        self,
        id: UUID,
        characteristics: PropertyCharacteristics,
        prices: List[PropertyPrice],
        listing: str,
        version_number: int = 0,
    ):
        self.id = id
        self.version_number = version_number
        self.characteristic = characteristics
        self.prices = prices
        self.latest_price = prices[0]
        self.change_since_previous_price: float | None = None
        self.listing = listing

    def calculate_price_change(
        self, new_price: PropertyPrice, old_price: PropertyPrice
    ) -> float:
        return new_price.price / old_price.price

    def add_price_entry(self, new_price: PropertyPrice) -> None:
        self.change_since_previous_price = self.calculate_price_change(
            new_price, self.latest_price
        )
        self.prices.append(new_price)
        self.latest_price = new_price

    def is_price_decreasing(self) -> bool | None:
        return (
            self.change_since_previous_price < 1
            if self.change_since_previous_price
            else None
        )
