from ._api import API
from .core import get_depth_args, get_trades_args, get_ticker_args, get_price_args, ws_get_depth_args, \
    ws_get_trades_args
from ...type import OrderBook, Trade, Price, Ticker


class Market(API):
    def get_depth(self,
                  symbol: str,
                  limit: int | None = None,
                  ):
        res = self._query(**get_depth_args(symbol=symbol, limit=limit))
        return OrderBook.from_list(res.json())

    def get_trades(self,
                   symbol: str,
                   limit: int | None = None,
                   ):
        res = self._query(**get_trades_args(symbol=symbol, limit=limit))
        return [Trade(**trade) for trade in res.json()]

    def get_price(self,
                  symbol: str | None = None,
                  symbols: list | None = None,
                  ):
        res = self._query(**get_price_args(symbol=symbol, symbols=symbols))
        return Price(**res.json())

    def get_ticker(self,
                   symbol: str | None = None,
                   symbols: list | None = None,
                   ):
        res = self._query(**get_ticker_args(symbol=symbol, symbols=symbols))
        return Ticker(**res.json())


class AsyncMarket(API):
    async def get_depth(self,
                        symbol: str,
                        limit: int | None = None,
                        ):
        res = await self._async_query(**get_depth_args(symbol=symbol, limit=limit))
        return OrderBook.from_list(res)

    async def get_trades(self,
                         symbol: str,
                         limit: int | None = None,
                         ):
        res = await self._async_query(**get_trades_args(symbol=symbol, limit=limit))
        return [Trade(**trade) for trade in res]

    async def get_price(self,
                        symbol: str | None = None,
                        symbols: list | None = None,
                        ):
        res = await self._async_query(**get_price_args(symbol=symbol, symbols=symbols))
        return Price(**res)

    async def get_ticker(self,
                         symbol: str | None = None,
                         symbols: list | None = None,
                         ):
        res = await self._async_query(**get_ticker_args(symbol=symbol, symbols=symbols))
        return Ticker(**res)


class WebsSocketMarket(API):
    async def get_depth(self,
                        symbol: str,
                        ):
        return self._ws_query(**ws_get_depth_args(symbol=symbol))

    async def get_trades(self,
                         symbol: str,
                         ):
        return self._ws_query(**ws_get_trades_args(symbol=symbol))
