import json
from typing import Generator

from ._api import API
from ._serialization import _serialize_depth, _serialize_trades, _serialize_ticker
from .core import MarketCore, WSMarketCore
from ..utils import validate_response
from .._response import Response


class Market(API):
    def get_depth(self, symbol: str) -> Response:
        """Get orderbook.

        GET /api/v1/market/orderbook/level2_100

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-part-order-book-aggregated-

        param:
            symbol (str): the trading pair

        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol)))
        json_data = response.json()['data']
        return _serialize_depth(json_data, response)

    def get_trades(self, symbol: str) -> Response:
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /api/v1/market/histories

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-trade-histories

        params:
            symbol (str): the trading pair
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol)))
        json_data = response.json()['data']
        return _serialize_trades(json_data, response)

    def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v1/market/stats or /api/v1/market/allTickers

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-24hr-stats
        or
        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-all-tickers

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json()['data']
        return _serialize_ticker(json_data, symbol, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str) -> Response:
        """Get orderbook.

        GET /api/v1/market/orderbook/level2_100

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-part-order-book-aggregated-

        param:
            symbol (str): the trading pair

        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol)))
        json_data = response.json['data']
        return _serialize_depth(json_data, response)

    async def get_trades(self, symbol: str) -> Response:
        """Recent Trades List

        Get recent trades (up to last 100).

        GET /api/v1/market/histories

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-trade-histories

        params:
            symbol (str): the trading pair
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol)))
        json_data = response.json['data']
        return _serialize_trades(json_data, response)

    async def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v1/market/stats or /api/v1/market/allTickers

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-24hr-stats
        or
        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-all-tickers

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json['data']
        return _serialize_ticker(json_data, symbol, response)


class WebSocketMarket(API):
    def __init__(self, token):
        super().__init__()
        self.token = token

    async def get_depth(self,
                        symbol: str,
                        limit: int | None = 50,
                        ) -> Generator:
        """Partial Book Depth Streams

        Stream Names: /spotMarket/level2Depth{limit}:{symbol}

        https://www.kucoin.com/docs/websocket/spot-trading/public-channels/level2-5-best-ask-bid-orders

        param:

            symbol (str): the trading pair

            limit (int, optional): limit the results. Valid are 5 or 50.

        """

        async for response in self._ws_query(
            **WSMarketCore(headers=self.headers, token=self.token).get_depth_args(symbol=symbol,
                                                                                  limit=limit,
                                                                                  )):
            json_data = json.loads(response)
            if 'data' in json_data:
                yield _serialize_depth(json_data['data'], response)

    async def get_trades(self,
                         symbol: str,
                         ) -> Generator:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: /market/match:{symbol}

         https://www.kucoin.com/docs/websocket/spot-trading/public-channels/match-execution-data

         param:
            symbol (str): the trading pair
         """
        async for response in self._ws_query(
            **WSMarketCore(headers=self.headers, token=self.token).get_trades_args(symbol=symbol)):
            json_data = json.loads(response)
            if 'data' in json_data:
                yield _serialize_trades([json_data['data']], response)
