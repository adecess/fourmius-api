"""create listings table

Revision ID: 7af07e61080a
Revises:
Create Date: 2023-10-28 19:40:49.479662

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7af07e61080a"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "listings",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("location", sa.String(), nullable=False),
        sa.Column("type", sa.String(), nullable=False),
        sa.Column("latest_price", sa.Integer(), nullable=False),
        sa.Column("surface", sa.Integer(), nullable=False),
        sa.Column("rooms", sa.Integer(), nullable=False),
        sa.Column("listing_url", sa.String(), nullable=False, unique=True),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    pass


def downgrade() -> None:
    op.drop_table("listings")
    pass
