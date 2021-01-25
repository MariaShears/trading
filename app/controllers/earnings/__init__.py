from app.services import alphavantage_api
from . import transformer, calculations

def count_price_increase_cases_on_positive_surprise(symbol):
    raw_earnings = alphavantage_api.get_earnings(symbol)
    raw_prices = alphavantage_api.get_prices(symbol)
    earnings_with_prices = transformer.get_earnings_with_prices(raw_earnings, raw_prices)
    return calculations.count_price_increase_cases(earnings_with_prices)


def get_last_4_earnings(symbol):
    raw_earnings = alphavantage_api.get_earnings(symbol)
    clean_earnings_df = transformer.clean_earnings(raw_earnings)
    return clean_earnings_df.head(4)
