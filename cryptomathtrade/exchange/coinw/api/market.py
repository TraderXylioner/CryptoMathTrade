from ..api.api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 5):
        """Get orderbook.

        GET /api/v1/public

        https://www.coinw.com/api-doc/en/spot-trading/market/get-order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Order book depth data levels (5, 20) Default is 5
        """
        response = validate_response(
            self._query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json()
        return deserialize.deserialize_depth(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = 5):
        """Get orderbook.

        GET /api/v1/public

        https://www.coinw.com/api-doc/en/spot-trading/market/get-order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Order book depth data levels (5, 20) Default is 5
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)
