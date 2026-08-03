"""add pgvector extension and note_embeddings table

Revision ID: adbbc2e35262
Revises: 67fe673d8e3c
Create Date: 2026-07-29 10:47:44.922908

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'adbbc2e35262'
down_revision: Union[str, Sequence[str], None] = '67fe673d8e3c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.execute("CREATE EXTENSION IF NOT EXISTS vector")
    op.alter_column(
        "note_embeddings",
        "embedding_vector",
        type_=Vector(1536),
        postgresql_using="embedding_vector::vector",
    )
def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "note_embeddings",
        "embedding_vector",
        type_=postgresql.ARRAY(sa.Float()),
        postgresql_using="embedding_vector::float[]",
    )
    op.execute("DROP EXTENSION IF EXISTS vector")