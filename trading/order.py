# trading/order.py
from enum import Enum, auto

class OrderType(Enum):
    BUY = auto()
    SELL = auto()

class Order:
    def __init__(self, order_type, price, amount):
        self.order_type = order_type
        self.price = price
        self.amount = amount

    def __str__(self):
        return f"订单类型: {self.order_type.name}, 价格: {self.price}, 数量: {self.amount}"
