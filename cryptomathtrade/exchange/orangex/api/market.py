from ..api.api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 100):
        """Get orderbook.

        GET /quote/v1/depth

        https://api-docs.toobit.com/api/spot-market-data.html#order-book

        param:
            symbol (str): the trading pair

            limit (int, optional):Default 100; Notes: If you set limit=0, a lot of data will be returned.
        """
        response = validate_response(
            self._query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json()
        return deserialize.deserialize_depth(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = 100):
        """Get orderbook.

        GET /quote/v1/depth

        https://api-docs.toobit.com/api/spot-market-data.html#order-book

        param:
            symbol (str): the trading pair

            limit (int, optional):Default 100; Notes: If you set limit=0, a lot of data will be returned.
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)
