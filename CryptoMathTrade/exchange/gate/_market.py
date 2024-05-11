import json
from typing import Generator

from ._api import API
from ._serialization import _serialize_depth, _serialize_trades, _serialize_ticker
from .core import MarketCore, WSMarketCore
from ..utils import validate_response
from .._response import Response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 10) -> Response:
        """Get orderbook.

        GET /api/v4/spot/order_book

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-order-book

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 10; max 5000.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json()
        return _serialize_depth(json_data, response)

    def get_trades(self, symbol: str, limit: int = 100) -> Response:
        """Recent Trades List

        GET /api/v4/spot/trades

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-market-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 1000.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json()
        return _serialize_trades(json_data, response)

    def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v4/spot/tickers

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-ticker-information

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json()
        return _serialize_ticker(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = 10) -> Response:
        """Get orderbook.

        GET /api/v4/spot/order_book

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-order-book

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 10; max 5000.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json
        return _serialize_depth(json_data, response)

    async def get_trades(self, symbol: str, limit: int = 100) -> Response:
        """Recent Trades List

        GET /api/v4/spot/trades

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-market-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 1000.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json
        return _serialize_trades(json_data, response)

    async def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v4/spot/tickers

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-ticker-information

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json
        return _serialize_ticker(json_data, response)


class WebSocketMarket(API):
    async def get_depth(self,
                        symbol: str,
                        limit: int | None = 50,
                        interval: int | None = 1000,
                        ) -> Generator:
        """Partial Book Depth Streams

        Stream Names: spot.order_book_update

        https://www.gate.io/docs/developers/apiv4/ws/en/#changed-order-book-levels

        param:

            symbol (str): the trading pair

            limit (int, optional): limit the results. Valid are 5, 10, 20, 50 or 100.

            interval (int, optional): 1000ms or 100ms.

        """

        async for response in self._ws_query(
            **WSMarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit, interval=interval)):
            json_data = json.loads(response)
            if json_data['event'] == 'update':
                yield _serialize_depth(json_data['result'], response)

    async def get_trades(self,
                         symbol: str,
                         ) -> Generator:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: spot.trades

         https://www.gate.io/docs/developers/apiv4/ws/en/#client-subscription-2

         param:
            symbol (str): the trading pair
         """
        async for response in self._ws_query(
            **WSMarketCore(headers=self.headers).get_trades_args(symbol=symbol)):
            json_data = json.loads(response)
            if json_data['event'] == 'update':
                yield _serialize_trades([json_data['result']], response)
