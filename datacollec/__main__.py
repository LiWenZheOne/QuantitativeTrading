import sys
import os
import time
import csv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))))
from QuantitativeTrading.data.api.bitget_api import BitgetAPI
from QuantitativeTrading.config import Config

config = Config()
api_key = config.api_key
api_secret = config.api_secret

# 创建 BitgetAPI 对象
api = BitgetAPI(api_key, api_secret)

# 指定数据存储的 CSV 文件
csv_file = os.path.join(os.path.dirname(__file__), "ticker_data.csv")

# 定义一个函数来将数据追加到 CSV 文件
def append_to_csv(data):
    with open(csv_file, mode="a", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)

# 在 CSV 文件中写入列名（仅在文件不存在时）
if not os.path.exists(csv_file):
    headers = [
        "Timestamp",
        "Symbol",
        "Last_Price",
        "Best_Ask",
        "Best_Bid",
        "Bid_Size",
        "Ask_Size",
        "High_24h",
        "Low_24h",
        "Price_Change_Percent",
        "Base_Volume",
        "Quote_Volume",
        "USDT_Volume",
        "Open_UTC",
        "Change_UTC",
        "Index_Price",
        "Funding_Rate",
        "Holding_Amount",
    ]
    append_to_csv(headers)

symbol = "BTCUSDT_UMCBL"  # 指定要获取的交易对

while True:
    response = api.get_ticker(symbol)
    if response["code"] == "00000":
        ticker_data = response["data"]
        timestamp = int(time.time())

        # 将数据写入 CSV 文件
        row_data = [
            timestamp,                                # Timestamp
            ticker_data["symbol"],                    # Symbol
            ticker_data["last"],                      # Last_Price
            ticker_data["bestAsk"],                   # Best_Ask
            ticker_data["bestBid"],                   # Best_Bid
            ticker_data["bidSz"],                     # Bid_Size
            ticker_data["askSz"],                     # Ask_Size
            ticker_data["high24h"],                   # High_24h
            ticker_data["low24h"],                    # Low_24h
            ticker_data["priceChangePercent"],        # Price_Change_Percent
            ticker_data["baseVolume"],                # Base_Volume
            ticker_data["quoteVolume"],               # Quote_Volume
            ticker_data["usdtVolume"],                # USDT_Volume
            ticker_data["openUtc"],                   # Open_UTC
            ticker_data["chgUtc"],                    # Change_UTC
            ticker_data["indexPrice"],                # Index_Price
            ticker_data["fundingRate"],               # Funding_Rate
            ticker_data["holdingAmount"],             # Holding_Amount
        ]
        append_to_csv(row_data)
    else:
        print(f"Error: {response['code']} - {response['msg']}")

    time.sleep(60)  # 每分钟执行一次
