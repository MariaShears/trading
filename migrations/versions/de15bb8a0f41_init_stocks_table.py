"""init stocks table

Revision ID: de15bb8a0f41
Revises: 
Create Date: 2020-08-15 15:22:48.267410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de15bb8a0f41'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'stocks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
        sa.Column('entry_signal', sa.String(500)),
        sa.Column('exit_signal', sa.String(500)),
        sa.Column('comment', sa.String(500)),
        sa.Column('buying_sum', sa.Float()),
        sa.Column('buying_date', sa.Date()),
    )

def downgrade():
    op.drop_table('stocks')
