# Top Reversed Alt Coins

1. First, calculate when Bitcoin bottomed out on Monday's Market Crash.
2. Using CoinGecko API get the top 200 Alt Coins.
3. Get price of Alt coins at the timestamp.
4. Get/Calculate the percentage change in the Alt coin from the timestamp for different time periods till 24-hour window using the Binance API.
5. Rank top 10 reversed alt coins for all the time periods.

Time Periods:
`1 min, 2 min, 5 min, 10 min, 15 min, 30 min, 1 hour, 2 hour, 4 hour, 8 hour, 16 hour, 24 hour`

### Install
```bash
python3 -m venv venv
source venv/bin/activate
pip install requests python-dotenv
```

## Notes
* Getting only hourly data from CG
* For price data I am using Binance API

### SMALL ERROR IN CALCULATION
Binance API only provides BTC/USDT pair, there will be error coming from USD/USDT pair.