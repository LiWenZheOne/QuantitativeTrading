# strategies/classic/macd.py
import numpy as np
import pandas as pd
from .. import AbstractStrategy

class MACDStrategy(AbstractStrategy):
    def __init__(self, short_window=12, long_window=26, signal_window=9):
        self.short_window = short_window
        self.long_window = long_window
        self.signal_window = signal_window
        self.macd = None
        self.macd_signal = None

    def analyze(self, data):
        df = pd.DataFrame(data)
        df['ewm_short'] = df['close'].ewm(span=self.short_window).mean()
        df['ewm_long'] = df['close'].ewm(span=self.long_window).mean()
        df['macd'] = df['ewm_short'] - df['ewm_long']
        df['macd_signal'] = df['macd'].ewm(span=self.signal_window).mean()

        self.macd = df['macd'].values
        self.macd_signal = df['macd_signal'].values

    def should_buy(self):
        if self.macd is None or self.macd_signal is None:
            return False

        if self.macd[-2] < self.macd_signal[-2] and self.macd[-1] > self.macd_signal[-1]:
            return True
        return False

    def should_sell(self):
        if self.macd is None or self.macd_signal is None:
            return False

        if self.macd[-2] > self.macd_signal[-2] and self.macd[-1] < self.macd_signal[-1]:
            return True
        return False
