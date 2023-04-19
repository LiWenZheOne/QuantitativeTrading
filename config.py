# config.py
class Config:
    def __init__(self):
        self.api_key = "YOUR_API_KEY"
        self.api_secret = "YOUR_API_SECRET"
        self.symbol = "BTCUSDT"
        self.interval = "1h"
        self.initial_balance = {
            "base": 1.0,  # 例如：BTC
            "quote": 1000.0  # 例如：USDT
        }
        self.cache_dir = "cache"
        # 添加其他全局配置信息，根据实际需求

    # 可以根据需要添加其他方法，例如从文件加载配置信息、保存配置信息等
