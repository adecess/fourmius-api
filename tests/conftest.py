import os

import pytest
from starlette.testclient import TestClient

from app import main
from app.config.config import get_settings, Settings


def get_settings_override():
    return Settings(
        testing=1,
        database_hostname=os.environ.get("DATABASE_HOSTNAME"),
        database_port=os.environ.get("DATABASE_PORT"),
        database_name=os.environ.get("DATABASE_NAME"),
        database_username=os.environ.get("DATABASE_USERNAME"),
        database_password=os.environ.get("DATABASE_PASSWORD"),
    )


@pytest.fixture(scope="module")
def test_app():
    # set up
    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:
        # testing
        yield test_client

    # tear down
