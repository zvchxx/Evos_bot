"""Migration message

Revision ID: fb312985f492
Revises: 66b7edac6d36
Create Date: 2024-11-25 18:57:38.713870

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb312985f492'
down_revision: Union[str, None] = '66b7edac6d36'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
