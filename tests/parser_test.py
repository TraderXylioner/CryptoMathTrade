import asyncio

from CryptoMathTrade.exchange.binance import Market, AsyncMarket, Spot
from CryptoMathTrade.exchange.binance.core import get_orders_args, new_order_args, get_ticker_args
from CryptoMathTrade.type.order import TimeInForce, Side, OrderBook
from tests.settings import KEY, SECRET


async def main():
    tasks = [asyncio.create_task(AsyncMarket().get_depth('BTCUSDT')) for i in range(20)]
    for i in tasks:
        await i
        print(i.result())


# asyncio.run(main())

spot = Spot(KEY, SECRET)
market = Market()
# data = spot.get_orders('BTCUSDT')
data = market.get_depth(symbol='ETHUSDT').json()
data = OrderBook(data)
print(data)
