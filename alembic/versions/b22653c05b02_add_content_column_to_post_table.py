"""add content column to post table

Revision ID: b22653c05b02
Revises: 43013ab470cd
Create Date: 2021-11-15 22:19:07.041989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b22653c05b02'
down_revision = '43013ab470cd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content', sa.String(),nullable=False))


def downgrade():
    op.drop_column('posts','content')
    pass
