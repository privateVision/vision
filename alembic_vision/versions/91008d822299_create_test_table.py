"""create test table

Revision ID: 91008d822299
Revises: 
Create Date: 2016-12-17 10:40:26.345335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91008d822299'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'test_account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(20), nullable=False),
        sa.Column('description', sa.String(255))
    )


def downgrade():
    op.drop_table('test_account')
