"""pub id added in user

Revision ID: 3067de60e50a
Revises: 
Create Date: 2020-11-19 15:46:57.001491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3067de60e50a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('public_id', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'user', ['public_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'public_id')
    # ### end Alembic commands ###
