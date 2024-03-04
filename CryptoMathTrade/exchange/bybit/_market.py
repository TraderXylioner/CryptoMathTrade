from typing import Generator

from ._api import API
from .core import get_depth_args, get_trades_args, get_ticker_args, ws_get_depth_args, ws_get_trades_args
from ...type import OrderBook, Trade, Ticker


class Market(API):
    def get_depth(self,
                  symbol: str,
                  limit: int | None = None,
                  ) -> OrderBook:
        """Get orderbook.

        GET /v5/market/orderbook

        https://bybit-exchange.github.io/docs/v5/market/orderbook

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 1; max 200. If limit > 200, then the response will truncate to 200.
        """
        res = self._query(**get_depth_args(symbol=symbol, limit=limit))
        res = res.json()['result']
        # return OrderBook.from_list(res.json())
        return res

    def get_trades(self,
                   symbol: str,
                   limit: int | None = None,
                   ) -> list[Trade]:
        """Recent Trades List
        Get recent trades (up to last 60).

        GET /v5/market/recent-trade

        https://bybit-exchange.github.io/docs/v5/market/recent-trade

        params:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 1; max 60.
        """
        res = self._query(**get_trades_args(symbol=symbol, limit=limit))
        # return [Trade(**trade) for trade in res.json()]
        return res.json()

    def get_ticker(self,
                   symbol: str | None = None,
                   ) -> Ticker:
        """24hr Ticker Price Change Statistics

        GET /v5/market/tickers

        https://bybit-exchange.github.io/docs/v5/market/tickers

        params:
            symbol (str, optional): the trading pair
        """
        res = self._query(**get_ticker_args(symbol=symbol))
        # return Ticker(**res.json())
        return res.json()


class AsyncMarket(API):
    async def get_depth(self,
                        symbol: str,
                        limit: int | None = None,
                        ) -> OrderBook:
        """Get orderbook.

        GET /v5/market/orderbook

        https://bybit-exchange.github.io/docs/v5/market/orderbook

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 1; max 200. If limit > 200, then the response will truncate to 200.
        """
        res = await self._async_query(**get_depth_args(symbol=symbol, limit=limit))
        # return OrderBook.from_list(res)
        return res

    async def get_trades(self,
                         symbol: str,
                         limit: int | None = None,
                         ) -> list[Trade]:
        """Recent Trades List
        Get recent trades (up to last 60).

        GET /v5/market/recent-trade

        https://bybit-exchange.github.io/docs/v5/market/recent-trade

        params:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 1; max 60.
        """
        res = await self._async_query(**get_trades_args(symbol=symbol, limit=limit))
        # return [Trade(**trade) for trade in res]
        return res.json()

    async def get_ticker(self,
                         symbol: str | None = None,
                         ) -> Ticker:
        """24hr Ticker Price Change Statistics

        GET /v5/market/tickers

        https://bybit-exchange.github.io/docs/v5/market/tickers

        params:
            symbol (str, optional): the trading pair
        """
        res = await self._async_query(**get_ticker_args(symbol=symbol))
        # return Ticker(**res)
        return res


class WebsSocketMarket(API):
    async def get_depth(self,
                        symbol: str,
                        limit: int | None = None,
                        ) -> Generator:
        """Partial Book Depth Streams

        Level 1 data, push frequency: 10ms
        Level 50 data, push frequency: 20ms
        Level 200 data, push frequency: 200ms

        Stream Names: orderbook.<limit>.<symbol>.

        param:
            symbol (str): the trading pair
        """
        return self._ws_query(**ws_get_depth_args(symbol=symbol, limit=limit))

    async def get_trades(self,
                         symbol: str,
                         ) -> Generator:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.

         Stream Name: publicTrade.<symbol>

         param:
            symbol (str): the trading pair

         Update Speed: Real-time
         """
        return self._ws_query(**ws_get_trades_args(symbol=symbol))
