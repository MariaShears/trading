import pandas as pd

from app.services import alphavantage_api
from . import transformer, calculations


def get_last_4_earnings(symbol):
    raw_earnings = alphavantage_api.get_earnings(symbol)
    clean_earnings_df = transformer.clean_earnings(raw_earnings)
    return clean_earnings_df.head(4)

def get_all_entries_df(all_entries):
    entries = pd.DataFrame(columns=[
    'id',
    'broker_id',
    'instrument',
    'buy_date',
    'sell_date',
    'buying_sum',
    'buying_sum_comission',
    'exchange_rate',
    'position_size',
    'comission',
    'trade_profit',
    'tax',
    'risk_reward_ratio',
    'entry_price',
    'target_price',
    'bid_price',
    'atr',
    'initial_stop',
    'risk_per_stock',
    'entry_signal',
    'exit_signal',
    'comment'])
    for entry in all_entries:
        entries = pd.concat([entries, pd.DataFrame(data={
            'id': entry.id,
            'broker_id': entry.broker_id,
            'instrument': entry.instrument,
            'buy_date': entry.buy_date,
            'sell_date': entry.sell_date,
            'buying_sum': entry.buying_sum,
            'buying_sum_comission': entry.buying_sum_comission,
            'exchange_rate': entry.exchange_rate,
            'position_size': entry.position_size,
            'comission': entry.comission,
            'trade_profit': entry.trade_profit,
            'tax': entry.tax,
            'risk_reward_ratio': entry.risk_reward_ratio,
            'entry_price': entry.entry_price,
            'target_price': entry.target_price,
            'bid_price': entry.bid_price,
            'atr': entry.atr,
            'initial_stop': entry.initial_stop,
            'risk_per_stock': entry.risk_per_stock,
            'entry_signal': entry.entry_signal,
            'exit_signal': entry.exit_signal,
            'comment': entry.comment
        }, index = [1])])
    return entries
