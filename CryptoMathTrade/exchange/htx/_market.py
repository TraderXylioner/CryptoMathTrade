import gzip
import json
from typing import Generator

from ._api import API
from ._serialization import _serialize_depth, _serialize_trades, _serialize_ticker, _serialize_trades_for_ws
from .core import MarketCore, WSMarketCore
from ..utils import validate_response
from .._response import Response


class Market(API):
    def get_depth(self, symbol: str, limit: int = None, type: str = 'step0') -> Response:
        """Get orderbook.

        GET /market/depth

        https://huobiapi.github.io/docs/spot/v1/en/#get-market-depth

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 20 or 150; max 20 or 150.
            type (str, optional): Market depth aggregation level, details below	step0, step1, step2, step3, step4, step5. Default step0.

            when type is set to "step0", the default value of "depth" is 150 instead of 20.

            step0	No market depth aggregation
            step1	Aggregation level = precision*10
            step2	Aggregation level = precision*100
            step3	Aggregation level = precision*1000
            step4	Aggregation level = precision*10000
            step5	Aggregation level = precision*100000
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit, type=type)))
        json_data = response.json()['tick']
        return _serialize_depth(json_data, response)

    def get_trades(self, symbol: str, limit: int = 1) -> Response:
        """Recent Trades List

        GET /market/history/trade

        https://huobiapi.github.io/docs/spot/v1/en/#get-the-most-recent-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 1; max 2000.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json()['data']
        return _serialize_trades(json_data, response)

    def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /market/detail/merged or /market/tickers

        https://huobiapi.github.io/docs/spot/v1/en/#get-latest-aggregated-ticker
        or
        https://huobiapi.github.io/docs/spot/v1/en/#get-latest-tickers-for-all-pairs

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        full_json_data = response.json()
        return _serialize_ticker(full_json_data, symbol, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = None, type: str = 'step0') -> Response:
        """Get orderbook.

        GET /market/depth

        https://huobiapi.github.io/docs/spot/v1/en/#get-market-depth

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 20 or 150; max 20 or 150.
            type (str, optional): Market depth aggregation level, details below	step0, step1, step2, step3, step4, step5. Default step0.

            when type is set to "step0", the default value of "depth" is 150 instead of 20.

            step0	No market depth aggregation
            step1	Aggregation level = precision*10
            step2	Aggregation level = precision*100
            step3	Aggregation level = precision*1000
            step4	Aggregation level = precision*10000
            step5	Aggregation level = precision*100000
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit, type=type)))
        json_data = response.json()['tick']
        return _serialize_depth(json_data, response)

    async def get_trades(self, symbol: str, limit: int = 1) -> Response:
        """Recent Trades List

        GET /market/history/trade

        https://huobiapi.github.io/docs/spot/v1/en/#get-the-most-recent-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 1; max 2000.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json()['data']
        return _serialize_trades(json_data, response)

    async def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /market/detail/merged or /market/tickers

        https://huobiapi.github.io/docs/spot/v1/en/#get-latest-aggregated-ticker
        or
        https://huobiapi.github.io/docs/spot/v1/en/#get-latest-tickers-for-all-pairs

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        full_json_data = response.json()
        return _serialize_ticker(full_json_data, symbol, response)


class WebSocketMarket(API):
    async def get_depth(self,
                        symbol: str,
                        type: str | None = 'step0',
                        ) -> Generator:
        """Partial Book Depth Streams

        Stream Names: market.{symbol}.depth.{type}

        https://www.htx.com/en-us/opend/newApiPages/?id=7ec5342e-7773-11ed-9966-0242ac110003

        param:
            symbol (str): the trading pair

            type (str, optional): Market depth aggregation level, details below	step0, step1, step2, step3, step4, step5. Default step0.

        when type is set to "step0", the default value of "depth" is 150 instead of 20.

        step0	No market depth aggregation
        step1	Aggregation level = precision*10
        step2	Aggregation level = precision*100
        step3	Aggregation level = precision*1000
        step4	Aggregation level = precision*10000
        step5	Aggregation level = precision*100000

        """

        async for response in self._ws_query(
            **WSMarketCore(headers=self.headers).get_depth_args(symbol=symbol, type=type)):
            json_data = json.loads(gzip.decompress(response))
            if 'tick' in json_data:
                yield _serialize_depth(json_data['tick'], response)

    async def get_trades(self,
                         symbol: str,
                         ) -> Generator:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: market.{symbol}.trade.detail

         https://www.htx.com/en-us/opend/newApiPages/?id=7ec53b69-7773-11ed-9966-0242ac110003

         param:
            symbol (str): the trading pair
         """
        async for response in self._ws_query(
            **WSMarketCore(headers=self.headers).get_trades_args(symbol=symbol)):
            json_data = json.loads(gzip.decompress(response))
            if 'tick' in json_data:
                yield _serialize_trades_for_ws(json_data['tick']['data'], response)
