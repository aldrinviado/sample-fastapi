"""add foreign key to posts table

Revision ID: 046ede47f33e
Revises: 2b6e365b3ab2
Create Date: 2021-11-15 22:29:44.964553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '046ede47f33e'
down_revision = '2b6e365b3ab2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk',source_table="posts", referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk',table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
