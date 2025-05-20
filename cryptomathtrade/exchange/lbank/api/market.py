from ..api.api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 100):
        """Get orderbook.

        GET /v2/depth.do

        https://www.lbank.com/docs/index.html#depth-information

        param:
            symbol (str): the trading pair

            limit (int, optional): The count of returned items.(1-200)
        """
        response = validate_response(
            self._query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json()
        return deserialize.deserialize_depth(json_data, response)

    def get_ticker(self, symbol: str = None):
        """24hr Ticker Price Change Statistics

        GET /v2/ticker/24hr.do

        https://www.lbank.com/docs/index.html#24hr-ticker

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker(symbol=symbol))
        )
        json_data = response.json()
        return deserialize.deserialize_ticker(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = 100):
        """Get orderbook.

        GET /v2/depth.do

        https://www.lbank.com/docs/index.html#depth-information

        param:
            symbol (str): the trading pair

            limit (int, optional): The count of returned items.(1-200)
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)

    async def get_ticker(self, symbol: str = None):
        """24hr Ticker Price Change Statistics

        GET /v2/ticker/24hr.do

        https://www.lbank.com/docs/index.html#24hr-ticker

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
