import os
import pandas as pd
import numpy as np

# 获取项目根目录
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 根据目录结构找到csv文件
csv_file = os.path.join(project_root, "datacollec", "ticker_data.csv")

def calculate_macd(df, short_span=12, long_span=26, signal_span=9):
    df["EMA_short"] = df["Close"].ewm(span=short_span, adjust=False).mean()
    df["EMA_long"] = df["Close"].ewm(span=long_span, adjust=False).mean()
    df["MACD"] = df["EMA_short"] - df["EMA_long"]
    df["Signal"] = df["MACD"].ewm(span=signal_span, adjust=False).mean()
    df["MACD_Histogram"] = df["MACD"] - df["Signal"]
    return df


def calculate_rsi(df, period=14):
    delta = df["Close"].diff()
    gains = delta.where(delta > 0, 0)
    losses = -delta.where(delta < 0, 0)
    avg_gain = gains.rolling(window=period).mean()
    avg_loss = losses.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rs))
    return df


# 读取原始数据
df = pd.read_csv(csv_file)

# 删除不需要的列
df.drop(
    ["Best_Ask", "Best_Bid", "Bid_Size", "Ask_Size", "Open_UTC", "Change_UTC", "Funding_Rate", "Holding_Amount"],
    axis=1,
    inplace=True,
)

# 重命名列以符合技术指标函数的要求
df.rename(columns={"Timestamp": "Date", "Last_Price": "Close"}, inplace=True)

# 计算MACD和RSI指标
df = calculate_macd(df)
df = calculate_rsi(df)

# 删除中间计算列
df.drop(["EMA_short", "EMA_long"], axis=1, inplace=True)

# 删除包含NaN值的行
df.dropna(inplace=True)

# 保存处理后的数据到新的CSV文件
processed_csv_file = os.path.join(os.path.dirname(__file__), "processed_data.csv")
df.to_csv(processed_csv_file, index=False)
