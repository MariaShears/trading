"""
Create journal table
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
        CREATE TABLE journal (
            instrument TEXT,
            date TEXT,
            buying_sum REAL,
            position_size REAL,
            trade_profit REAL,
            risk_reward_ratio REAL,
            entry_price REAL,
            target_price REAL,
            bid_price REAL,
            atr REAL,
            subscription_ratio REAL,
            knock_out REAL,
            multiplicator REAL,
            strike_price REAL,
            entry_underlying_price REAL,
            target_underlying_price REAL,
            initial_stop REAL,
            risk_per_stock REAL,
            entry_signal TEXT,
            exit_signal TEXT,
            comment TEXT
        ) 
    """)
]
