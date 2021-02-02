"""empty message

Revision ID: 285897c72c13
Revises: 802524e5e18a
Create Date: 2021-02-02 02:53:19.404100

"""

# revision identifiers, used by Alembic.
revision = '285897c72c13'
down_revision = '802524e5e18a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('site',
    sa.Column('site_id', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('site_name', sa.String(length=100), nullable=True),
    sa.Column('ems_id', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('site_id')
    )
    op.create_table('line',
    sa.Column('line_id', sa.String(length=50), nullable=False),
    sa.Column('site_id', sa.String(length=50), nullable=True),
    sa.Column('line_name', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['site_id'], ['site.site_id'], ),
    sa.PrimaryKeyConstraint('line_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('line')
    op.drop_table('site')
    # ### end Alembic commands ###
