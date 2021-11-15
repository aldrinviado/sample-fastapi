"""empty message

Revision ID: 7a8a6bee7659
Revises: 046ede47f33e
Create Date: 2021-11-15 22:38:18.830825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a8a6bee7659'
down_revision = '046ede47f33e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),server_default='TRUE', nullable=False),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('NOW()')),)


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
