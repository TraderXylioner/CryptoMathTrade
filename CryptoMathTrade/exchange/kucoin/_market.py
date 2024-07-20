from ._api import API
from ._deserialization import _deserialize_depth, _deserialize_trades, _deserialize_ticker, _deserialize_symbols, \
    _deserialize_kline
from .core import MarketCore
from ..utils import validate_response
from .._response import Response
from ...types import OrderBook, Trade, Ticker, Symbol, Kline


class Market(API):
    def get_depth(self, symbol: str) -> Response[OrderBook, object]:
        """Get orderbook.

        GET /api/v1/market/orderbook/level2_100

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-part-order-book-aggregated-

        param:
            symbol (str): the trading pair
        """
        response = validate_response(self._query(**MarketCore(headers=self.headers).get_depth(symbol=symbol)))
        json_data = response.json()
        return _deserialize_depth(json_data, response)

    def get_trades(self, symbol: str) -> Response[list[Trade], object]:
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /api/v1/market/histories

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-trade-histories

        params:
            symbol (str): the trading pair
        """
        response = validate_response(self._query(**MarketCore(headers=self.headers).get_trades(symbol=symbol)))
        json_data = response.json()
        return _deserialize_trades(json_data, response)

    def get_ticker(self, symbol: str = None) -> Response[list[Ticker], object]:
        """24hr Ticker Price Change Statistics

        GET /api/v1/market/stats or /api/v1/market/allTickers

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-24hr-stats
        or
        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-all-tickers

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(self._query(**MarketCore(headers=self.headers).get_ticker(symbol=symbol)))
        json_data = response.json()
        return _deserialize_ticker(json_data, response)

    def get_symbols(self) -> Response[list[Symbol], object]:
        """Query Symbols

        GET /api/v2/symbols

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-symbols-list
        """
        response = validate_response(self._query(**MarketCore.get_symbols(self)))
        json_data = response.json()
        return _deserialize_symbols(json_data, response)

    def get_kline(self,
                  symbol: str,
                  interval: str,
                  startTime: int = None,
                  endTime: int = None,
                  ) -> Response[list[Kline], object]:
        """Historical K-line data

        GET /api/v1/market/candles

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-klines

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1min, 3min, 5min, 15min, 30min, 1hour, 2hour, 4hour, 6hour, 8hour, 12hour, 1day, 1week, 1month).

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.
        """
        response = validate_response(self._query(**MarketCore.get_kline(self,
                                                                        symbol=symbol,
                                                                        interval=interval,
                                                                        startTime=startTime,
                                                                        endTime=endTime,
                                                                        )))
        json_data = response.json()
        return _deserialize_kline(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str) -> Response[OrderBook, object]:
        """Get orderbook.

        GET /api/v1/market/orderbook/level2_100

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-part-order-book-aggregated-

        param:
            symbol (str): the trading pair
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_depth(symbol=symbol)))
        json_data = response.json
        return _deserialize_depth(json_data, response)

    async def get_trades(self, symbol: str) -> Response[list[Trade], object]:
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /api/v1/market/histories

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-trade-histories

        params:
            symbol (str): the trading pair
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_trades(symbol=symbol)))
        json_data = response.json
        return _deserialize_trades(json_data, response)

    async def get_ticker(self, symbol: str = None) -> Response[list[Ticker], object]:
        """24hr Ticker Price Change Statistics

        GET /api/v1/market/stats or /api/v1/market/allTickers

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-24hr-stats
        or
        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-all-tickers

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_ticker(symbol=symbol)))
        json_data = response.json
        return _deserialize_ticker(json_data, response)

    async def get_symbols(self) -> Response[list[Symbol], object]:
        """Query Symbols

        GET /api/v2/symbols

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-symbols-list
        """
        response = validate_response(await self._async_query(**MarketCore.get_symbols(self)))
        json_data = response.json
        return _deserialize_symbols(json_data, response)

    async def get_kline(self,
                        symbol: str,
                        interval: str,
                        startTime: int = None,
                        endTime: int = None,
                        ) -> Response[list[Kline], object]:
        """Historical K-line data

        GET /api/v1/market/candles

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-klines

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1min, 3min, 5min, 15min, 30min, 1hour, 2hour, 4hour, 6hour, 8hour, 12hour, 1day, 1week, 1month).

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.
        """
        response = validate_response(await self._async_query(**MarketCore.get_kline(self,
                                                                                    symbol=symbol,
                                                                                    interval=interval,
                                                                                    startTime=startTime,
                                                                                    endTime=endTime,
                                                                                    )))
        json_data = response.json
        return _deserialize_kline(json_data, response)

# TODO: WebSocketMarket

# class WebSocketMarket(API):
#     def __init__(self, token):
#         super().__init__()
#         self.token = token
#
#     async def get_depth(self,
#                         symbol: str,
#                         limit: int | None = 50,
#                         ) -> Generator:
#         """Partial Book Depth Streams
#
#         Stream Names: /spotMarket/level2Depth{limit}:{symbol}
#
#         https://www.kucoin.com/docs/websocket/spot-trading/public-channels/level2-5-best-ask-bid-orders
#
#         param:
#
#             symbol (str): the trading pair
#
#             limit (int, optional): limit the results. Valid are 5 or 50.
#
#         """
#
#         async for response in self._ws_query(
#             **WSMarketCore(headers=self.headers, token=self.token).get_depth(symbol=symbol,
#                                                                              limit=limit,
#                                                                              )):
#             json_data = json.loads(response)
#             if 'data' in json_data:
#                 yield _deserialize_depth(json_data['data'], response)
#
#     async def get_trades(self,
#                          symbol: str,
#                          ) -> Generator:
#         """Trade Streams
#
#          The Trade Streams push raw trade information; each trade has a unique buyer and seller.
#          Update Speed: Real-time
#
#          Stream Name: /market/match:{symbol}
#
#          https://www.kucoin.com/docs/websocket/spot-trading/public-channels/match-execution-data
#
#          param:
#             symbol (str): the trading pair
#          """
#         async for response in self._ws_query(
#             **WSMarketCore(headers=self.headers, token=self.token).get_trades(symbol=symbol)):
#             json_data = json.loads(response)
#             if 'data' in json_data:
#                 yield _deserialize_trades([json_data['data']], response)
