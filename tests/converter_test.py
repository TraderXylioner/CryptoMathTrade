from trader import Trader
from type import Order, OrderList, OrderBook

orders = [{'price': 100.0, 'volume': 0.1},
          {'price': 101.0, 'volume': 0.2},
          {'price': 102.0, 'volume': 0.3},
          {'price': 103.0, 'volume': 0.4},
          {'price': 104.0, 'volume': 0.5},
          ]


order1 = Order.from_dict({'price': 1010.0, 'volume': 0.1})
order2 = Order.from_dict({'price': 101.0, 'volume': 0.1})
order3 = Order.from_dict({'price': 102.0, 'volume': 0.1})
data = Trader.convert_price_in_orderbook(orders, 100)
print(data)
