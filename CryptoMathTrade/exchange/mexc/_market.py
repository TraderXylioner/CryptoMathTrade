import json
from typing import Generator

from ._api import API
from ._serialization import _serialize_depth, _serialize_trades, _serialize_ticker, _serialize_depth_for_ws, \
    _serialize_trades_for_ws
from .core import MarketCore, WSMarketCore
from ..utils import validate_response
from .._response import Response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 100) -> Response:
        """Get orderbook.

        GET /api/v3/depth

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 5000. If limit > 5000, then the response will truncate to 5000.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json()
        return _serialize_depth(json_data, response)

    def get_trades(self, symbol: str, limit: int = 500) -> Response:
        """Recent Trades List

        Get recent trades (up to last 500).

        GET /api/v3/trades

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#recent-trades-list

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 500; max 1000.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json()
        return _serialize_trades(json_data, response)

    def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json()
        return _serialize_ticker(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = 100) -> Response:
        """Get orderbook.

        GET /api/v3/depth

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 5000. If limit > 5000, then the response will truncate to 5000.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json
        return _serialize_depth(json_data, response)

    async def get_trades(self, symbol: str, limit: int = 500) -> Response:
        """Recent Trades List

        Get recent trades (up to last 500).

        GET /api/v3/trades

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#recent-trades-list

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 500; max 1000.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json
        return _serialize_trades(json_data, response)

    async def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json
        return _serialize_ticker(json_data, response)


class WebSocketMarket(API):
    async def get_depth(self,
                        symbol: str,
                        limit: int | None = 20,
                        ) -> Generator:
        """Partial Book Depth Streams

        Stream Names: spot@public.limit.depth.v3.api@<symbol>@<level>.

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#partial-book-depth-streams

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Valid are 5, 10, or 20.

        """

        async for response in self._ws_query(**WSMarketCore(headers=self.headers).get_depth_args(symbol=symbol,
                                                                                                 limit=limit,
                                                                                                 )):
            json_data = json.loads(response)
            if 'd' in json_data:
                yield _serialize_depth_for_ws(json_data['d'], response)

    async def get_trades(self,
                         symbol: str,
                         ) -> Generator:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: spot@public.deals.v3.api@<symbol>

         https://mexcdevelop.github.io/apidocs/spot_v3_en/#trade-streams

         param:
            symbol (str): the trading pair
         """
        async for response in self._ws_query(**WSMarketCore(headers=self.headers).get_trades_args(symbol=symbol)):
            json_data = json.loads(response)
            if 'd' in json_data:
                yield _serialize_trades_for_ws(json_data['d']['deals'], response)
