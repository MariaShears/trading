from pprint import pprint


def calculate_profit(instruments):
    total_profit = 0
    for instrument in instruments:
        total_profit = total_profit + instrument.trade_profit
    return total_profit


# import sqlite3
# from app.config import c

# def profits_summ():
#     try:
#         sqliteConnection = sqlite3.connect(c.db_table_name)
#         cursor = sqliteConnection.cursor()
#         sqlite_select_profit = """SELECT SUM(trade_profit) FROM journal"""
#         sqlite_select_profit_year = """SELECT SUM(trade_profit) FROM journal where strftime('%Y', sell_date) >= strftime('%Y', date('now')) """
#         sqlite_select_profit_month = """SELECT SUM(trade_profit) FROM journal where strftime('%Y %m', sell_date) >= strftime('%Y %m', date('now')) """
#         cursor.execute(sqlite_select_profit_year)
#         profits_year = cursor.fetchone()[0]
#         cursor.execute(sqlite_select_profit)
#         profits = cursor.fetchone()[0]
#         cursor.execute(sqlite_select_profit_month)
#         profits_month = cursor.fetchone()[0]
#         print("Total profits are:  ", profits)
#         print("Profits this year are: ", profits_year)
#         print("Profits this month are: ", profits_month)
#         cursor.close()

#     except sqlite3.Error as error:
#         print("Failed to read data from sqlite table", error)

#     finally:
#         if (sqliteConnection):
#             sqliteConnection.close()