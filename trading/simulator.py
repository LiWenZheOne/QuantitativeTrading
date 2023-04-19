# trading/simulator.py
from .abstract_trading import AbstractTrading

class Simulator(AbstractTrading):
    def __init__(self, api, symbol, balance):
        super().__init__(api, symbol, balance)

    def buy(self, price, amount):
        cost = price * amount

        if self.balance["quote"] >= cost:
            self.balance["quote"] -= cost
            self.balance["base"] += amount
            print(f"模拟买入：价格 {price}，数量 {amount}")
        else:
            print("模拟买入失败：余额不足")

    def sell(self, price, amount):
        if self.balance["base"] >= amount:
            self.balance["base"] -= amount
            self.balance["quote"] += price * amount
            print(f"模拟卖出：价格 {price}，数量 {amount}")
        else:
            print("模拟卖出失败：余额不足")

    def get_balance(self):
        return self.balance

    def update_balance(self):
        pass  # 模拟交易不需要更新余额，因为我们已经在buy/sell方法中手动更新了余额

    def get_current_price(self):
        ticker = self.api.get_ticker(self.symbol)
        return float(ticker["last"])
