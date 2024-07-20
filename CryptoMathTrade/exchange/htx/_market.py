from ._api import API
from ._deserialization import _deserialize_depth, _deserialize_trades, _deserialize_ticker, _deserialize_symbols, \
    _deserialize_kline
from .core import MarketCore
from ..utils import validate_response
from .._response import Response
from ...types import OrderBook, Trade, Ticker, Symbol, Kline


class Market(API):
    def get_depth(self, symbol: str, limit: int = None, type: str = 'step0') -> Response[OrderBook, object]:
        """Get orderbook.

        GET /market/depth

        https://huobiapi.github.io/docs/spot/v1/en/#get-market-depth

        when type is set to "step0", the default value of "depth" is 150 instead of 20.

        step0	No market depth aggregation
        step1	Aggregation level = precision*10
        step2	Aggregation level = precision*100
        step3	Aggregation level = precision*1000
        step4	Aggregation level = precision*10000
        step5	Aggregation level = precision*100000

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 20 or 150; max 20 or 150.

            type (str, optional): Market depth aggregation level, details below	step0, step1, step2, step3, step4, step5. Default step0.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit, type=type)))
        json_data = response.json()
        return _deserialize_depth(json_data, response)

    def get_trades(self, symbol: str, limit: int = 1) -> Response[list[Trade], object]:
        """Recent Trades List

        GET /market/history/trade

        https://huobiapi.github.io/docs/spot/v1/en/#get-the-most-recent-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 1; max 2000.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades(symbol=symbol, limit=limit)))
        json_data = response.json()
        return _deserialize_trades(json_data, response)

    def get_ticker(self, symbol: str = None) -> Response[list[Ticker], object]:
        """24hr Ticker Price Change Statistics

        GET /market/detail/merged or /market/tickers

        https://huobiapi.github.io/docs/spot/v1/en/#get-latest-aggregated-ticker
        or
        https://huobiapi.github.io/docs/spot/v1/en/#get-latest-tickers-for-all-pairs

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(self._query(**MarketCore(headers=self.headers).get_ticker(symbol=symbol)))
        json_data = response.json()
        return _deserialize_ticker(json_data, symbol, response)

    def get_symbols(self) -> Response[list[Symbol], object]:
        """Query Symbols

        GET /v2/settings/common/symbols

        https://huobiapi.github.io/docs/spot/v1/en/#get-all-supported-trading-symbol-v2
        """
        response = validate_response(self._query(**MarketCore.get_symbols(self)))
        json_data = response.json()
        return _deserialize_symbols(json_data, response)

    def get_kline(self, symbol: str, interval: str, limit: int = 150) -> Response[list[Kline], object]:
        """Historical K-line data

        GET /market/history/kline

        https://huobiapi.github.io/docs/spot/v1/en/#get-klines-candles

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1min, 5min, 15min, 30min, 60min, 4hour, 1day, 1mon, 1week, 1year).

            limit (int, optional): Default 150; max 2000.
        """
        response = validate_response(
            self._query(**MarketCore.get_kline(self, symbol=symbol, interval=interval, limit=limit)))
        json_data = response.json()
        return _deserialize_kline(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = None, type: str = 'step0') -> Response[OrderBook, object]:
        """Get orderbook.

        GET /market/depth

        https://huobiapi.github.io/docs/spot/v1/en/#get-market-depth

        when type is set to "step0", the default value of "depth" is 150 instead of 20.

        step0	No market depth aggregation
        step1	Aggregation level = precision*10
        step2	Aggregation level = precision*100
        step3	Aggregation level = precision*1000
        step4	Aggregation level = precision*10000
        step5	Aggregation level = precision*100000

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 20 or 150; max 20 or 150.

            type (str, optional): Market depth aggregation level, details below	step0, step1, step2, step3, step4, step5. Default step0.
        """
        response = validate_response(await self._async_query(
            **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit, type=type)))
        json_data = response.json
        return _deserialize_depth(json_data, response)

    async def get_trades(self, symbol: str, limit: int = 1) -> Response[list[Trade], object]:
        """Recent Trades List

        GET /market/history/trade

        https://huobiapi.github.io/docs/spot/v1/en/#get-the-most-recent-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 1; max 2000.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_trades(symbol=symbol, limit=limit)))
        json_data = response.json
        return _deserialize_trades(json_data, response)

    async def get_ticker(self, symbol: str = None) -> Response[list[Ticker], object]:
        """24hr Ticker Price Change Statistics

        GET /market/detail/merged or /market/tickers

        https://huobiapi.github.io/docs/spot/v1/en/#get-latest-aggregated-ticker
        or
        https://huobiapi.github.io/docs/spot/v1/en/#get-latest-tickers-for-all-pairs

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_ticker(symbol=symbol)))
        json_data = response.json
        return _deserialize_ticker(json_data, symbol, response)

    async def get_symbols(self) -> Response[list[Symbol], object]:
        """Query Symbols

        GET /v2/settings/common/symbols

        https://huobiapi.github.io/docs/spot/v1/en/#get-all-supported-trading-symbol-v2
        """
        response = validate_response(await self._async_query(**MarketCore.get_symbols(self)))
        json_data = response.json
        return _deserialize_symbols(json_data, response)

    async def get_kline(self, symbol: str, interval: str, limit: int = 150) -> Response[list[Kline], object]:
        """Historical K-line data

        GET /market/history/kline

        https://huobiapi.github.io/docs/spot/v1/en/#get-klines-candles

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1min, 5min, 15min, 30min, 60min, 4hour, 1day, 1mon, 1week, 1year).

            limit (int, optional): Default 150; max 2000.
        """
        response = validate_response(
            await self._async_query(**MarketCore.get_kline(self, symbol=symbol, interval=interval, limit=limit)))
        json_data = response.json
        return _deserialize_kline(json_data, response)

# TODO: WebSocketMarket

# class WebSocketMarket(API):
#     async def get_depth(self,
#                         symbol: str,
##                         type: str | None = 'step0',
#                         ) -> Generator:
#         """Partial Book Depth Streams
#
#         Stream Names: market.{symbol}.depth.{type}
#
#         https://www.htx.com/en-us/opend/newApiPages/?id=7ec5342e-7773-11ed-9966-0242ac110003
#
#         param:
#             symbol (str): the trading pair
#
#             type (str, optional): Market depth aggregation level, details below	step0, step1, step2, step3, step4, step5. Default step0.
#
#         when type is set to "step0", the default value of "depth" is 150 instead of 20.
#
#         step0	No market depth aggregation
#         step1	Aggregation level = precision*10
#         step2	Aggregation level = precision*100
#         step3	Aggregation level = precision*1000
#         step4	Aggregation level = precision*10000
#         step5	Aggregation level = precision*100000
#
#         """
#
#         async for response in self._ws_query(
#             **WSMarketCore(headers=self.headers).get_depth_args(symbol=symbol, type=type)):
#             json_data = json.loads(gzip.decompress(response))
#             if 'tick' in json_data:
#                 yield _serialize_depth(json_data['tick'], response)
#
#     async def get_trades(self,
#                          symbol: str,
#                          ) -> Generator:
#         """Trade Streams
#
#          The Trade Streams push raw trade information; each trade has a unique buyer and seller.
#          Update Speed: Real-time
#
#          Stream Name: market.{symbol}.trade.detail
#
#          https://www.htx.com/en-us/opend/newApiPages/?id=7ec53b69-7773-11ed-9966-0242ac110003
#
#          param:
#             symbol (str): the trading pair
#          """
#         async for response in self._ws_query(
#             **WSMarketCore(headers=self.headers).get_trades_args(symbol=symbol)):
#             json_data = json.loads(gzip.decompress(response))
#             if 'tick' in json_data:
#                 yield _serialize_trades_for_ws(json_data['tick']['data'], response)
