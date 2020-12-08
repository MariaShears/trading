from . import Stock
import datetime

def get_instruments(session):
    return session.query(Stock).all()

def presentable_stock(stock):
    stock_properties = str(stock.__dict__)
    return (stock_properties, stock)

def filter_by_year(instruments):
    filtered_instruments = []
    for instrument in instruments:
        if instrument.sell_date.year == datetime.date.today().year:
            filtered_instruments.append(instrument)
    return filtered_instruments

def filter_by_month(instruments):
    filtered_instruments = []
    for instrument in instruments:
            if (instrument.sell_date.year == datetime.date.today().year and instrument.sell_date.month == datetime.date.today().month):
                filtered_instruments.append(instrument)
    return filtered_instruments
