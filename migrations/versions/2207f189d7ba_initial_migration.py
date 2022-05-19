"""Initial Migration

Revision ID: 2207f189d7ba
Revises: 
Create Date: 2022-05-20 00:19:08.393338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2207f189d7ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('posted_on', sa.DateTime(), nullable=True))
    op.add_column('comments', sa.Column('post_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'posts', ['post_id'], ['post_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'post_id')
    op.drop_column('comments', 'posted_on')
    # ### end Alembic commands ###