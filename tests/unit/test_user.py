import pytest
from uuid import uuid4
from src.domain.user import User


@pytest.fixture
def user():
    return User(
        id=uuid4(),
        username="alex",
        email="alex@dupont.com",
        password_hash=b"Lapartdetartedetamaman1990",
    )


def test_bookmark_property(user):
    property_id = uuid4()
    user.bookmark_property(property_id)

    assert property_id in user.bookmarked_property_ids
    assert len(user.bookmarked_property_ids) == 1


def test_remove_bookmark(user):
    property_id = uuid4()
    user.bookmark_property(property_id)
    user.remove_bookmark(property_id)

    assert property_id not in user.bookmarked_property_ids
    assert len(user.bookmarked_property_ids) == 0


def test_has_bookmarked(user):
    property_id = uuid4()

    assert not user.has_bookmarked(property_id)

    user.bookmark_property(property_id)
    assert user.has_bookmarked(property_id)
