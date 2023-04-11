import pandas as pd
import numpy as np
from pandas import json_normalize

def get_earnings_with_prices(raw_earnings, raw_prices):
    earnings = clean_earnings(raw_earnings)
    prices = _clean_prices(raw_prices)
    merged = prices.merge(earnings, on='reportedDate', how='left')
    _calculate_prices_next_previous_day(merged)
    _calculate_price_increase(merged)
    return merged

def clean_earnings(raw_earnings): 
    earnings_df = json_normalize(raw_earnings['quarterlyEarnings'])
    earnings_df = earnings_df[['reportedDate', 'surprise', 'surprisePercentage']]
    earnings_df['surprise'] = pd.to_numeric(earnings_df['surprise'], errors='coerce')
    earnings_df['surprisePercentage'] = pd.to_numeric(earnings_df['surprisePercentage'], errors='coerce')
    earnings_df['reportedDate'] = pd.to_datetime(earnings_df['reportedDate'])
    earnings_df.dropna(inplace=True)
    return earnings_df

def _clean_prices(raw_prices):
    prices_for_specified_stock = raw_prices['Time Series (Daily)']
    prices_df = pd.concat([pd.DataFrame([v]).assign(reportedDate=k)
                           for k, v in prices_for_specified_stock.items()])
    prices_df = prices_df.rename(columns={
                                 '1. open': 'open',
                                 '2. high': 'high',
                                 '3. low': 'low',
                                 '4. close': 'close',
                                 '5. volume': 'volume'
                                 })
    columns_to_convert = ['open', 'high', 'low', 'close', 'volume']
    prices_df[columns_to_convert] = prices_df[columns_to_convert].apply(
        pd.to_numeric, errors='coerce')
    prices_df['reportedDate'] = pd.to_datetime(prices_df['reportedDate'])
    return prices_df

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

def _calculate_price_increase(merged):
    merged.loc[:, 'price_increase'] = merged.apply(lambda x: True
                                                   if np.mean([x['open'], x['high']]) > np.mean([x['high_previous_day'], x['close_previous_day']])
                                                   or np.mean([x['open_next_day'], x['high_next_day']]) > np.mean([x['high_previous_day'], x['close_previous_day']])
                                                   else False, axis=1)
