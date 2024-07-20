from ._api import API
from ._deserialization import _deserialize_depth, _deserialize_trades, _deserialize_ticker, _deserialize_symbols, \
    _deserialize_kline
from .core import MarketCore
from ..utils import validate_response
from .._response import Response
from ...types import OrderBook, Trade, Ticker, Symbol, Kline


class Market(API):
    def get_depth(self, symbol: str, limit: int = 35) -> Response[OrderBook, object]:
        """Get orderbook.

        GET /spot/quotation/v3/books

        https://developer-pro.bitmart.com/en/spot/#get-depth-v3

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 35; max 50.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)))
        json_data = response.json()
        return _deserialize_depth(json_data, response)

    def get_trades(self, symbol: str, limit: int = 50) -> Response[list[Trade], object]:
        """Recent Trades List

        GET /spot/quotation/v3/trades

        https://developer-pro.bitmart.com/en/spot/#get-recent-trades-v3

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 50; max 50.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades(symbol=symbol, limit=limit)))
        json_data = response.json()
        return _deserialize_trades(json_data, response)

    def get_ticker(self, symbol: str = None) -> Response[list[Ticker], object]:
        """24hr Ticker Price Change Statistics

        GET /spot/quotation/v3/ticker or /spot/quotation/v3/tickers

        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-a-trading-pair-v3
        or
        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-all-pairs-v3

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(self._query(**MarketCore(headers=self.headers).get_ticker(symbol=symbol)))
        json_data = response.json()
        return _deserialize_ticker(json_data, response)

    def get_symbols(self) -> Response[list[Symbol], object]:
        """Query Symbols

        GET /spot/v1/symbols/details

        https://developer-pro.bitmart.com/en/spot/#get-trading-pair-details-v1
        """
        response = validate_response(self._query(**MarketCore.get_symbols(self)))
        json_data = response.json()
        return _deserialize_symbols(json_data, response)

    def get_kline(self,
                  symbol: str,
                  interval: str,
                  limit: int = 100,
                  startTime: int = None,
                  endTime: int = None,
                  ) -> Response[list[Kline], object]:
        """Historical K-line data

        GET /spot/quotation/v3/klines

        https://developer-pro.bitmart.com/en/spot/#get-history-k-line-v3

        params:
            symbol (str): the trading pair.

            interval (str): Time interval ([1, 3, 5, 15, 30, 45, 60, 120, 180, 240, 1440, 10080, 43200] unit: minute, default 1).

            limit (int, optional): Default 100; max 200.

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
    async def get_depth(self, symbol: str, limit: int = 35) -> Response[OrderBook, object]:
        """Get orderbook.

        GET /spot/quotation/v3/books

        https://developer-pro.bitmart.com/en/spot/#get-depth-v3

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 35; max 50.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)))
        json_data = response.json
        return _deserialize_depth(json_data, response)

    async def get_trades(self, symbol: str, limit: int = 50) -> Response[list[Trade], object]:
        """Recent Trades List

        GET /spot/quotation/v3/trades

        https://developer-pro.bitmart.com/en/spot/#get-recent-trades-v3

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 50; max 50.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_trades(symbol=symbol, limit=limit)))
        json_data = response.json
        return _deserialize_trades(json_data, response)

    async def get_ticker(self, symbol: str = None) -> Response[list[Ticker], object]:
        """24hr Ticker Price Change Statistics

        GET /spot/quotation/v3/ticker or /spot/quotation/v3/tickers

        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-a-trading-pair-v3
        or
        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-all-pairs-v3

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_ticker(symbol=symbol)))
        json_data = response.json
        return _deserialize_ticker(json_data, response)

    async def get_symbols(self) -> Response[list[Symbol], object]:
        """Query Symbols

        GET /spot/v1/symbols/details

        https://developer-pro.bitmart.com/en/spot/#get-trading-pair-details-v1
        """
        response = validate_response(await self._async_query(**MarketCore.get_symbols(self)))
        json_data = response.json
        return _deserialize_symbols(json_data, response)

    async def get_kline(self,
                        symbol: str,
                        interval: str,
                        limit: int = 100,
                        startTime: int = None,
                        endTime: int = None,
                        ) -> Response[list[Kline], object]:
        """Historical K-line data

        GET /spot/quotation/v3/klines

        https://developer-pro.bitmart.com/en/spot/#get-history-k-line-v3

        params:
            symbol (str): the trading pair.

            interval (str): Time interval ([1, 3, 5, 15, 30, 45, 60, 120, 180, 240, 1440, 10080, 43200] unit: minute, default 1).

            limit (int, optional): Default 100; max 200.

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

# TODO: WebSocketMarket

# class WebSocketMarket(API):
#     async def get_depth(self,
#                         symbol: str,
#                         limit: int | None = 50,
#                         ) -> Generator:
#         """Partial Book Depth Streams
#
#         Stream Names: spot/depth{limit}:{symbol}
#
#         https://developer-pro.bitmart.com/en/spot/#public-depth-all-channel
#
#         param:
#
#             symbol (str): the trading pair
#
#             limit (int, optional): limit the results. Valid are 5, 20 or 50.
#
#         """
#         async for response in self._ws_query(**WSMarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)):
#             json_data = json.loads(response)
#             if 'data' in json_data:
#                 yield _serialize_depth({'data': json_data['data'][0]}, response)
#
#     async def get_trades(self,
#                          symbol: str,
#                          ) -> Generator:
#         """Trade Streams
#
#          The Trade Streams push raw trade information; each trade has a unique buyer and seller.
#          Update Speed: Real-time
#
#          Stream Name: spot/trade:{symbol}
#
#         https://developer-pro.bitmart.com/en/spot/#public-trade-channel-2
#
#          param:
#             symbol (str): the trading pair
#          """
#         async for response in self._ws_query(
#             **WSMarketCore(headers=self.headers).get_trades_args(symbol=symbol)):
#             json_data = json.loads(response)
#             if 'data' in json_data:
#                 yield _serialize_trades_for_ws(json_data, response)
