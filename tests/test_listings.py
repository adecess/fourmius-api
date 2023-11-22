from app.schemas.listing import ListingItem
from .database import client, session


def test_root(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Fourmius.io!",
        "environment": "dev",
        "testing": True,
    }


def test_get_listings(client):
    response = client.get("/listings/")

    # Then
    assert response.status_code == 200
    assert response.json() == []


def test_create_listing(client):
    response = client.post(
        "/listings/",
        json={
            "latest_price": 400000,
            "listing_url": "seloger.com/massivehouselille",
            "location": "27 rue Solferino, Lille",
            "rooms": 13,
            "surface": 300,
            "title": "Massive House Lille Vauban",
            "type": "house",
        },
    )

    new_listing = ListingItem(**response.json())

    assert new_listing.id == 1
    assert new_listing.listing_url == "seloger.com/massivehouselille"
    assert new_listing.title == "Massive House Lille Vauban"
    assert new_listing.latest_price == 400000
    assert new_listing.location == "27 rue Solferino, Lille"

    assert response.status_code == 201
