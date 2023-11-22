import pytest

from app.schemas.listing import ListingItem
from .database import client, session

listing_data = {
    "latest_price": 400000,
    "listing_url": "seloger.com/massivehouselille",
    "location": "27 rue Solferino, Lille",
    "rooms": 13,
    "surface": 300,
    "title": "Massive House Lille Vauban",
    "type": "house",
}


@pytest.fixture()
def test_listing(client):
    response = client.post("/listings/", json=listing_data)

    assert response.status_code == 201


def test_get_listings(client, test_listing):
    response = client.get("/listings/")

    # Then
    assert response.status_code == 200
    assert response.json() == [listing_data]


def test_create_listing(client):
    response = client.post(
        "/listings/",
        json={
            "latest_price": 500000,
            "listing_url": "seloger.com/massiveflatlille",
            "location": "28 rue Solferino, Lille",
            "rooms": 6,
            "surface": 150,
            "title": "Massive Flat Lille Vauban",
            "type": "flat",
        },
    )

    listing_response = ListingItem(**response.json())

    assert listing_response.id == 1
    assert listing_response.listing_url == "seloger.com/massiveflatlille"
    assert listing_response.title == "Massive Flat Lille Vauban"
    assert listing_response.latest_price == 500000
    assert listing_response.location == "28 rue Solferino, Lille"

    assert response.status_code == 201
