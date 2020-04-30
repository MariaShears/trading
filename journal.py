import click
import sqlite3

@click.command()

def journal():
    instrument = input("The product ISIN is: ")
    date = input("Date of the trade: ")
    position_size = float(input("Position size of the trade: "))
    entry_price = float(input("Your product's entry price is: "))
    target_price = float(input("Target price of the instrument: "))
    bid_price = float(input("Bid price of the instrument: "))
    atr = float(input("ATR of the instrument at entry time: "))
    subscription_ratio = float(input("Subscription ratio of the instrument, if relevant: "))
    knock_out = float(input("Knock-out threshold of the instrument, if relevant: "))
    multiplicator = float(input("Multiplicator of the instrument, if relevant: "))
    strike_price = float(input("Strike price of the instrument, if relevant: "))
    entry_underlying_price = float(input("Underlying price at entry, if relevant: "))
    entry_signal = input("Signal for trade entry: ")
    exit_signal = input("Signal for trade exit: ")
    comment = input("Comment on the success/failure of the trade: ")

    # canculate target price of product's underlying
    target_underlying_price = (target_price) * (multiplicator) * (strike_price)
    # calculate initial stop (atr factor = 2)
    initial_stop = (entry_price) - (atr * 2)
    # calculate risk per stock
    risk_per_stock = entry_price - initial_stop
    # calculate risk/reward ratio
    risk_reward_ratio = (target_price - entry_price) - risk_per_stock
    # calculate buying sum
    buying_sum = position_size * entry_price
    # calculate profit of trade
    trade_profit = position_size * (target_price - bid_price)

    try:
        sqliteConnection = sqlite3.connect('traders_journal.db')
        cursor = sqliteConnection.cursor()
        variables = (instrument, date, buying_sum, position_size, trade_profit, risk_reward_ratio, entry_price, target_price, bid_price, atr, subscription_ratio, knock_out, multiplicator, strike_price, entry_underlying_price, target_underlying_price, initial_stop, risk_per_stock, entry_signal, exit_signal, comment,)
        sql = '''INSERT INTO journal(instrument, date, buying_sum, position_size, trade_profit, risk_reward_ratio, entry_price, target_price, bid_price, atr, subscription_ratio, knock_out, multiplicator, strike_price, entry_underlying_price, target_underlying_price, initial_stop, risk_per_stock, entry_signal, exit_signal, comment) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        cursor.execute(sql, variables)
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


if __name__ == '__main__':
    journal()