"""empty message

Revision ID: 802524e5e18a
Revises: 4f2e2c180af
Create Date: 2021-02-01 12:57:37.538647

"""

# revision identifiers, used by Alembic.
revision = '802524e5e18a'
down_revision = '4f2e2c180af'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('uid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account')
    # ### end Alembic commands ###
