# data/cache.py
import os
import pickle

class Cache:
    def __init__(self, cache_dir="cache"):
        self.cache_dir = cache_dir

        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def get_cache_filename(self, symbol, interval, start_time, end_time):
        # 构建缓存文件名
        return f"{symbol}_{interval}_{start_time}_{end_time}.pkl"

    def save_to_cache(self, symbol, interval, start_time, end_time, data):
        # 保存数据到缓存
        filename = self.get_cache_filename(symbol, interval, start_time, end_time)
        filepath = os.path.join(self.cache_dir, filename)
        
        with open(filepath, "wb") as f:
            pickle.dump(data, f)

    def load_from_cache(self, symbol, interval, start_time, end_time):
        # 从缓存加载数据
        filename = self.get_cache_filename(symbol, interval, start_time, end_time)
        filepath = os.path.join(self.cache_dir, filename)

        if os.path.exists(filepath):
            with open(filepath, "rb") as f:
                return pickle.load(f)
        else:
            return None

    def is_cached(self, symbol, interval, start_time, end_time):
        # 检查数据是否已缓存
        filename = self.get_cache_filename(symbol, interval, start_time, end_time)
        filepath = os.path.join(self.cache_dir, filename)
        return os.path.exists(filepath)
