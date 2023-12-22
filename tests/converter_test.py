from converter import Converter
from type import Order

orders = [{'price': 100.0, 'volume': 0.1},
          {'price': 101.0, 'volume': 0.2},
          {'price': 102.0, 'volume': 0.3},
          {'price': 103.0, 'volume': 0.4},
          {'price': 104.0, 'volume': 0.5},
          ]

print(Converter.convert_price_from_order({'price': 100.0, 'volume': 0.1}, 100))
