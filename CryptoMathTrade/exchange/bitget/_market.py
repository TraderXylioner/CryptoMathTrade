from ._api import API
from ._serialization import _serialize_depth, _serialize_trades, _serialize_ticker
from .core import MarketCore
from ..utils import validate_response
from .._response import Response


class Market(API):
    def get_depth(self,
                  symbol: str,
                  limit: int = 150,
                  ) -> Response:
        """Get orderbook.

        GET /api/v2/spot/market/orderbook

        https://www.bitget.com/api-doc/spot/market/Get-Orderbook

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 150; max 150.

            type (str, optional) The value enums：step0，step1，step2，step3，step4，step5. Default: step0.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json()['data']
        return _serialize_depth(json_data, response)

    def get_trades(self,
                   symbol: str,
                   limit: int = 100,
                   ) -> Response:
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /api/v2/spot/market/fills

        https://www.bitget.com/api-doc/spot/market/Get-Recent-Trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 500.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json()['data']
        return _serialize_trades(json_data, response)

    def get_ticker(self,
                   symbol: str | None = None,
                   ) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v2/spot/market/tickers

        https://www.bitget.com/api-doc/spot/market/Get-Tickers

        params:
            symbol (str, optional): the trading pair
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json()['data']
        return _serialize_ticker(json_data, response)


class AsyncMarket(API):
    async def get_depth(self,
                        symbol: str,
                        limit: int = 100,
                        ) -> Response:
        """Get orderbook.

        GET /api/v2/spot/market/orderbook

        https://www.bitget.com/api-doc/spot/market/Get-Orderbook

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 150; max 150.

            type (str, optional) The value enums：step0，step1，step2，step3，step4，step5. Default: step0.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json['data']
        return _serialize_depth(json_data, response)

    async def get_trades(self,
                         symbol: str,
                         limit: int = 100,
                         ) -> Response:
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /api/v2/spot/market/fills

        https://www.bitget.com/api-doc/spot/market/Get-Recent-Trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 500.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json['data']
        return _serialize_trades(json_data, response)

    async def get_ticker(self,
                         symbol: str | None = None,
                         ) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v2/spot/market/tickers

        https://www.bitget.com/api-doc/spot/market/Get-Tickers

        params:
            symbol (str, optional): the trading pair
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json['data']
        return _serialize_ticker(json_data, response)
