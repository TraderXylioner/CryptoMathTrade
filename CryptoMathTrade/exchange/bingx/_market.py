import gzip
import io
import json

from ._api import API
from ._deserialization import _deserialize_depth, _deserialize_trades, _deserialize_ticker, _deserialize_trades_for_ws, \
    _deserialize_symbols, _deserialize_kline
from .core import MarketCore, WebSocketMarketCore
from .._response import Response
from ..utils import validate_response
from ...types import OrderBook, Trade, Ticker, Kline, Symbol


class Market(API):
    def get_depth(self, symbol: str, limit: int = 100) -> Response[OrderBook, object]:
        """Get orderbook.

        GET /openApi/spot/v1/market/depth

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20depth%20information

        param:
            symbol (str): the trading pair.

            limit (int, optional): Default 100; max 1000.
        """
        response = validate_response(self._query(**MarketCore.get_depth(self, symbol=symbol, limit=limit)))
        json_data = response.json()
        return _deserialize_depth(json_data, response)

    def get_trades(self, symbol: str, limit: int = 100) -> Response[list[Trade], object]:
        """Recent Trades List

        GET /openApi/spot/v1/market/trades

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20transaction%20records

        params:
            symbol (str): the trading pair.

            limit (int, optional): Default 100; max 100.
        """
        response = validate_response(self._query(**MarketCore.get_trades(self, symbol=symbol, limit=limit)))
        json_data = response.json()
        return _deserialize_trades(json_data, response)

    def get_ticker(self, symbol: str = None) -> Response[list[Ticker], object]:
        """24hr Ticker Price Change Statistics

        GET /openApi/spot/v1/ticker/24hr

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#24-hour%20price%20changes

        params:
            symbol (str, optional): the trading pair.
        """
        response = validate_response(self._query(**MarketCore.get_ticker(self, symbol=symbol)))
        json_data = response.json()
        return _deserialize_ticker(json_data, response)

    def get_symbols(self, symbol: str = None) -> Response[list[Symbol], object]:
        """Query Symbols

        GET /openApi/spot/v1/common/symbols

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20Symbols

        params:
            symbol (str, optional): the trading pair.
        """
        response = validate_response(self._query(**MarketCore.get_symbols(self, symbol=symbol)))
        json_data = response.json()
        return _deserialize_symbols(json_data, response)

    def get_kline(self,
                  symbol: str,
                  interval: str,
                  limit: int = 500,
                  startTime: int = None,
                  endTime: int = None,
                  ) -> Response[list[Kline], object]:
        """Historical K-line data

        GET /openApi/market/his/v1/kline

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Historical%20K-line%20data

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M).

            limit (int, optional): Default 500; max 1000.

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.
        """
        response = validate_response(self._query(**MarketCore.get_kline(self,
                                                                        symbol=symbol,
                                                                        interval=interval,
                                                                        limit=limit,
                                                                        startTime=startTime,
                                                                        endTime=endTime,
                                                                        )))
        json_data = response.json()
        return _deserialize_kline(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = 100) -> Response[OrderBook, object]:
        """Get orderbook.

        GET /openApi/spot/v1/market/depth

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20depth%20information

        param:
            symbol (str): the trading pair.

            limit (int, optional): Default 100; max 1000.
        """
        response = validate_response(
            await self._async_query(**MarketCore.get_depth(self, symbol=symbol, limit=limit)))
        json_data = response.json
        return _deserialize_depth(json_data, response)

    async def get_trades(self, symbol: str, limit: int = 100) -> Response[list[Trade], object]:
        """Recent Trades List

        GET /openApi/spot/v1/market/trades

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20transaction%20records

        params:
            symbol (str): the trading pair.

            limit (int, optional): Default 100; max 100.
        """
        response = validate_response(
            await self._async_query(**MarketCore.get_trades(self, symbol=symbol, limit=limit)))
        json_data = response.json
        return _deserialize_trades(json_data, response)

    async def get_ticker(self, symbol: str = None) -> Response[list[Ticker], object]:
        """24hr Ticker Price Change Statistics

        GET /openApi/spot/v1/ticker/24hr

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#24-hour%20price%20changes

        params:
            symbol (str, optional): the trading pair.
        """
        response = validate_response(await self._async_query(**MarketCore.get_ticker(self, symbol=symbol)))
        json_data = response.json
        return _deserialize_ticker(json_data, response)

    async def get_symbols(self, symbol: str = None) -> Response[list[Symbol], object]:
        """Query Symbols

        GET /openApi/spot/v1/common/symbols

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20Symbols

        params:
            symbol (str, optional): the trading pair.
        """
        response = validate_response(
            await self._async_query(**MarketCore.get_symbols(self, symbol=symbol)))
        json_data = response.json
        return _deserialize_symbols(json_data, response)

    async def get_kline(self,
                        symbol: str,
                        interval: str,
                        limit: int = 500,
                        startTime: int = None,
                        endTime: int = None,
                        ) -> Response[list[Kline], object]:
        """Historical K-line data

        GET /openApi/market/his/v1/kline

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Historical%20K-line%20data

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M).

            limit (int, optional): Default 500; max 1000.

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.
        """
        response = validate_response(await self._async_query(**MarketCore.get_kline(self,
                                                                                    symbol=symbol,
                                                                                    interval=interval,
                                                                                    limit=limit,
                                                                                    startTime=startTime,
                                                                                    endTime=endTime,
                                                                                    )))
        json_data = response.json
        return _deserialize_kline(json_data, response)


class WebSocketMarket(API):
    async def get_depth(self, symbol: str, limit: int = 10) -> Response[OrderBook, object]:
        """Partial Book Depth Streams

        Stream Names: {symbol}@depth{limit}

        https://bingx-api.github.io/docs/#/en-us/spot/socket/market.html#Subscribe%20Market%20Depth%20Data

        param:
            symbol (str): the trading pair.

            limit (int, optional): Valid are 50.
        """
        async for response in self._ws_query(**WebSocketMarketCore.get_depth(self, symbol=symbol, limit=limit)):
            json_data = json.loads(gzip.GzipFile(fileobj=io.BytesIO(response), mode='rb').read().decode())
            if 'data' in json_data:
                yield _deserialize_depth(json_data, response)

    async def get_trades(self, symbol: str) -> Response[list[Trade], object]:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: {symbol}@trade

         https://bingx-api.github.io/docs/#/en-us/spot/socket/market.html#Subscription%20transaction%20by%20transaction

         param:
            symbol (str): the trading pair.
         """
        async for response in self._ws_query(**WebSocketMarketCore.get_trades(self, symbol=symbol)):
            json_data = json.loads(gzip.GzipFile(fileobj=io.BytesIO(response), mode='rb').read().decode())
            if 'data' in json_data:
                yield _deserialize_trades_for_ws(json_data, response)
