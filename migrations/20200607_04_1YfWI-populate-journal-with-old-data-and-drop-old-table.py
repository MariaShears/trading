"""
populate journal with old data and drop old table
"""

from yoyo import step

__depends__ = {'20200607_03_cXWae'}

steps = [
    step("""
    INSERT INTO journal (instrument,
            buy_date,
            buying_sum,
            position_size,
            trade_profit,
            risk_reward_ratio,
            entry_price,
            target_price,
            bid_price,
            atr,
            subscription_ratio,
            knock_out,
            multiplicator,
            strike_price,
            entry_underlying_price,
            target_underlying_price,
            initial_stop,
            risk_per_stock,
            entry_signal,
            exit_signal,
            comment) 
            SELECT instrument,
            buy_date,
            buying_sum,
            position_size,
            trade_profit,
            risk_reward_ratio,
            entry_price,
            target_price,
            bid_price,
            atr,
            subscription_ratio,
            knock_out,
            multiplicator,
            strike_price,
            entry_underlying_price,
            target_underlying_price,
            initial_stop,
            risk_per_stock,
            entry_signal,
            exit_signal,
            comment FROM TempOldJournal;
    """)
]
