# strategies/abstract_strategy.py
from abc import ABC, abstractmethod

class AbstractStrategy(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def analyze(self, data):
        pass

    @abstractmethod
    def should_buy(self):
        pass

    @abstractmethod
    def should_sell(self):
        pass
