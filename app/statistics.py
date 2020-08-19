from pprint import pprint
import datetime
from .instruments.get import filter_by_year
from .instruments.get import filter_by_month


from .instruments.get import filter_by_year
def print_calculations(instruments):
    calculation_pairs = [
      ("Your overall profit is:", calculate_profit(instruments)), 
      ("Your profit this year is:", calculate_profit_year(instruments)), 
      ("Your profit this month is:", calculate_profit_month(instruments)),    
    ]
    for (phrase, num) in calculation_pairs:
        print(f"{phrase} {num}")


def calculate_profit(instruments):
    total_profit = 0
    for instrument in instruments:
        total_profit += instrument.trade_profit
    return total_profit
    
def calculate_profit_year(instruments):
    yearly_instruments = filter_by_year(instruments)
    return calculate_profit(yearly_instruments)
    
def calculate_profit_month(instruments):
    monthly_instruments = filter_by_month(instruments)
    return calculate_profit(monthly_instruments)



