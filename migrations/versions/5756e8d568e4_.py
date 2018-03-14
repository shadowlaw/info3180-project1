"""empty message

Revision ID: 5756e8d568e4
Revises: 91a64c90d854
Create Date: 2018-03-14 15:49:45.885948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5756e8d568e4'
down_revision = '91a64c90d854'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'users_email_key', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(u'users_email_key', 'users', ['email'])
    # ### end Alembic commands ###
