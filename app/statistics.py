from pprint import pprint
import datetime


def calculate_profit(instruments):
    total_profit = 0
    for instrument in instruments:
        total_profit += instrument.trade_profit
    return total_profit

#TODO check math, wrong result
def calculate_profit_year(instruments):
    total_profit_year = 0
    for instrument in instruments:
        if instrument.sell_date.year == datetime.date.today().year:
            total_profit_year += total_profit_year + instrument.trade_profit
    return total_profit_year, datetime.date.today().year, instrument.sell_date.year

def calculate_profit_month(instruments):
    total_profit_month = 0
    for instrument in instruments:
        if (instrument.sell_date.year == datetime.date.today().year and instrument.sell_date.month == datetime.date.today().month):
            total_profit_month += total_profit_month + instrument.trade_profit
    return total_profit_month



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