"""init exemption table

Revision ID: 831119d56ee6
Revises: da33afd37372
Create Date: 2020-09-04 18:51:55.939013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '831119d56ee6'
down_revision = 'da33afd37372'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'exemption',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('broker_id', sa.Integer, sa.ForeignKey("brokers.id")),
        sa.Column('exemption_amount', sa.Float),
        sa.Column('date', sa.Date),
        sa.Column('comment', sa.String)
    )

def downgrade():
    op.drop_table('exemption')
