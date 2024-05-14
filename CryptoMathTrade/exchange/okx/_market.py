import json
from typing import Generator

from ._api import API
from ._serialization import _serialize_depth, _serialize_trades, _serialize_ticker
from .core import MarketCore, WSMarketCore
from ..utils import validate_response
from .._response import Response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 1) -> Response:
        """Get orderbook.

        GET /api/v5/market/books

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 1; max 400.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json()['data'][0]
        return _serialize_depth(json_data, response)

    def get_trades(self, symbol: str, limit: int = 100) -> Response:
        """Recent Trades List

        Get recent trades (up to last 500).

        GET /api/v5/market/trades

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 500.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json()['data']
        return _serialize_trades(json_data, response)

    def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v5/market/ticker or /api/v5/market/tickers

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-ticker
        or
        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-tickers

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json()['data']
        return _serialize_ticker(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = 1) -> Response:
        """Get orderbook.

        GET /api/v5/market/books

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 1; max 400.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json['data'][0]
        return _serialize_depth(json_data, response)

    async def get_trades(self, symbol: str, limit: int = 100) -> Response:
        """Recent Trades List

        Get recent trades (up to last 500).

        GET /api/v5/market/trades

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 500.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json['data']
        return _serialize_trades(json_data, response)

    async def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v5/market/ticker or /api/v5/market/tickers

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-ticker
        or
        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-tickers

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json['data']
        return _serialize_ticker(json_data, response)


class WebSocketMarket(API):
    async def get_depth(self,
                        symbol: str,
                        ) -> Generator:
        """Partial Book Depth Streams

        Stream Names: books

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-order-book-channel

        param:
            symbol (str): the trading pair

        """
        async for response in self._ws_query(**WSMarketCore(headers=self.headers).get_depth_args(symbol=symbol)):
            json_data = json.loads(response)
            if 'data' in json_data:
                yield _serialize_depth(json_data['data'][0], response)

    async def get_trades(self,
                         symbol: str,
                         ) -> Generator:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: trades

         https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-trades-channel

         param:
            symbol (str): the trading pair
         """
        async for response in self._ws_query(**WSMarketCore(headers=self.headers).get_trades_args(symbol=symbol)):
            json_data = json.loads(response)
            if 'data' in json_data:
                yield _serialize_trades(json_data['data'], response)
