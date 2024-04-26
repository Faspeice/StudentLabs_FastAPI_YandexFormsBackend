"""mtm

Revision ID: 9d515cc4b2d2
Revises: 07228c998de0
Create Date: 2024-04-25 22:15:14.618108

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9d515cc4b2d2"
down_revision: Union[str, None] = "07228c998de0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("forms", "type")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "forms", sa.Column("type", sa.VARCHAR(), autoincrement=False, nullable=False)
    )
    # ### end Alembic commands ###