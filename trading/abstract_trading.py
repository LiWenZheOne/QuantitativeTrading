# trading/abstract_trading.py
from abc import ABC, abstractmethod

class AbstractTrading(ABC):
    @abstractmethod
    def __init__(self, api, symbol, balance):
        self.api = api
        self.symbol = symbol
        self.balance = balance

    @abstractmethod
    def buy(self, price, amount):
        pass

    @abstractmethod
    def sell(self, price, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def update_balance(self):
        pass

    @abstractmethod
    def get_current_price(self):
        pass

    # 可以根据需求添加其他交易相关的抽象方法
