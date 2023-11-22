from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.schemas.listing import ListingItem
from app.config.config import settings
from app.config.database import get_db

SQLALCHEMY_DATABASE_URL = (f"postgresql://{settings.database_username}:{settings.database_password}"
                           f"@{settings.database_test_hostname}:{settings.database_port}/{settings.database_test_name}")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Fourmius.io!", "environment": "dev", "testing": False}


def test_get_listings():
    response = client.get("/listings")

    # Then
    assert response.status_code == 200
    assert response.json() == []


def test_create_listing():
    response = client.post(
        "/listings",
        json={
            'latest_price': 400000,
            'listing_url': 'seloger.com/massivehouselille',
            'location': '27 rue Solferino, Lille',
            'rooms': 13,
            'surface': 300,
            'title': 'Massive House Lille Vauban',
            'type': 'house',
         })

    new_listing = ListingItem(**response.json())

    assert new_listing.id == 1
    assert new_listing.listing_url == 'seloger.com/massivehouselille'
    assert new_listing.title == 'Massive House Lille Vauban'
    assert new_listing.price == 400000
    assert new_listing.location == '27 rue Solferino, Lille'

    assert response.status_code == 201
