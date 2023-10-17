import pprint
import json
import requests
import urllib2


try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

def get_data():
    url = 'https://api.worldtradingdata.com/api/v1/ticker_list'
    params = {
    'type': 'stocks',
    'api_token': 'FT2ITg2SQsYWUDYp5qo9DoA5trU4frDzD0BiFGsc8VMIm8ZLW4wnB3X9Hav5'
    }
    response = requests.request('GET', url, params=params)
    response.json()

    url = ("https://financialmodelingprep.com/api/v3/company/stock/list?apikey=bc90c8b2498094b8effc464c1bc45b50")
    pprint.pprint(get_jsonparsed_data(url)) 

def get_jsonparsed_data(url):

    response = urlopen(url)
    stocks_list = {response.read().decode("utf-8")}
    for stock in stocks_list:
        if (stocks_list['exchange'] == 'NasdaqGS'):
            nasdaq_stocks = nasdaq_stocks.append(stock)
    return json.loads(stocks_list[3])


