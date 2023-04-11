from app.exemption.get import get_exemptions
from app.db import session
from app.instruments.get import get_instruments
from app.brokers.get import get_brokers
from app.instruments import Stock

def calculate_total_exemption(exemptions):
    sum_exemptions = 0
    for exemption in exemptions:
        sum_exemptions += exemption.exemption_amount
    return sum_exemptions


def calculate_running_exemption(exemptions):
    instruments = get_instruments(session)
    profits = 0
    for instrument in instruments:
        profits += instrument.trade_profit
        running_exemption = calculate_total_exemption(exemptions) - profits
    return running_exemption

def calculate_running_exemption_per_broker():
    brokers = get_brokers(session)
    for broker in brokers: 
        total_exemption = 0
        for exemption in broker.exemptions:
            total_exemption += exemption.exemption_amount
        total_profit = 0
        for stock in broker.stocks:
            total_profit += stock.trade_profit
        print(f"Broker {broker.name} has remaining exemption {total_exemption -  total_profit}")
