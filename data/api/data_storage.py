import os
import pandas as pd

def save_historical_data_to_csv(data, filename='historical_data.csv'):
    # 将数据转换为Pandas DataFrame
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

    # 设置文件路径（使用相对路径）
    filepath = os.path.join(os.path.dirname(__file__), filename)

    # 将数据存储到CSV文件中
    df.to_csv(filepath, index=False)

