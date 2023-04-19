# data/api/abstract_api.py
from abc import ABC, abstractmethod

class AbstractAPI(ABC):
    @abstractmethod
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    @abstractmethod
    def get_ticker(self, symbol):
        pass

    @abstractmethod
    def get_depth(self, symbol):
        pass

    @abstractmethod
    def get_klines(self, symbol):
        pass
    # 其他API抽象方法
