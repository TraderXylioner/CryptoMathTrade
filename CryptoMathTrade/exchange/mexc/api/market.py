from ..api.api import API
from ..deserialize import market as deserialize
from ..core import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 100):
        """Get orderbook.

        GET /api/v3/depth

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 5000. If limit > 5000, then the response will truncate to 5000.
        """
        response = validate_response(
            self._query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json()
        return deserialize.deserialize_depth(json_data, response)

    def get_trades(self, symbol: str, limit: int = 500):
        """Recent Trades List
        Get recent trades (up to last 500).

        GET /api/v3/trades

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#recent-trades-list

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 500; max 1000.
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

        GET /api/v3/ticker/24hr

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker(symbol=symbol))
        )
        json_data = response.json()
        return deserialize.deserialize_ticker(json_data, response)

    def get_symbols(self):
        """Query Symbols

        GET /open/api/v2/market/symbols

        https://mexcdevelop.github.io/apidocs/spot_v2_en/#all-symbols
        """
        response = validate_response(self._query(**MarketCore.get_symbols(self)))
        json_data = response.json()
        return deserialize.deserialize_symbols(json_data, response)

    def get_kline(
        self,
        symbol: str,
        interval: str,
        limit: int = 500,
        startTime: int = None,
        endTime: int = None,
    ):
        """Historical K-line data

        GET /api/v3/klines

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#kline-candlestick-data

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1m, 5m, 15m, 30m, 60m, 4h, 1d, 1W, 1M).

            limit (int, optional): Default 500; max 1000.

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
    async def get_depth(self, symbol: str, limit: int = 100):
        """Get orderbook.

        GET /api/v3/depth

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 5000. If limit > 5000, then the response will truncate to 5000.
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)

    async def get_trades(self, symbol: str, limit: int = 500):
        """Recent Trades List
        Get recent trades (up to last 500).

        GET /api/v3/trades

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#recent-trades-list

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 500; max 1000.
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

        GET /api/v3/ticker/24hr

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#24hr-ticker-price-change-statistics

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

    async def get_symbols(self):
        """Query Symbols

        GET /open/api/v2/market/symbols

        https://mexcdevelop.github.io/apidocs/spot_v2_en/#all-symbols
        """
        response = validate_response(
            await self._async_query(**MarketCore.get_symbols(self))
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
    ):
        """Historical K-line data

        GET /api/v3/klines

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#kline-candlestick-data

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1m, 5m, 15m, 30m, 60m, 4h, 1d, 1W, 1M).

            limit (int, optional): Default 500; max 1000.

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
#                         limit: int | None = 20,
#                         ) -> Generator:
#         """Partial Book Depth Streams
#
#         Stream Names: spot@public.limit.depth.v3.api@<symbol>@<level>.
#
#         https://mexcdevelop.github.io/apidocs/spot_v3_en/#partial-book-depth-streams
#
#         param:
#             symbol (str): the trading pair
#
#             limit (int, optional): limit the results. Valid are 5, 10, or 20.
#
#         """
#
#         async for response in self._ws_query(**WSMarketCore(headers=self.headers).get_depth_args(symbol=symbol,
#                                                                                                  limit=limit,
#                                                                                                  )):
#             json_data = json.loads(response)
#             if 'd' in json_data:
#                 yield _serialize_depth_for_ws(json_data['d'], response)
#
#     async def get_trades(self,
#                          symbol: str,
#                          ) -> Generator:
#         """Trade Streams
#
#          The Trade Streams push raw trade information; each trade has a unique buyer and seller.
#          Update Speed: Real-time
#
#          Stream Name: spot@public.deals.v3.api@<symbol>
#
#          https://mexcdevelop.github.io/apidocs/spot_v3_en/#trade-streams
#
#          param:
#             symbol (str): the trading pair
#          """
#         async for response in self._ws_query(**WSMarketCore(headers=self.headers).get_trades_args(symbol=symbol)):
#             json_data = json.loads(response)
#             if 'd' in json_data:
#                 yield _serialize_trades_for_ws(json_data['d']['deals'], response)
