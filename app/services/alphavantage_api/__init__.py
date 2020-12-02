import requests

def get_prices(symbol):
    return _get_from_api({
    "function": 'TIME_SERIES_DAILY',
    "outputsize": 'full',
    "symbol": symbol
    })
    

def get_earnings(symbol):
    return _get_from_api({
        "function" : 'EARNINGS',
        "symbol": symbol
    })

api_key = "MTR40FAMHPUR84HF"

def _get_from_api(params):
    default_params = {
        "apikey": api_key 
    }
    response = requests.get("https://www.alphavantage.co/query",
                            {
                                **default_params,
                                **params
                            }
                            )
    return response.json()