"""create shelters table

Revision ID: 28c0de53c7e2
Revises: 
Create Date: 2019-05-03 23:21:02.613538

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '28c0de53c7e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'shelters',
        sa.Column('shelter_uuid', UUID, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

def downgrade():
    op.drop_table('shelters')
