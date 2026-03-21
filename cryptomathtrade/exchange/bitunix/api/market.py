from ..api.api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str):
        """Get orderbook.

        GET /api/spot/v1/market/depth

        https://www.bitunix.com/api-docs/spots/en_us/public/#2-get-depth-data

        param:
            symbol (str): the trading pair
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth(symbol=symbol))
        )
        json_data = response.json()
        return deserialize.deserialize_depth(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str):
        """Get orderbook.

        GET /api/spot/v1/market/depth

        https://www.bitunix.com/api-docs/spots/en_us/public/#2-get-depth-data

        param:
            symbol (str): the trading pair
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol)
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)
