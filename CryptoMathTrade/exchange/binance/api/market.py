import json

from .api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore, WebSocketMarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 100):
        """Get orderbook.

        GET /api/v3/depth

        https://binance-docs.github.io/apidocs/spot/en/#order-book

        params:
            symbol (str): the trading pair.

            limit (int, optional): Default 100; max 5000.
        """
        response = validate_response(
            self._query(**MarketCore.get_depth(self, symbol=symbol, limit=limit))
        )
        json_data = response.json()
        return deserialize.deserialize_depth(json_data, response)

    def get_trades(self, symbol: str, limit: int = 500):
        """Recent Trades List

        GET /api/v3/trades

        https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 500; max 1000.
        """
        response = validate_response(
            self._query(**MarketCore.get_trades(self, symbol=symbol, limit=limit))
        )
        json_data = response.json()
        return deserialize.deserialize_trades(json_data, response)

    def get_ticker(self, symbol: str = None, symbols: list = None):
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair

            or / and

            symbols (list, optional): list of trading pairs
        """
        response = validate_response(
            self._query(**MarketCore.get_ticker(self, symbol=symbol, symbols=symbols))
        )
        json_data = response.json()
        return deserialize.deserialize_ticker(json_data, response)

    def get_symbols(self, symbol: str = None, symbols: list = None):
        """Query Symbols

        GET /api/v3/exchangeInfo

        https://binance-docs.github.io/apidocs/spot/en/#exchange-information

        params:
            symbol (str, optional): the trading pair.

            or / and

            symbols (list, optional): list of trading pairs.
        """
        response = validate_response(
            self._query(**MarketCore.get_symbols(self, symbol=symbol, symbols=symbols))
        )
        json_data = response.json()
        return deserialize.deserialize_symbols(json_data, response)

    def get_kline(
        self,
        symbol: str,
        interval: str,
        limit: int = 500,
        startTime: int = None,
        endTime: int = None,
        timeZone: str = None,
    ):
        """Historical K-line data

        GET /api/v3/klines

        https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1s, 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M).

            limit (int, optional): Default 500; max 1000.

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.

            timeZone (str, optional): Default: 0 (UTC).
        """
        response = validate_response(
            self._query(
                **MarketCore.get_kline(
                    self,
                    symbol=symbol,
                    interval=interval,
                    limit=limit,
                    startTime=startTime,
                    endTime=endTime,
                    timeZone=timeZone,
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_kline(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = 100):
        """Get orderbook.

        GET /api/v3/depth

        https://binance-docs.github.io/apidocs/spot/en/#order-book

        params:
            symbol (str): the trading pair.

            limit (int, optional): Default 100; max 5000.
        """
        response = validate_response(
            await self._async_query(
                **MarketCore.get_depth(self, symbol=symbol, limit=limit)
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)

    async def get_trades(self, symbol: str, limit: int = 500):
        """Recent Trades List

        GET /api/v3/trades

        https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list

        params:
            symbol (str): the trading pair.

            limit (int, optional): Default 500; max 1000.
        """
        response = validate_response(
            await self._async_query(
                **MarketCore.get_trades(self, symbol=symbol, limit=limit)
            )
        )
        json_data = response.json
        return deserialize.deserialize_trades(json_data, response)

    async def get_ticker(self, symbol: str = None, symbols: list = None):
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair.

            or / and

            symbols (list, optional): list of trading pairs.
        """
        response = validate_response(
            await self._async_query(
                **MarketCore.get_ticker(self, symbol=symbol, symbols=symbols)
            )
        )
        json_data = response.json
        return deserialize.deserialize_ticker(json_data, response)

    async def get_symbols(self, symbol: str = None, symbols: list = None):
        """Query Symbols

        GET /api/v3/exchangeInfo

        https://binance-docs.github.io/apidocs/spot/en/#exchange-information

        params:
            symbol (str, optional): the trading pair.

            or / and

            symbols (list, optional): list of trading pairs.
        """
        response = validate_response(
            await self._async_query(
                **MarketCore.get_symbols(self, symbol=symbol, symbols=symbols)
            )
        )
        json_data = response.json
        return deserialize.deserialize_symbols(json_data, response)

    async def get_kline(
        self,
        symbol: str,
        interval: str,
        limit: int = 500,
        startTime: int = None,
        endTime: int = None,
        timeZone: str = None,
    ):
        """Historical K-line data

        GET /api/v3/klines

        https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1s, 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M).

            limit (int, optional): Default 500; max 1000.

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.

            timeZone (str, optional): Default: 0 (UTC).
        """
        response = validate_response(
            await self._async_query(
                **MarketCore.get_kline(
                    self,
                    symbol=symbol,
                    interval=interval,
                    limit=limit,
                    startTime=startTime,
                    endTime=endTime,
                    timeZone=timeZone,
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_kline(json_data, response)


class WebSocketMarket(API):
    async def get_depth(self, symbol: str, limit: int = 20, interval: int = 1000):
        """Partial Book Depth Streams

        Stream Names: <symbol>@depth<levels> OR <symbol>@depth<levels>@100ms.

        https://binance-docs.github.io/apidocs/spot/en/#partial-book-depth-streams

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Valid are 5, 10, or 20.

            interval (int, optional): 1000ms or 100ms.
        """
        async for response in self._ws_query(
            **WebSocketMarketCore.get_depth(
                self,
                symbol=symbol,
                limit=limit,
                interval=interval,
            )
        ):
            json_data = json.loads(response)
            if "result" not in json_data:
                yield deserialize.deserialize_depth(json_data, response)

    async def get_trades(self, symbol: str):
        """Trade Streams

        The Trade Streams push raw trade information; each trade has a unique buyer and seller.
        Update Speed: Real-time

        Stream Name: <symbol>@trade

        https://binance-docs.github.io/apidocs/spot/en/#trade-streams

        params:
           symbol (str): the trading pair.
        """
        async for response in self._ws_query(
            **WebSocketMarketCore.get_trades(self, symbol=symbol)
        ):
            json_data = json.loads(response)
            if "result" not in json_data:
                yield deserialize.deserialize_trades_for_ws(json_data, response)
