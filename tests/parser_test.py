import asyncio

from CryptoMathTrade.exchange import bingx
from CryptoMathTrade.exchange import binance
from CryptoMathTrade.exchange import okx
from tests.settings import BINANCE_KEY, BINANCE_SECRET


async def main():
    tasks = [asyncio.create_task(okx.AsyncMarket().get_ticker()) for i in range(1)]
    for i in tasks:
        await i
        print(i.result())


# asyncio.run(main())

binance_market = binance.Market()
bingx_market = bingx.Market()
okx_market = okx.Market()

binance_spot = binance.Spot(BINANCE_KEY, BINANCE_SECRET)
bingx_spot = bingx.Spot()
okx_spot = okx.Spot()


# data = okx_market.get_depth(symbol='BTC-USDT')
# print(data)
