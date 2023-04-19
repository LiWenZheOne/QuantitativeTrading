# strategies/classic/moving_average.py
import numpy as np
import pandas as pd
from .. import AbstractStrategy

class MovingAverageStrategy(AbstractStrategy):
    def __init__(self, short_window=10, long_window=30):
        self.short_window = short_window
        self.long_window = long_window
        self.short_sma = None
        self.long_sma = None

    def analyze(self, data):
        df = pd.DataFrame(data)
        df['short_sma'] = df['close'].rolling(window=self.short_window).mean()
        df['long_sma'] = df['close'].rolling(window=self.long_window).mean()

        self.short_sma = df['short_sma'].values
        self.long_sma = df['long_sma'].values

    def should_buy(self):
        if self.short_sma is None or self.long_sma is None:
            return False

        if self.short_sma[-2] < self.long_sma[-2] and self.short_sma[-1] > self.long_sma[-1]:
            return True
        return False

    def should_sell(self):
        if self.short_sma is None or self.long_sma is None:
            return False

        if self.short_sma[-2] > self.long_sma[-2] and self.short_sma[-1] < self.long_sma[-1]:
            return True
        return False
