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
        sa.Column('instrument', sa.String(500)),
        sa.Column('buy_date', sa.Date),
        sa.Column('sell_date', sa.Date),
        sa.Column('buying_sum', sa.Float),
        sa.Column('buying_sum_comission', sa.Float),
        sa.Column('exchange_rate', sa.Float),
        sa.Column('position_size', sa.Float),
        sa.Column('comission', sa.Float),
        sa.Column('trade_profit', sa.Float),
        sa.Column('risk_reward_ratio', sa.Float),
        sa.Column('entry_price', sa.Float),
        sa.Column('target_price', sa.Float),
        sa.Column('bid_price', sa.Float),
        sa.Column('atr', sa.Float),
        sa.Column('initial_stop', sa.Float),
        sa.Column('risk_per_stock', sa.Float),
        sa.Column('entry_signal', sa.String(500)),
        sa.Column('exit_signal', sa.String(500)),
        sa.Column('comment', sa.String(500)),
    )

def downgrade():
    op.drop_table('stocks')
