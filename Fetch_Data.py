"""
@Author: Swapnil Bhoyar
@Date: 2021-08-05
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-08-05
@Title : Fetching real time stock data using flume.
"""

import requests
from os import environ as env
from dotenv import load_dotenv
import time
import json

load_dotenv()
key = env['KEY']

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=1min&apikey=key'

r = requests.get(url)
parsed = r.json()
print(json.dumps(parsed, indent=2, sort_keys=True))
        