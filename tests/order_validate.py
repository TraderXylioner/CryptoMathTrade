from lib.order import Order
from lib.orderbook import OrderBook

orders = [{'price': 100.0, 'volume': 0.1},
          {'price': 101.0, 'volume': 0.2},
          {'price': 102.0, 'volume': 0.3},
          {'price': 103.0, 'volume': 0.4},
          {'price': 104.0, 'volume': 0.5},
          ]

new_orders = OrderBook(orders)
print(new_orders)
