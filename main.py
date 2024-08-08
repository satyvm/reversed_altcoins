import requests
from dotenv import load_dotenv
import os

load_dotenv(override=True)
CG_API_KEY = os.getenv('CG_API_KEY')

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": CG_API_KEY
}

# server check
if requests.get("https://api.coingecko.com/api/v3/ping", headers=headers).status_code == 200:
    print("server is connected")
else:
    print("server is not connected")

# time when bitcoin bottomed out on Monday's Market Crash, in GMT+0530 (India Standard Time)
bitcoin_5aug_price = requests.get(
    "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from=1722796200&to=1722882600&precision=full",
    headers=headers
)
print(bitcoin_5aug_price.text)

# Mon Aug 05 2024 00:47:21 GMT+0530
# Mon Aug 05 2024 01:51:00 GMT+0530
# Mon Aug 05 2024 02:30:29 GMT+
# Mon Aug 05 2024 22:47:43 GMT+0530
# getting only hourly data from CG

# SMALL ERROR IN CALCULATION: as I am going to use Binance and it only provides BTC/USDT pair, there will be error coming from USD/USDT pair