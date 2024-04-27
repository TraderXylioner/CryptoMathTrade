from ._api import API
from ._serialization import _serialize_depth, _serialize_trades, _serialize_ticker
from .core import MarketCore
from ..utils import validate_response
from .._response import Response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 35) -> Response:
        """Get orderbook.

        GET /spot/quotation/v3/books

        https://developer-pro.bitmart.com/en/spot/#get-depth-v3

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 35; max 50.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json()
        return _serialize_depth(json_data, response)

    def get_trades(self, symbol: str, limit: int = 50) -> Response:
        """Recent Trades List
        Get recent trades (up to last 50).

        GET /spot/quotation/v3/trades

        https://developer-pro.bitmart.com/en/spot/#get-recent-trades-v3

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 50; max 50.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json()
        return _serialize_trades(json_data, response)

    def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /spot/quotation/v3/ticker or /spot/quotation/v3/tickers

        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-a-trading-pair-v3
        or
        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-all-pairs-v3

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json()
        return _serialize_ticker(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = 35) -> Response:
        """Get orderbook.

        GET /spot/quotation/v3/books

        https://developer-pro.bitmart.com/en/spot/#get-depth-v3

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 35; max 50.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json
        return _serialize_depth(json_data, response)

    async def get_trades(self, symbol: str, limit: int = 50) -> Response:
        """Recent Trades List
        Get recent trades (up to last 50).

        GET /spot/quotation/v3/trades

        https://developer-pro.bitmart.com/en/spot/#get-recent-trades-v3

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 50; max 50.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json
        return _serialize_trades(json_data, response)

    async def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /spot/quotation/v3/ticker or /spot/quotation/v3/tickers

        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-a-trading-pair-v3
        or
        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-all-pairs-v3

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json
        return _serialize_ticker(json_data, response)
