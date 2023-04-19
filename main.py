import pandas as pd
from alpaca_trade_api.rest import REST, TimeFrame

import ccxt

class AlpacaClient:
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.rest_client = REST(api_key, secret_key)

    def get_historical_data(self, symbol, start_date, end_date, timeframe=TimeFrame.Day):
        bars = self.rest_client.get_bars(symbol, timeframe, start_date, end_date).df
        return bars

    def get_current_data(self, symbol):
        pass
     
    
if __name__ == "__main__":
    # API_KEY = 'PK4J0TQAERTOHMQMT2UE'
    # SECRET_KEY = 'FB1XCuT5B5ezDzdDZZmdSITooeJogNrjWul7CAge'

    # alpaca_client = AlpacaClient(API_KEY, SECRET_KEY)

    # historical_data = alpaca_client.get_historical_data("SPY", "2021-06-01", "2021-10-01")
    # print("Historical data:")
    # print(historical_data)


    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker('BTC/USDT')
    print(f"Ask price: {ticker['ask']}")
    print(f"Bid price: {ticker['bid']}")
