import requests
import pprint
import pandas as pd
import numpy as np
from app.cli_utils import get_required_string_from_cli
from pandas import json_normalize


def _get_earnings_from_api(symbol):
    function = 'EARNINGS'
    response = requests.get("https://www.alphavantage.co/query",
                            params={
                                "function": function,
                                "apikey": "MTR40FAMHPUR84HF",
                                "symbol": symbol
                            }
                            )
    return response.json()


def _get_sybmol_from_user():
    symbol = get_required_string_from_cli(
        'The stock exchange symbol of the stock is')
    return symbol


def _get_raw_earnings(symbol):
    earnings_for_specified_stock = _get_earnings_from_api(symbol)
    return earnings_for_specified_stock['quarterlyEarnings']


def get_last_4_earnings():
    symbol = _get_sybmol_from_user()
    raw_earnings = _get_raw_earnings(symbol)
    earnings_df = json_normalize(raw_earnings)[
        ['reportedDate', 'surprise', 'surprisePercentage']]
    earnings_df['surprise'] = pd.to_numeric(
        earnings_df['surprise'], errors='coerce')
    earnings_df['surprisePercentage'] = pd.to_numeric(
        earnings_df['surprisePercentage'], errors='coerce')
    earnings_df.dropna(inplace=True)
    earnings_df.sort_values(by=['reportedDate'], ascending=False, inplace=True)
    return earnings_df.head(4)


def _get_earnings(symbol):
    raw_earnings = _get_raw_earnings(symbol)
    earnings_df = json_normalize(raw_earnings)[
        ['reportedDate', 'surprise', 'surprisePercentage']]
    earnings_df['surprise'] = pd.to_numeric(
        earnings_df['surprise'], errors='coerce')
    earnings_df['surprisePercentage'] = pd.to_numeric(
        earnings_df['surprisePercentage'], errors='coerce')
    earnings_df['reportedDate'] = pd.to_datetime(earnings_df['reportedDate'])
    earnings_df.dropna(inplace=True)
    return earnings_df


def _get_prices_from_api(symbol):
    function = 'TIME_SERIES_DAILY'
    outputsize = 'full'
    response = requests.get("https://www.alphavantage.co/query",
                            params={
                                "function": function,
                                "apikey": "MTR40FAMHPUR84HF",
                                "symbol": symbol,
                                "outputsize": outputsize
                            }
                            )
    return response.json()


def _get_prices(symbol):
    prices_for_specified_stock = _get_prices_from_api(symbol)[
        'Time Series (Daily)']
    prices_df = pd.concat([pd.DataFrame([v]).assign(reportedDate=k)
                           for k, v in prices_for_specified_stock.items()])
    prices_df = prices_df.rename(columns={
                                 '1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. volume': 'volume'})
    columns_to_convert = ['open', 'high', 'low', 'close', 'volume']
    prices_df[columns_to_convert] = prices_df[columns_to_convert].apply(
        pd.to_numeric, errors='coerce')
    prices_df['reportedDate'] = pd.to_datetime(prices_df['reportedDate'])
    return prices_df


def _merge_earnings_prices(prices, earnings):
    merged = prices.merge(earnings, on='reportedDate', how='left')
    return merged


def _calculate_prices_next_previous_day(merged):
    merged['open_next_day'] = merged.open.shift(-1)
    merged['high_next_day'] = merged.high.shift(-1)
    merged['low_next_day'] = merged.low.shift(-1)
    merged['close_next_day'] = merged.close.shift(-1)
    merged['volume_next_day'] = merged.volume.shift(-1)
    merged['open_previous_day'] = merged.open.shift(+1)
    merged['high_previous_day'] = merged.high.shift(+1)
    merged['low_previous_day'] = merged.low.shift(+1)
    merged['close_previous_day'] = merged.close.shift(+1)
    merged['volume_previous_day'] = merged.volume.shift(+1)
    merged.dropna(inplace=True)
    return merged


def _calculate_price_increase(merged):
    merged.loc[:, 'price_increase'] = merged.apply(lambda x: True
                                                   if np.mean([x['open'], x['high']]) > np.mean([x['high_previous_day'], x['close_previous_day']])
                                                   or np.mean([x['open_next_day'], x['high_next_day']]) > np.mean([x['high_previous_day'], x['close_previous_day']])
                                                   else False, axis=1)


def count_price_increase_cases_on_positive_surprise():
    symbol = _get_sybmol_from_user()
    earnings = _get_earnings(symbol)
    prices = _get_prices(symbol)

    prices_earnings_df = _merge_earnings_prices(prices, earnings)
    _calculate_prices_next_previous_day(prices_earnings_df)
    _calculate_price_increase(prices_earnings_df)
    
    prices_earnings_df.where(prices_earnings_df['surprise'] > 0, inplace=True)
    return prices_earnings_df['price_increase'].astype('bool').value_counts()
