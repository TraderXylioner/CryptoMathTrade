import asyncio
import gzip

from CryptoMathTrade.exchange.binance import WebsSocketMarket

if __name__ == '__main__':

    bingx_params = 'BTC-USDT@depth50'

    bingx_url = 'wss://open-api-ws.bingx.com/market'


    async def binance():
        socket = WebsSocketMarket()
        connect = await socket.get_trades('btcusdt')
        async for binance_data in connect:
            print(binance_data)

    async def bingx():
        async for bingx_data in bingx_API._ws_query(bingx_url, bingx_params):
            print(bingx_data)


async def main():
    tasks = [asyncio.create_task(bingx()), asyncio.create_task(binance())]
    for task in tasks:
        await task


asyncio.run(binance())
