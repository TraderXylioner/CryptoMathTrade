from ..api.api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 100):
        """Get orderbook.

        GET /api/v1/depth

        https://docs.backpack.exchange/#tag/Markets/operation/get_depth

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Enum: "5" "10" "20" "50" "100" "500" "1000" Limit on the number of price levels to return on each side. Defaults to 100.
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

        https://docs.backpack.exchange/#tag/Markets/operation/get_depth

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Enum: "5" "10" "20" "50" "100" "500" "1000" Limit on the number of price levels to return on each side. Defaults to 100.
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)
