"""Added 

Revision ID: 777a825d3517
Revises: 23156cba7801
Create Date: 2023-09-06 20:20:47.730661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '777a825d3517'
down_revision = '23156cba7801'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_name', sa.String(), nullable=True),
    sa.Column('phone_number', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_number', sa.Integer(), nullable=True),
    sa.Column('room_type', sa.String(), nullable=True),
    sa.Column('room_capacity', sa.Integer(), nullable=True),
    sa.Column('room_price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('room_customer',
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('room_customer')
    op.drop_table('rooms')
    op.drop_table('customers')
    # ### end Alembic commands ###