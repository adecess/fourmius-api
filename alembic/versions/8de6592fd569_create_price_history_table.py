"""create price_history table

Revision ID: 8de6592fd569
Revises: 7af07e61080a
Create Date: 2023-10-28 19:53:14.501641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8de6592fd569'
down_revision: Union[str, None] = '7af07e61080a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('price_history',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('listing_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ondelete='CASCADE'),
                    sa.Column('price', sa.Integer(), nullable=False),
                    sa.Column('price_date', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    )
    pass


def downgrade() -> None:
    op.drop_table('price_history')
    pass
