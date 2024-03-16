from typing import Generator

from ._api import API
from .core import MarketCore, WSMarketCore
from CryptoMathTrade.types import OrderBook, Trade, Ticker, Order


class Market(API):
    def get_depth(self,
                  symbol: str,
                  limit: int | None = None,
                  ) -> OrderBook:
        """Get orderbook.

        GET /api/v3/depth

        https://binance-docs.github.io/apidocs/spot/en/#order-book

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 100; max 5000. If limit > 5000, then the response will truncate to 5000.
        """
        res = self._query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit))
        json_data = res.json()
        return OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in json_data['asks']],
                         bids=[Order(price=bid[0], volume=bid[1]) for bid in json_data['bids']],
                         )

    def get_trades(self,
                   symbol: str,
                   limit: int | None = None,
                   ) -> list[Trade]:
        """Recent Trades List
        Get recent trades (up to last 500).

        GET /api/v3/trades

        https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list

        params:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 500; max 1000.
        """
        res = self._query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit))
        return [Trade(**trade) for trade in res.json()]

    def get_ticker(self,
                   symbol: str | None = None,
                   symbols: list | None = None,
                   ) -> Ticker:
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair
            symbols (list, optional): list of trading pairs
        """
        res = self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol, symbols=symbols))
        return Ticker(**res.json())


class AsyncMarket(API):
    async def get_depth(self,
                        symbol: str,
                        limit: int | None = None,
                        ) -> OrderBook:
        """Get orderbook.

        GET /api/v3/depth

        https://binance-docs.github.io/apidocs/spot/en/#order-book

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 100; max 5000. If limit > 5000, then the response will truncate to 5000.
        """
        res = await self._async_query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit))
        json_data = res
        return OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in json_data['asks']],
                         bids=[Order(price=bid[0], volume=bid[1]) for bid in json_data['bids']],
                         )

    async def get_trades(self,
                         symbol: str,
                         limit: int | None = None,
                         ) -> list[Trade]:
        """Recent Trades List
        Get recent trades (up to last 500).

        GET /api/v3/trades

        https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list

        params:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 500; max 1000.
        """
        res = await self._async_query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit))
        return [Trade(**trade) for trade in res]

    async def get_ticker(self,
                         symbol: str | None = None,
                         symbols: list | None = None,
                         ) -> Ticker:
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair
            symbols (list, optional): list of trading pairs
        """
        res = await self._async_query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol, symbols=symbols))
        return Ticker(**res)


class WebsSocketMarket(API):
    async def get_depth(self,
                        symbol: str,
                        ) -> Generator:
        """Partial Book Depth Streams

        Top bids and asks, Valid are 5, 10, or 20.

        Stream Names: <symbol>@depth<levels> OR <symbol>@depth<levels>@100ms.

        param:
            symbol (str): the trading pair

        Update Speed: 1000ms or 100ms
        """
        return self._ws_query(**Core.ws_get_depth_args(symbol=symbol))

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
        return self._ws_query(**Core.ws_get_trades_args(symbol=symbol))
