from ..api.api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 100):
        """Get orderbook.

        GET /api/v1/depth

        https://www.bitrue.com/api_docs_includes_file/spot/index.html#market-data-endpoints

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Default 100; max 1000. Valid limits:[5, 10, 20, 50, 100, 500, 1000]
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

        GET /api/v1/depth

        https://www.bitrue.com/api_docs_includes_file/spot/index.html#market-data-endpoints

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Default 100; max 1000. Valid limits:[5, 10, 20, 50, 100, 500, 1000]
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)
