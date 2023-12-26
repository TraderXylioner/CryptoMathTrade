from CryptoMathTrade.trader import Trader
from CryptoMathTrade.type import ArbitrageDeal

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

order = ArbitrageDeal(100, 200, 100)
data = Trader.convert_price_in_orderbook(asks, 100)
print(data)
