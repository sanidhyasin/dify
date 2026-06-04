"""merge mcp identity_mode and human_input_upload heads

Revision ID: 9f0a1b2c3d4e
Revises: 3df4dbcc1e21, 8d4c2a1b9f03
Create Date: 2026-06-04 20:00:00.000000

Joins two leaves that diverged from 121e7346074d after rebasing onto main:

  * 3df4dbcc1e21 — add identity_mode to mcp tool provider (this branch)
  * 8d4c2a1b9f03 — add human-input upload tables (landed on main)

No DDL — this is a routing-only merge so `alembic upgrade head` resolves
to a single revision.
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9f0a1b2c3d4e"
down_revision = ("3df4dbcc1e21", "8d4c2a1b9f03")
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
