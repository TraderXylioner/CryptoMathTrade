from typing import Generator

from ._api import API
from .core import get_depth_args, get_trades_args, get_ticker_args, ws_get_depth_args, ws_get_trades_args
from ...type import OrderBook, Trade, Ticker


class Market(API):
    def get_depth(self,
                  symbol: str,
                  limit: int | None = None,
                  recvWindow: int | None = None,
                  ):
        res = self._query(**get_depth_args(symbol=symbol, limit=limit, recvWindow=recvWindow)).json()['data']
        res['asks'] = res['asks'][::-1]
        return OrderBook.from_list(res)

    def get_trades(self,
                   symbol: str,
                   limit: int | None = None,
                   recvWindow: int | None = None,
                   ):
        res = self._query(**get_trades_args(symbol=symbol, limit=limit, recvWindow=recvWindow)).json()['data']
        return [Trade(id=trade.get('id'),
                      price=trade.get('price'),
                      qty=trade.get('qty'),
                      time=trade.get('time'),
                      isBuyerMaker=trade.get('buyerMaker'),
                      quoteQty=trade.get('quoteQty'),
                      isBestMatch=trade.get('isBestMatch'),
                      ) for trade in res]

    def get_ticker(self,
                   symbol: str | None = None
                   ):
        res = self._query(**get_ticker_args(symbol=symbol))
        res = res.json()['data']
        return [Ticker(symbol=ticker.get('symbol'),
                       priceChange=ticker.get('priceChange'),
                       priceChangePercent=ticker.get('priceChangePercent'),
                       openPrice=ticker.get('openPrice'),
                       highPrice=ticker.get('highPrice'),
                       lowPrice=ticker.get('lowPrice'),
                       lastPrice=ticker.get('lastPrice'),
                       volume=ticker.get('volume'),
                       quoteVolume=ticker.get('quoteVolume'),
                       openTime=ticker.get('openTime'),
                       closeTime=ticker.get('closeTime'),
                       ) for ticker in res]


class AsyncMarket(API):
    async def get_depth(self,
                        symbol: str,
                        limit: int | None = None,
                        recvWindow: int | None = None
                        ):
        res = await self._async_query(**get_depth_args(symbol=symbol, limit=limit, recvWindow=recvWindow))
        res = res['data']
        res['asks'] = res['asks'][::-1]
        return OrderBook.from_list(res)

    async def get_trades(self,
                         symbol: str,
                         limit: int | None = None):
        res = await self._async_query(**get_trades_args(symbol=symbol, limit=limit))
        res = res['data']
        return [Trade(id=trade.get('id'),
                      price=trade.get('price'),
                      qty=trade.get('qty'),
                      time=trade.get('time'),
                      isBuyerMaker=trade.get('buyerMaker'),
                      quoteQty=trade.get('quoteQty'),
                      isBestMatch=trade.get('isBestMatch'),
                      ) for trade in res]

    async def get_ticker(self,
                         symbol: str | None = None,
                         symbols: list | None = None):
        res = await self._async_query(**get_ticker_args(symbol=symbol, symbols=symbols))
        res = res['data']
        return [Ticker(symbol=ticker.get('symbol'),
                       priceChange=ticker.get('priceChange'),
                       priceChangePercent=ticker.get('priceChangePercent'),
                       openPrice=ticker.get('openPrice'),
                       highPrice=ticker.get('highPrice'),
                       lowPrice=ticker.get('lowPrice'),
                       lastPrice=ticker.get('lastPrice'),
                       volume=ticker.get('volume'),
                       quoteVolume=ticker.get('quoteVolume'),
                       openTime=ticker.get('openTime'),
                       closeTime=ticker.get('closeTime'),
                       ) for ticker in res]


class WebsSocketMarket(API):
    async def get_depth(self,
                        symbol: str,
                        ) -> Generator:
        return self._ws_query(**ws_get_depth_args(symbol=symbol))

    async def get_trades(self,
                         symbol: str,
                         ) -> Generator:
        return self._ws_query(**ws_get_trades_args(symbol=symbol))
