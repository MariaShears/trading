import requests
import pandas as pd
from app.cli_utils import get_required_string_from_cli
from pandas import json_normalize


def _get_earnings_from_api(symbol):
    function = 'EARNINGS'
    response = requests.get("https://www.alphavantage.co/query",
                            # headers={
                            #     "X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
                            #     "X-RapidAPI-Key": "MTR40FAMHPUR84HF"
                            # },
                            params={
                               "function": function,
                                "apikey": "MTR40FAMHPUR84HF",
                                "symbol": symbol
                            }
                            )
    return response.json()


def _get_raw_earnings():
    symbol = get_required_string_from_cli('The NASDAQ symbol of the stock is')
    earnings_for_specified_stock = _get_earnings_from_api(symbol)
    return earnings_for_specified_stock['quarterlyEarnings']

def get_earnings():
    raw_earnings = _get_raw_earnings()
    earnings_df = json_normalize(raw_earnings)[['reportedDate', 'surprise']]
    earnings_df['surprise'] = pd.to_numeric(earnings_df['surprise'], errors = 'coerce')
    earnings_df.dropna(inplace=True)
    return earnings_df 
