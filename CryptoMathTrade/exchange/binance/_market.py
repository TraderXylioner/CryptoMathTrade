from ._api import API
from .core import get_depth_args, get_trades_args, get_ticker_args, get_price_args
from ...type import OrderBook, Trades, Trade, Price, Ticker


class Market(API):
    def get_depth(self,
                  symbol: str,
                  limit: int | None = None
                  ):
        return self._query(**get_depth_args(symbol=symbol, limit=limit))

    def get_trades(self, symbol: str, limit: int | None = None):
        return self._query(**get_trades_args(symbol=symbol, limit=limit))

    def get_price(self,
                  symbol: str | None = None,
                  symbols: list | None = None):
        return self._query(**get_price_args(symbol=symbol, symbols=symbols))

    def get_ticker(self,
                   symbol: str | None = None,
                   symbols: list | None = None):
        return self._query(**get_ticker_args(symbol=symbol, symbols=symbols))


class AsyncMarket(API):
    async def get_depth(self,
                        symbol: str,
                        limit: int | None = None):
        return await self._async_query(**get_depth_args(symbol=symbol, limit=limit))

    async def get_trades(self,
                         symbol: str,
                         limit: int | None = None):
        return self._async_query(**get_trades_args(symbol=symbol, limit=limit))

    async def get_price(self,
                        symbol: str | None = None,
                        symbols: list | None = None):
        return self._async_query(**get_price_args(symbol=symbol, symbols=symbols))

    async def get_ticker(self,
                         symbol: str | None = None,
                         symbols: list | None = None):
        return self._async_query(**get_ticker_args(symbol=symbol, symbols=symbols))
