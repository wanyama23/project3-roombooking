"""Added Booking

Revision ID: 00c39f8f16f5
Revises: 777a825d3517
Create Date: 2023-09-08 01:12:56.434101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00c39f8f16f5'
down_revision = '777a825d3517'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('check_in_date', sa.Date(), nullable=True),
    sa.Column('check_out_date', sa.Date(), nullable=True),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    # ### end Alembic commands ###
