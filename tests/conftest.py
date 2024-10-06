from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app
from src.config.config import settings
from src.config.database import get_db
from src.models.sqlalchemy import Base

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.database_username}:{settings.database_password}"
    f"@{settings.database_test_hostname}:{settings.database_test_port}/{settings.database_test_name}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


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
