import gzip
import io
import json
from typing import Generator

from ._api import API
from ._serialization import _serialize_depth, _serialize_trades, _serialize_ticker, _serialize_trades_for_ws, \
    _serialize_symbols, _serialize_kline
from .core import MarketCore, WSMarketCore
from .._response import Response
from ..utils import validate_response


class Market(API):
    def get_depth(self,
                  symbol: str,
                  limit: int = 100,
                  ) -> Response:
        """Get orderbook.

        GET /openApi/spot/v1/market/depth

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20depth%20information

        param:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 100; max 1000.
        """
        response = validate_response(self._query(
            **MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json()
        return _serialize_depth(json_data['data'], response)

    def get_trades(self,
                   symbol: str,
                   limit: int = 100,
                   ) -> Response:
        """Recent Trades List

        GET /openApi/spot/v1/market/trades

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20transaction%20records

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 100; max 100.
        """
        response = validate_response(self._query(
            **MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json()
        return _serialize_trades(json_data['data'], response)

    def get_ticker(self,
                   symbol: str | None = None
                   ):
        """24hr Ticker Price Change Statistics

        GET /openApi/spot/v1/ticker/24hr

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#24-hour%20price%20changes

        params:
            symbol (str, optional): the trading pair.
        """
        response = validate_response(self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json()
        return _serialize_ticker(json_data['data'], response)

    def get_symbols(self,
                    symbol: str | None = None
                    ):
        """Query Symbols

        GET /openApi/spot/v1/common/symbols

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20Symbols

        params:
            symbol (str, optional): the trading pair.
        """
        response = validate_response(self._query(**MarketCore(headers=self.headers).get_symbols_args(symbol=symbol)))
        json_data = response.json()
        return _serialize_symbols(json_data['data'], response)

    def get_kline(self,
                  symbol: str,
                  interval: str,
                  startTime: int | None = None,
                  endTime: int | None = None,
                  limit: int | None = None,
                  ):
        """Historical K-line data

        GET /openApi/market/his/v1/kline

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Historical%20K-line%20data

        params:
            symbol (str): the trading pair

            interval (str): Time interval, reference field description

            startTime (int, optional): Start time

            endTime (int, optional): End time

            limit (int, optional): Default value: 500 Maximum value: 500
        """
        response = validate_response(self._query(**MarketCore(headers=self.headers).get_kline_args(symbol=symbol,
                                                                                                   interval=interval,
                                                                                                   startTime=startTime,
                                                                                                   endTime=endTime,
                                                                                                   limit=limit,
                                                                                                   )))
        json_data = response.json()
        return _serialize_kline(json_data['data'], response)


class AsyncMarket(API):
    async def get_depth(self,
                        symbol: str,
                        limit: int = 100,
                        ):
        """Get orderbook.

        GET /openApi/spot/v1/market/depth

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20depth%20information

        param:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 100; max 1000.
        """
        response = validate_response(await self._async_query(
            **MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json
        return _serialize_depth(json_data['data'], response)

    async def get_trades(self,
                         symbol: str,
                         limit: int = 100):
        """Recent Trades List

        GET /openApi/spot/v1/market/trades

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20transaction%20records

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 100; max 100.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json
        return _serialize_trades(json_data['data'], response)

    async def get_ticker(self,
                         symbol: str | None = None
                         ):
        """24hr Ticker Price Change Statistics

        GET /openApi/spot/v1/ticker/24hr

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#24-hour%20price%20changes

        params:
            symbol (str, optional): the trading pair.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json
        return _serialize_ticker(json_data['data'], response)

    async def get_symbols(self,
                          symbol: str | None = None
                          ):
        """Query Symbols

        GET /openApi/spot/v1/common/symbols

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20Symbols

        params:
            symbol (str, optional): the trading pair.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_symbols_args(symbol=symbol)))
        json_data = response.json
        return _serialize_symbols(json_data['data'], response)

    async def get_kline(self,
                        symbol: str,
                        interval: str,
                        startTime: int | None = None,
                        endTime: int | None = None,
                        limit: int | None = None,
                        ):
        """Historical K-line data

        GET /openApi/market/his/v1/kline

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Historical%20K-line%20data

        params:
            symbol (str): the trading pair

            interval (str): Time interval, reference field description

            startTime (int, optional): Start time

            endTime (int, optional): End time

            limit (int, optional): Default value: 500 Maximum value: 500
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_kline_args(symbol=symbol,
                                                                                      interval=interval,
                                                                                      startTime=startTime,
                                                                                      endTime=endTime,
                                                                                      limit=limit,
                                                                                      )))
        json_data = response.json
        return _serialize_kline(json_data['data'], response)


class WebSocketMarket(API):
    async def get_depth(self,
                        symbol: str,
                        limit: int | None = 10,
                        ) -> Generator:
        """Partial Book Depth Streams

        Stream Names: {symbol}@depth{limit}

        https://bingx-api.github.io/docs/#/en-us/spot/socket/market.html#Subscribe%20Market%20Depth%20Data

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Valid are 50.
        """
        async for response in self._ws_query(
                **WSMarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)):
            json_data = json.loads(gzip.GzipFile(fileobj=io.BytesIO(response), mode='rb').read().decode())
            if 'data' in json_data:
                yield _serialize_depth(json_data['data'], response)

    async def get_trades(self,
                         symbol: str,
                         ) -> Generator:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: {symbol}@trade

         https://bingx-api.github.io/docs/#/en-us/spot/socket/market.html#Subscription%20transaction%20by%20transaction

         param:
            symbol (str): the trading pair
         """
        async for response in self._ws_query(**WSMarketCore(headers=self.headers).get_trades_args(symbol=symbol)):
            json_data = json.loads(gzip.GzipFile(fileobj=io.BytesIO(response), mode='rb').read().decode())
            if 'data' in json_data:
                yield _serialize_trades_for_ws(json_data['data'], response)
