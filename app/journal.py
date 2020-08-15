import sqlite3
from datetime import date
from dateutil.parser import parse

from app.config import c

def create_journal_entry_KO():
    instrument = input("The product ISIN/WKN is: ") or "n/a"
    buy_date = parse(input("Date trade entered: " ) or "n/a").date()
    sell_date = parse(input("Date trade closed: ") or "n/a").date()
    position_size = None
    while position_size is None:
        try:
            position_size = float(input("Position size of the trade: ") or 0)
        except Exception:
            print("Position size should be a number")
    comission = None
    while comission is None:
        try:
            comission = float(input("Overall fees/tax charged by broker: ") or 0)
        except Exception:
            print("Comission should be a number")
    exchange_rate = None
    while exchange_rate is None:
        try:
            exchange_rate = float(input("Excahge rate used by broker: ") or 0)
        except Exception:
            print("Exchange rate should be a number")
    entry_price = None
    while entry_price is None:
        try:
            entry_price = float(input("Your product's entry price is: ") or 0)
        except Exception:
            print("Enrty price should be a number")
    target_price = None
    while target_price is None:
        try:
            target_price = float(input("Target price of the product: ") or 0)
        except Exception:
            print("Target price should be a number")
    bid_price = None
    while bid_price is None:
        try:
            bid_price = float(input("Bid price of the product: ") or 0)
        except Exception:
            print("Bid price should be a number")
    atr = None
    while atr is None:
        try:
            atr = float(input("ATR of the product at entry time: ") or 0)
        except Exception:
            print("ATR should be a number")
    subscription_ratio = None
    while subscription_ratio is None:
        try:
            subscription_ratio = float(input("Subscription ratio of the instrument, if relevant: ") or 0)
        except Exception:
            print("Subscription ratio should be a number")
    knock_out = None
    while knock_out is None:
        try:
            knock_out = float(input("Knock-out threshold of the instrument, if relevant: ") or 0)
        except Exception:
            print("Knock-out threshold should be a number")
    multiplicator = None
    while multiplicator is None:
        try:
            multiplicator = float(input("Multiplicator of the instrument, if relevant: ") or 0)
        except Exception:
            print("Multiplicator should be a number")
    strike_price = None
    while strike_price is None:
        try:
            strike_price = float(input("Strike price of the instrument, if relevant: ") or 0)
        except Exception:
            print("Strike price should be a number")
    entry_underlying_price = None
    while entry_underlying_price is None:
        try:
            entry_underlying_price = float(input("Underlying price at entry, if relevant: ") or 0)
        except Exception:
            print("Underlying price at entry should be a number")
    entry_signal = input("Signal for trade entry: ") or "n/a"
    exit_signal = input("Signal for trade exit: ") or "n/a"
    comment = input("Comment on the success/failure of the trade: ") or "n/a"

    # calculate initial stop (atr factor = 2)
    initial_stop = (entry_price) - (atr * 2)
    # calculate risk per stock
    risk_per_stock = entry_price - initial_stop
    # calculate risk/reward ratio
    risk_reward_ratio = None
    while risk_reward_ratio is None:
        try:
            risk_reward_ratio = risk_per_stock/(target_price - entry_price)
        except ZeroDivisionError:
            risk_reward_ratio = 0
    # calculate buying sum
    buying_sum = position_size * entry_price
    # calculate buying sum with comission
    buying_sum_comission = (position_size * entry_price) + comission
    # calculate profit of trade
    trade_profit = (position_size * (bid_price - entry_price)) - comission

    try:
        sqliteConnection = sqlite3.connect(c.db_table_name)
        cursor = sqliteConnection.cursor()
        variables_KO = (instrument, buy_date, sell_date, buying_sum, buying_sum_comission, position_size, comission, trade_profit, risk_reward_ratio, entry_price, target_price, bid_price, atr, subscription_ratio, knock_out, multiplicator, strike_price, entry_underlying_price, initial_stop, risk_per_stock, entry_signal, exit_signal, comment)
        sql_KO = '''INSERT INTO journal(instrument, buy_date, sell_date, buying_sum, buying_sum_comission, position_size, comission, trade_profit, risk_reward_ratio, entry_price, target_price, bid_price, atr, subscription_ratio, knock_out, multiplicator, strike_price, entry_underlying_price, initial_stop, risk_per_stock, entry_signal, exit_signal, comment) VALUES(?,date(?),date(?),?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        cursor.execute(sql_KO, variables_KO)
        sqliteConnection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into journal")
    except sqlite3.Error as error:
        print("Failed to insert record into journal", error)
    finally:
        if (sqliteConnection):
            cursor.close()
            sqliteConnection.close()
            print("The SQLite connection is closed")

def create_journal_entry_stock():
    instrument = input("The product ISIN/WKN is: ") or "n/a"
    buy_date = parse(input("Date trade entered: " ) or "n/a").date()
    sell_date = parse(input("Date trade closed: " ) or "n/a").date()
    position_size = None
    while position_size is None:
        try:
            position_size = float(input("Position size of the trade: ") or 0)
        except Exception:
            print("Position size should be a number")
    comission = None
    while comission is None:
        try:
            comission = float(input("Overall fees/tax charged by broker: ") or 0)
        except Exception:
            print("Comission should be a number")
    exchange_rate = None
    while exchange_rate is None:
        try:
            exchange_rate = float(input("Excahge rate used by broker: ") or 0)
        except Exception:
            print("Exchange rate should be a number")
    entry_price = None
    while entry_price is None:
        try:
            entry_price = float(input("Your product's entry price is: ") or 0)
        except Exception:
            print("Enrty price should be a number")
    target_price = None
    while target_price is None:
        try:
            target_price = float(input("Target price of the product: ") or 0)
        except Exception:
            print("Target price should be a number")
    bid_price = None
    while bid_price is None:
        try:
            bid_price = float(input("Bid price of the product: ") or 0)
        except Exception:
            print("Bid price should be a number")
    atr = None
    while atr is None:
        try:
            atr = float(input("ATR of the product at entry time: ") or 0)
        except Exception:
            print("ATR should be a number")
    entry_signal = input("Signal for trade entry: ") or "n/a"
    exit_signal = input("Signal for trade exit: ") or "n/a"
    comment = input("Comment on the success/failure of the trade: ") or "n/a"

    initial_stop = (entry_price) - (atr * 2)
    # calculate risk per stock
    risk_per_stock = entry_price - initial_stop
    # calculate risk/reward ratio
    risk_reward_ratio = None
    while risk_reward_ratio is None:
        try:
            risk_reward_ratio = risk_per_stock/(target_price - entry_price)
        except ZeroDivisionError:
            risk_reward_ratio = 0
    # calculate buying sum
    buying_sum = position_size * entry_price
    # calculate buying sum with comission
    buying_sum_comission = (position_size * entry_price) + comission
    # calculate profit of trade
    trade_profit = None
    while trade_profit is None:
        try:
            trade_profit = (position_size * ((bid_price - entry_price)/exchange_rate) - comission)
        except ZeroDivisionError:
            trade_profit = (position_size * (bid_price - entry_price) - comission)

    try:
        sqliteConnection = sqlite3.connect(c.db_table_name)
        cursor = sqliteConnection.cursor()
        variables_stock = (instrument, buy_date, sell_date, buying_sum, buying_sum_comission, exchange_rate, position_size, comission, trade_profit, risk_reward_ratio, entry_price, target_price, bid_price, atr, initial_stop, risk_per_stock, entry_signal, exit_signal, comment)
        sql_stock = '''INSERT INTO journal(instrument, buy_date, sell_date, buying_sum, buying_sum_comission, position_size, comission, exchange_rate, trade_profit, risk_reward_ratio, entry_price, target_price, bid_price, atr, initial_stop, risk_per_stock, entry_signal, exit_signal, comment) VALUES(?,date(?),date(?),?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        cursor.execute(sql_stock, variables_stock)
        sqliteConnection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into journal")
    except sqlite3.Error as error:
        print("Failed to insert record into journal", error)
    finally:
        if (sqliteConnection):
            cursor.close()
            sqliteConnection.close()
            print("The SQLite connection is closed")

# def list_entries(journal_id):
#     print(f"all my trading entries in journal {journal_id}")
