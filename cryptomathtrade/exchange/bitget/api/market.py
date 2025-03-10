from .api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 150, type: str = None):
        """Get orderbook.

        GET /api/v2/spot/market/orderbook

        https://www.bitget.com/api-doc/spot/market/Get-Orderbook

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 150; max 150.

            type (str, optional) The value enums：step0，step1，step2，step3，step4，step5. Default: step0.
        """
        response = validate_response(
            self._query(
                **MarketCore(headers=self.headers).get_depth(
                    symbol=symbol, limit=limit, type=type
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_depth(json_data, response)

    def get_trades(self, symbol: str, limit: int = 100):
        """Recent Trades List

        GET /api/v2/spot/market/fills

        https://www.bitget.com/api-doc/spot/market/Get-Recent-Trades

        params:
            symbol (str): the trading pair.

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

        GET /api/v2/spot/market/tickers

        https://www.bitget.com/api-doc/spot/market/Get-Tickers

        params:
            symbol (str, optional): the trading pair.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker(symbol=symbol))
        )
        json_data = response.json()
        return deserialize.deserialize_ticker(json_data, response)

    def get_symbols(self, symbol: str = None):
        """Query Symbols

        GET /api/v2/spot/public/symbols

        https://www.bitget.com/api-doc/spot/market/Get-Symbols

        params:
            symbol (str, optional): the trading pair.
        """
        response = validate_response(
            self._query(**MarketCore.get_symbols(self, symbol=symbol))
        )
        json_data = response.json()
        return deserialize.deserialize_symbols(json_data, response)

    def get_kline(
        self,
        symbol: str,
        interval: str,
        limit: int = 100,
        startTime: int = None,
        endTime: int = None,
    ):
        """Historical K-line data

        GET /api/v2/spot/market/candles

        https://www.bitget.com/api-doc/spot/market/Get-Candle-Data

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1m, 3m, 5m can query for one month,15m can query for 52 days,30m can query for 62 days,1H can query for 83 days,2H can query for 120 days,4H can query for 240 days,6H can query for 360 days.).

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
    async def get_depth(self, symbol: str, limit: int = 150, type: str = None):
        """Get orderbook.

        GET /api/v2/spot/market/orderbook

        https://www.bitget.com/api-doc/spot/market/Get-Orderbook

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 150; max 150.

            type (str, optional) The value enums：step0，step1，step2，step3，step4，step5. Default: step0.
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_depth(
                    symbol=symbol, limit=limit, type=type
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)

    async def get_trades(self, symbol: str, limit: int = 100):
        """Recent Trades List

        GET /api/v2/spot/market/fills

        https://www.bitget.com/api-doc/spot/market/Get-Recent-Trades

        params:
            symbol (str): the trading pair.

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

        GET /api/v2/spot/market/tickers

        https://www.bitget.com/api-doc/spot/market/Get-Tickers

        params:
            symbol (str, optional): the trading pair.
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

        GET /api/v2/spot/public/symbols

        https://www.bitget.com/api-doc/spot/market/Get-Symbols

        params:
            symbol (str, optional): the trading pair.
        """
        response = validate_response(
            await self._async_query(**MarketCore.get_symbols(self, symbol=symbol))
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

        GET /api/v2/spot/market/candles

        https://www.bitget.com/api-doc/spot/market/Get-Candle-Data

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1m, 3m, 5m can query for one month,15m can query for 52 days,30m can query for 62 days,1H can query for 83 days,2H can query for 120 days,4H can query for 240 days,6H can query for 360 days.).

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


# TODO:  WebSocketMarket

# class WebSocketMarket(API):
#     async def get_depth(self,
#                         symbol: str,
#                         limit: int | None = None,
#                         ) -> Generator:
#         """Partial Book Depth Streams
#
#         Stream Names: books{limit}
#
#         https://www.bitget.com/api-doc/spot/websocket/public/Depth-Channel
#
#         param:
#
#             symbol (str): the trading pair
#
#             limit (int, optional): limit the results. Valid are 1, 5 or 15.
#
#
#         books: Push the full snapshot data for the first time, push update afterwards, that is, if there is a change in depth, the depth data that has changed will be pushed.
#         books1: 1 depth level will be pushed every time(snapshot).
#         books5: 5 depth levels will be pushed every time(snapshot).
#         books15: 15 depth levels will be pushed every time(snapshot).
#
#         """
#         async for response in self._ws_query(
#                 **WSMarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)):
#             json_data = json.loads(response)
#             if 'data' in json_data:
#                 yield _deserialize_depth(json_data['data'][0], response)
#
#     async def get_trades(self,
#                          symbol: str,
#                          ) -> Generator:
#         """Trade Streams
#
#          The Trade Streams push raw trade information; each trade has a unique buyer and seller.
#          Update Speed: Real-time
#
#          Stream Name: trade
#
#         https://www.bitget.com/api-doc/spot/websocket/public/Trades-Channel
#
#          param:
#             symbol (str): the trading pair
#          """
#         async for response in self._ws_query(
#                 **WSMarketCore(headers=self.headers).get_trades_args(symbol=symbol)):
#             json_data = json.loads(response)
#             if 'data' in json_data:
#                 yield _deserialize_trades(json_data['data'], response)
