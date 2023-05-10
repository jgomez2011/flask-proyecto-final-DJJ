"""empty message

Revision ID: 03d76e7dcb93
Revises: baa75eadfe5f
Create Date: 2023-05-09 22:47:16.165494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03d76e7dcb93'
down_revision = 'baa75eadfe5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_img', sa.String(length=200), nullable=False))
        batch_op.create_unique_constraint(None, ['product_img'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('product_img')

    # ### end Alembic commands ###
