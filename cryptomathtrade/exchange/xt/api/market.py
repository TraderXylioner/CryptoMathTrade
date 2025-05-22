from ..api.api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 100):
        """Get orderbook.

        GET /v4/public/depth

        https://doc.xt.com/#market3depth

        param:
            symbol (str): the trading pair

            limit (int, optional): 100	minimum number of queries is 100	1~500
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

        GET /v4/public/depth

        https://doc.xt.com/#market3depth

        param:
            symbol (str): the trading pair

            limit (int, optional): 100	minimum number of queries is 100	1~500
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)
