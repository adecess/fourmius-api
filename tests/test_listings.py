from src.schemas.listing import ListingResponse
from tests.conftest import listing_data


def test_get_listings(client, test_listing):
    response = client.get("/listings/")

    # Then
    assert response.status_code == 200
    assert response.json() == [{**listing_data, "id": 1}]


def test_get_listing(client, test_listing):
    new_listing_response = client.post(
        "/listings/",
        json={
            "title": "Big Flat Gambetta Lille",
            "location": "335 rue Gambetta, Lille",
            "type": "flat",
            "latest_price": 320000,
            "surface": 45,
            "rooms": 2,
            "listing_url": "seloger.com/bigflatgambetta",
        },
    )
    listing_id = new_listing_response.json()["id"]

    response = client.get(f"/listings/{listing_id}/")
    assert response.status_code == 200

    listing_response = ListingResponse(**response.json())
    assert listing_response.id == listing_id
    assert listing_response.listing_url == "seloger.com/bigflatgambetta"
    assert listing_response.latest_price == 320000
    assert listing_response.title == "Big Flat Gambetta Lille"


def test_get_listing_invalid_id(client, test_listing):
    new_listing_response = client.post(
        "/listings/",
        json={
            "title": "Big Flat Gambetta Lille",
            "location": "335 rue Gambetta, Lille",
            "type": "flat",
            "latest_price": 320000,
            "surface": 45,
            "rooms": 2,
            "listing_url": "seloger.com/bigflatgambetta",
        },
    )
    listing_id = 43

    response = client.get(f"/listings/{listing_id}/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Listing not found"


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

    listing_response = ListingResponse(**response.json())

    assert listing_response.id == 1
    assert listing_response.listing_url == "seloger.com/massiveflatlille"
    assert listing_response.title == "Massive Flat Lille Vauban"
    assert listing_response.latest_price == 500000
    assert listing_response.location == "28 rue Solferino, Lille"

    assert response.status_code == 201


def test_create_listing_invalid_json(client):
    response = client.post(
        "/listings/",
        json={},
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": ["body", "title"],
                "msg": "Field required",
                "input": {},
                "url": "https://errors.pydantic.dev/2.4/v/missing",
            },
            {
                "type": "missing",
                "loc": ["body", "location"],
                "msg": "Field required",
                "input": {},
                "url": "https://errors.pydantic.dev/2.4/v/missing",
            },
            {
                "type": "missing",
                "loc": ["body", "type"],
                "msg": "Field required",
                "input": {},
                "url": "https://errors.pydantic.dev/2.4/v/missing",
            },
            {
                "type": "missing",
                "loc": ["body", "latest_price"],
                "msg": "Field required",
                "input": {},
                "url": "https://errors.pydantic.dev/2.4/v/missing",
            },
            {
                "type": "missing",
                "loc": ["body", "surface"],
                "msg": "Field required",
                "input": {},
                "url": "https://errors.pydantic.dev/2.4/v/missing",
            },
            {
                "type": "missing",
                "loc": ["body", "rooms"],
                "msg": "Field required",
                "input": {},
                "url": "https://errors.pydantic.dev/2.4/v/missing",
            },
            {
                "type": "missing",
                "loc": ["body", "listing_url"],
                "msg": "Field required",
                "input": {},
                "url": "https://errors.pydantic.dev/2.4/v/missing",
            },
        ]
    }
