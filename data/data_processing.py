# data/data_processing.py
import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, api):
        self.api = api

    def get_historical_data(self, symbol, interval, start_time, end_time):
        # 从API获取历史K线数据
        raw_data = self.api.get_klines(symbol, interval, start_time, end_time)
        
        # 将原始数据转换为Pandas DataFrame
        data = pd.DataFrame(raw_data, columns=["open_time", "open", "high", "low", "close", "volume",
                                               "close_time", "quote_asset_volume", "number_of_trades",
                                               "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"])
        
        # 将时间戳转换为日期时间格式
        data["open_time"] = pd.to_datetime(data["open_time"], unit="ms")
        data["close_time"] = pd.to_datetime(data["close_time"], unit="ms")
        
        # 转换数据类型
        data[["open", "high", "low", "close", "volume", "quote_asset_volume", "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume"]] = \
            data[["open", "high", "low", "close", "volume", "quote_asset_volume", "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume"]].astype(float)
        data[["number_of_trades"]] = data[["number_of_trades"]].astype(int)
        
        # 添加技术指标
        data["SMA_10"] = data["close"].rolling(window=10).mean()  # 10日简单移动平均线
        data["SMA_20"] = data["close"].rolling(window=20).mean()  # 20日简单移动平均线
        data["RSI"] = self.calculate_rsi(data["close"])           # RSI指标

        # 删除无用列
        data = data.drop(columns=["ignore"])

        return data

    @staticmethod
    def calculate_rsi(close_prices, period=14):
        delta = close_prices.diff(1)
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
