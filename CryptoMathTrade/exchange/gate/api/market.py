from .api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 10):
        """Get orderbook.

        GET /api/v4/spot/order_book

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-order-book

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 10; max 5000.
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

        GET /api/v4/spot/trades

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-market-trades

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 100; max 1000.
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

        GET /api/v4/spot/tickers

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-ticker-information

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker(symbol=symbol))
        )
        json_data = response.json()
        return deserialize.deserialize_ticker(json_data, response)

    def get_symbols(self):
        """Query Symbols

        GET /api/v4/spot/currency_pairs

        https://www.gate.io/docs/developers/apiv4/en/#list-all-currency-pairs-supported
        """
        response = validate_response(self._query(**MarketCore.get_symbols(self)))
        json_data = response.json()
        return deserialize.deserialize_symbols(json_data, response)

    def get_kline(
        self,
        symbol: str,
        interval: str = "30m",
        limit: int = 100,
        startTime: int = None,
        endTime: int = None,
    ):
        """Historical K-line data

        GET /api/v4/spot/candlesticks

        https://www.gate.io/docs/developers/apiv4/en/#market-candlesticks

        params:
            symbol (str): the trading pair.

            interval (str, optional):Default 30m; Time interval (10s, 1m, 5m, 15m, 30m, 1h, 4h, 8h, 1d, 7d, 30d).

            limit (int, optional): Default 100; max 1000.

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
    async def get_depth(self, symbol: str, limit: int = 10):
        """Get orderbook.

        GET /api/v4/spot/order_book

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-order-book

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 10; max 5000.
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

        GET /api/v4/spot/trades

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-market-trades

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 100; max 1000.
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

        GET /api/v4/spot/tickers

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-ticker-information

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned.
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_ticker(symbol=symbol)
            )
        )
        json_data = response.json
        return deserialize.deserialize_ticker(json_data, response)

    async def get_symbols(self):
        """Query Symbols

        GET /api/v4/spot/currency_pairs

        https://www.gate.io/docs/developers/apiv4/en/#list-all-currency-pairs-supported
        """
        response = validate_response(
            await self._async_query(**MarketCore.get_symbols(self))
        )
        json_data = response.json
        return deserialize.deserialize_symbols(json_data, response)

    async def get_kline(
        self,
        symbol: str,
        interval: str = "30m",
        limit: int = 100,
        startTime: int = None,
        endTime: int = None,
    ):
        """Historical K-line data

        GET /api/v4/spot/candlesticks

        https://www.gate.io/docs/developers/apiv4/en/#market-candlesticks

        params:
            symbol (str): the trading pair.

            interval (str, optional):Default 30m; Time interval (10s, 1m, 5m, 15m, 30m, 1h, 4h, 8h, 1d, 7d, 30d).

            limit (int, optional): Default 100; max 1000.

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
        json_data = response.json()
        return deserialize.deserialize_kline(json_data, response)


# TODO: WebSocketMarket

# class WebSocketMarket(API):
#     async def get_depth(self,
#                         symbol: str,
#                         limit: int | None = 50,
#                         interval: int | None = 1000,
#                         ) -> Generator:
#         """Partial Book Depth Streams
#
#         Stream Names: spot.order_book_update
#
#         https://www.gate.io/docs/developers/apiv4/ws/en/#changed-order-book-levels
#
#         param:
#
#             symbol (str): the trading pair
#
#             limit (int, optional): limit the results. Valid are 5, 10, 20, 50 or 100.
#
#             interval (int, optional): 1000ms or 100ms.
#
#         """
#
#         async for response in self._ws_query(
#             **WSMarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit, interval=interval)):
#             json_data = json.loads(response)
#             if json_data['event'] == 'update':
#                 yield _serialize_depth(json_data['result'], response)
#
#     async def get_trades(self,
#                          symbol: str,
#                          ) -> Generator:
#         """Trade Streams
#
#          The Trade Streams push raw trade information; each trade has a unique buyer and seller.
#          Update Speed: Real-time
#
#          Stream Name: spot.trades
#
#          https://www.gate.io/docs/developers/apiv4/ws/en/#client-subscription-2
#
#          param:
#             symbol (str): the trading pair
#          """
#         async for response in self._ws_query(
#             **WSMarketCore(headers=self.headers).get_trades_args(symbol=symbol)):
#             json_data = json.loads(response)
#             if json_data['event'] == 'update':
#                 yield _serialize_trades([json_data['result']], response)
