"""
Add exchange_rate to journal table
"""

from yoyo import step

__depends__ = {'20200810_01_El0Mu-add-exchange-rate-to-journal-table'}

steps = [
    step("""
        CREATE TABLE journal (
            instrument TEXT,
            buy_date TEXT,
	        sell_date TEXT,
            buying_sum REAL,
	    buying_sum_comission REAL,
            position_size REAL,
	    comission REAL,
        exchange_rate REAL,
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
            comment TEXT); 
    """),
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
            comment FROM journal_old;
    """),
    step("DROP TABLE journal_old;")
]
