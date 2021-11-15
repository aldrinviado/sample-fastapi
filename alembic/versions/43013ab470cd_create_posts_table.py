"""create posts table

Revision ID: 43013ab470cd
Revises: 
Create Date: 2021-11-15 22:06:05.852670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43013ab470cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id', sa.Integer(), nullable=False,primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
