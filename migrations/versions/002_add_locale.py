"""add locale

Revision ID: 002
Revises: 001
Create Date: 2025-03-12 20:01:46.698581

"""

from typing import Optional, Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "002"
down_revision: Optional[str] = "001"
branch_labels: Optional[Sequence[str]] = None
depends_on: Optional[Sequence[str]] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("locale", sa.String(length=2), nullable=False, server_default="en")
    )
    op.add_column(
        "users",
        sa.Column("bot_blocked", sa.Boolean(), nullable=False, server_default="false"),
    )
    op.drop_column("users", "language")
    op.drop_column("users", "blocked_at")
    op.drop_column("users", "language_code")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("language_code", sa.VARCHAR(), autoincrement=False, nullable=True)
    )
    op.add_column(
        "users",
        sa.Column(
            "blocked_at", postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "users", sa.Column("language", sa.VARCHAR(length=2), autoincrement=False, nullable=False)
    )
    op.drop_column("users", "bot_blocked")
    op.drop_column("users", "locale")
    # ### end Alembic commands ###
