from datetime import datetime
from sqlalchemy import text, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship, Mapped


class Base(DeclarativeBase):
    pass


class Listing(Base):
    __tablename__ = 'listings'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    location: Mapped[str]
    type: Mapped[str]
    latest_price: Mapped[int]
    surface: Mapped[int]
    rooms: Mapped[int]
    listing_url: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=text('now()'))


class PriceHistory(Base):
    __tablename__ = 'price_history'

    id: Mapped[int] = mapped_column(primary_key=True)
    listing_id: Mapped[str] = mapped_column(ForeignKey("listings.id", ondelete="CASCADE"))
    price: Mapped[int]
    price_date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=text('now()'))
    listing: Mapped["Listing"] = relationship("Listing")
