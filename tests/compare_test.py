from converter import Converter
from type import Order, OrderList
from decimal import Decimal

asks = [{'price': 90.0, 'volume': 0.1},
          {'price': 91.0, 'volume': 0.2},
          {'price': 92.0, 'volume': 0.3},
          {'price': 93.0, 'volume': 0.4},
          {'price': 94.0, 'volume': 0.5}]

bids = [{'price': 100.0, 'volume': 0.2},
          {'price': 99.0, 'volume': 0.2},
          {'price': 98.0, 'volume': 0.3},
          {'price': 97.0, 'volume': 0.4},
          {'price': 96.0, 'volume': 0.5}]


order1 = Order.from_dict({'price': 100.0, 'volume': 1})
order2 = Order.from_dict({'price': 200.0, 'volume': 2})
# order3 = Order.from_dict({'price': 102.0, 'volume': 0.1})
# data = Converter.convert_price_from_orderbook(orders, 100)
data = Converter.calculate_spread(asks, bids, 0.01, 0.01)
print(data[0])
