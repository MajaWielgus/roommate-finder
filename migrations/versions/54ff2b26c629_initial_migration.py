"""Initial migration

Revision ID: 54ff2b26c629
Revises: 
Create Date: 2025-04-28 18:05:09.211885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54ff2b26c629'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('offer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.Column('balcony', sa.Boolean(), nullable=True),
    sa.Column('smoking', sa.Boolean(), nullable=True),
    sa.Column('pets', sa.Boolean(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('offer')
    # ### end Alembic commands ###
