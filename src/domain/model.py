from dataclasses import dataclass
from datetime import date
from typing import List
from uuid import UUID
from enum import Enum


class PropertyType(Enum):
    HOUSE = 1
    APARTMENT = 2


@dataclass(frozen=True)
class PropertyCharacteristic:
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
        characteristic: PropertyCharacteristic,
        prices: List[PropertyPrice],
        listing: str,
        version_number: int = 0,
    ):
        self.id = id
        self.version_number = version_number
        self.characteristic = characteristic
        self.prices = prices
        self.latest_price = prices[0]
        self.change_since_previous_price = None
        self.listing = listing
