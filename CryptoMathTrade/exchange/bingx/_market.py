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
        """Get orderbook.

        GET /openApi/spot/v1/market/depth

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20depth%20information

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 100; max 1000. If limit > 1000, then the response will truncate to 1000
            recvWindow (int, optional).
        """
        res = self._query(**get_depth_args(symbol=symbol, limit=limit, recvWindow=recvWindow))
        res = res.json()['data']
        res['asks'] = res['asks'][::-1]
        return OrderBook.from_list(res)

    def get_trades(self,
                   symbol: str,
                   limit: int | None = None,
                   recvWindow: int | None = None,
                   ):
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /openApi/spot/v1/market/trades

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20transaction%20records

        params:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 100; max 100
            recvWindow (int, optional).
        """
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
        """24hr Ticker Price Change Statistics

        GET /openApi/spot/v1/ticker/24hr

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#24-hour%20price%20changes

        params:
            symbol (str, optional): the trading pair.
        """
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
        """Get orderbook.

        GET /openApi/spot/v1/market/depth

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20depth%20information

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 100; max 1000. If limit > 1000, then the response will truncate to 1000
            recvWindow (int, optional).
        """
        res = await self._async_query(**get_depth_args(symbol=symbol, limit=limit, recvWindow=recvWindow))
        res = res['data']
        res['asks'] = res['asks'][::-1]
        return OrderBook.from_list(res)

    async def get_trades(self,
                         symbol: str,
                         limit: int | None = None):
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /openApi/spot/v1/market/trades

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20transaction%20records

        params:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 100; max 100
            recvWindow (int, optional).
        """
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
                         symbol: str | None = None
                         ):
        """24hr Ticker Price Change Statistics

        GET /openApi/spot/v1/ticker/24hr

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#24-hour%20price%20changes

        params:
            symbol (str, optional): the trading pair.
        """
        res = await self._async_query(**get_ticker_args(symbol=symbol))
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
        """Partial Book Depth Streams

        Top bids and asks.

        Stream Names: <symbol>@depth<levels>.

        param:
            symbol (str): the trading pair
        """
        return self._ws_query(**ws_get_depth_args(symbol=symbol))

    async def get_trades(self,
                         symbol: str,
                         ) -> Generator:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.

         Stream Name: <symbol>@trade

         param:
            symbol (str): the trading pair

         Update Speed: Real-time
         """
        return self._ws_query(**ws_get_trades_args(symbol=symbol))
