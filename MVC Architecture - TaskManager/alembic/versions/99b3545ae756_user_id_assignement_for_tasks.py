"""User Id assignement for Tasks

Revision ID: 99b3545ae756
Revises: 
Create Date: 2026-10-12 21:31:01.698223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '99b3545ae756'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.add_column(
        'tasks',
        sa.Column('UserId', sa.Integer(), nullable=True)
    )

    op.create_foreign_key(
        'fk_tasks_user_id_users',
        'tasks',
        'users',
        ['UserId'],
        ['Id'],
        ondelete='CASCADE'
    )


def downgrade() -> None:
    op.drop_constraint(
        'fk_tasks_user_id_users',
        'tasks',
        type_='foreignkey'
    )

    op.drop_column('tasks', 'UserId')
