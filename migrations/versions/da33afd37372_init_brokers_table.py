"""init brokers table

Revision ID: da33afd37372
Revises: c7437799e5a8
Create Date: 2020-08-20 16:15:00.745972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da33afd37372'
down_revision = None
branch_labels = None
depends_on = None



def upgrade():
    op.create_table(
        'broker',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(500)),
        sa.Column('date', sa.Date),
        sa.Column('comment', sa.String(500))
    )

def downgrade():
    op.drop_table('broker')
