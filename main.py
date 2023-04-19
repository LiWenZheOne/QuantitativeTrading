from data.api.bitget_api import BitgetAPI
from data.data_processing import DataProcessor
from data.api.data_storage import save_historical_data_to_csv
import datetime

def main():
    # 创建BitgetAPI对象
    api_key = "your_api_key"
    secret_key = "your_secret_key"
    api = BitgetAPI(api_key, secret_key)

    # 创建DataProcessor对象
    processor = DataProcessor(api)

    # 获取历史K线数据
    symbol = "BTC_USDT"
    interval = "1day"
    start_time = datetime.datetime(2023, 1, 1)
    end_time = datetime.datetime(2023, 4, 1)
    data = processor.get_historical_data(symbol, interval, start_time, end_time)

    # 将数据保存到CSV文件中
    filename = "historical_data.csv"
    save_historical_data_to_csv(data, filename)

if __name__ == "__main__":
    main()