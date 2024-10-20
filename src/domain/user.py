from typing import Set
from uuid import UUID


class User:
    def __init__(self, id: UUID, username: str, email: str, password_hash: bytes):
        self.id: UUID = id
        self.username: str = username
        self.email: str = email
        self.password_hash: bytes = password_hash
        self.bookmarked_property_ids: Set[UUID] = set()

    def bookmark_property(self, property_id: UUID):
        self.bookmarked_property_ids.add(property_id)

    def remove_bookmark(self, property_id: UUID):
        self.bookmarked_property_ids.discard(property_id)

    def has_bookmarked(self, property_id: UUID) -> bool:
        return property_id in self.bookmarked_property_ids
