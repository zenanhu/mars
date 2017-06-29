"""Init db

Revision ID: 8aed397c1741
Revises: 
Create Date: 2017-06-29 17:51:43.786015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8aed397c1741'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=300), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('time_created', sa.Integer(), nullable=True),
    sa.Column('time_modified', sa.Integer(), nullable=True),
    sa.Column('time_removed', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_engine='InnoDB'
    )
    op.create_table('Word',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=300), nullable=True),
    sa.Column('autoSugg', sa.TEXT(), nullable=True),
    sa.Column('Defi', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Word')
    op.drop_table('Message')
    # ### end Alembic commands ###