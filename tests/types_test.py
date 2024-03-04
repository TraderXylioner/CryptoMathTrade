from CryptoMathTrade.types import Deal, Deals, OrderBook, Order

asks = [{'price': 10, 'volume': 1}, {'price': 11, 'volume': 1}]

deals = Deals(deals=asks)
print(deals)
