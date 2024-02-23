from CryptoMathTrade.trader import calculate_spread
from CryptoMathTrade.types import Order

asks = [Order.model_validate({'price': 10, 'volume': 10}), Order.model_validate({'price': 11, 'volume': 10})]
bids = [Order.model_validate({'price': 11, 'volume': 10}), Order.model_validate({'price': 10, 'volume': 10})]

res = calculate_spread(asks, bids, 0.001, 0.001)
print(res)
