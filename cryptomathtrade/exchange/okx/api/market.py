from ..api.api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 1):
        """Get orderbook.

        GET /api/v5/market/books

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 1; max 400.
        """
        response = validate_response(
            self._query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json()
        return deserialize.deserialize_depth(json_data, response)

    def get_trades(self, symbol: str, limit: int = 100):
        """Recent Trades List

        Get recent trades (up to last 500).

        GET /api/v5/market/trades

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 500.
        """
        response = validate_response(
            self._query(
                **MarketCore(headers=self.headers).get_trades(
                    symbol=symbol, limit=limit
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_trades(json_data, response)

    def get_ticker(self, symbol: str = None):
        """24hr Ticker Price Change Statistics

        GET /api/v5/market/ticker or /api/v5/market/tickers

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-ticker
        or
        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-tickers

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker(symbol=symbol))
        )
        json_data = response.json()
        return deserialize.deserialize_ticker(json_data, response)

    def get_symbols(self, symbol: str = None):
        """Query Symbols

        GET /api/v5/public/instruments

        https://www.okx.com/docs-v5/en/#public-data-rest-api-get-instruments

        params:
            symbol (str, optional): the trading pair
        """
        response = validate_response(
            self._query(**MarketCore.get_symbols(self, symbol=symbol))
        )
        json_data = response.json()
        return deserialize.deserialize_symbols(json_data, response)

    def get_kline(
        self,
        symbol: str,
        interval: str = None,
        limit: int = 100,
        startTime: int = None,
        endTime: int = None,
    ):
        """Historical K-line data

        GET /api/v5/market/history-candles

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-candlesticks-history

        params:
            symbol (str): the trading pair.

            interval (str, optional): Default 1m; Time interval (1s, 1m, 3m, 5m, 15m, 30m, 1H, 2H, 4H, 6H, 12H, 1D, 2D, 3D, 1W, 1M, 3M).

            limit (int, optional): Default 100; max 100.

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.
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
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_kline(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = 1):
        """Get orderbook.

        GET /api/v5/market/books

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 1; max 400.
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)

    async def get_trades(self, symbol: str, limit: int = 100):
        """Recent Trades List

        Get recent trades (up to last 500).

        GET /api/v5/market/trades

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 500.
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_trades(
                    symbol=symbol, limit=limit
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_trades(json_data, response)

    async def get_ticker(self, symbol: str = None):
        """24hr Ticker Price Change Statistics

        GET /api/v5/market/ticker or /api/v5/market/tickers

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-ticker
        or
        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-tickers

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_ticker(symbol=symbol)
            )
        )
        json_data = response.json
        return deserialize.deserialize_ticker(json_data, response)

    async def get_symbols(self, symbol: str = None):
        """Query Symbols

        GET /api/v5/public/instruments

        https://www.okx.com/docs-v5/en/#public-data-rest-api-get-instruments

        params:
            symbol (str, optional): the trading pair
        """
        response = validate_response(
            await self._async_query(**MarketCore.get_symbols(self, symbol=symbol))
        )
        json_data = response.json
        return deserialize.deserialize_symbols(json_data, response)

    async def get_kline(
        self,
        symbol: str,
        interval: str = None,
        limit: int = 100,
        startTime: int = None,
        endTime: int = None,
    ):
        """Historical K-line data

        GET /api/v5/market/history-candles

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-candlesticks-history

        params:
            symbol (str): the trading pair.

            interval (str, optional): Default 1m; Time interval (1s, 1m, 3m, 5m, 15m, 30m, 1H, 2H, 4H, 6H, 12H, 1D, 2D, 3D, 1W, 1M, 3M).

            limit (int, optional): Default 100; max 100.

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.
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
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_kline(json_data, response)


# TODO: WebSocketMarket

# class WebSocketMarket(API):
#     async def get_depth(self,
#                         symbol: str,
#                         ) -> Generator:
#         """Partial Book Depth Streams
#
#         Stream Names: books
#
#         https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-order-book-channel
#
#         param:
#             symbol (str): the trading pair
#
#         """
#         async for response in self._ws_query(**WSMarketCore(headers=self.headers).get_depth(symbol=symbol)):
#             json_data = json.loads(response)
#             if 'data' in json_data:
#                 yield _serialize_depth(json_data['data'][0], response)
#
#     async def get_trades(self,
#                          symbol: str,
#                          ) -> Generator:
#         """Trade Streams
#
#          The Trade Streams push raw trade information; each trade has a unique buyer and seller.
#          Update Speed: Real-time
#
#          Stream Name: trades
#
#          https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-trades-channel
#
#          param:
#             symbol (str): the trading pair
#          """
#         async for response in self._ws_query(**WSMarketCore(headers=self.headers).get_trades(symbol=symbol)):
#             json_data = json.loads(response)
#             if 'data' in json_data:
#                 yield _serialize_trades(json_data['data'], response)
