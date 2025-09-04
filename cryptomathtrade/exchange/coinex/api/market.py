from ..api.api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 50, interval: int = 0):
        """Get orderbook.

        GET /spot/depth

        https://docs.coinex.com/api/v2/spot/market/http/list-market-depth

        param:
            symbol (str): the trading pair

            limit (int, optional): One of [5, 10, 20, 50] 	Number of entries (default: 50)

            interval (int, optional): Merge interval. One of ["0", "0.00000000001", "0.000000000001", "0.0000000001", "0.000000001", "0.00000001", "0.0000001", "0.000001", "0.00001", "0.0001", "0.001", "0.01", "0.1", "1", "10", "100", "1000"] (default: 0)
        """
        response = validate_response(
            self._query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit, interval=interval)
            )
        )
        json_data = response.json()
        return deserialize.deserialize_depth(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = 150, interval: int = 0):
        """Get orderbook.

        GET /spot/depth

        https://docs.coinex.com/api/v2/spot/market/http/list-market-depth

        param:
            symbol (str): the trading pair

            limit (int, optional): One of [5, 10, 20, 50] 	Number of entries (default: 50)

            interval (int, optional): Merge interval. One of ["0", "0.00000000001", "0.000000000001", "0.0000000001", "0.000000001", "0.00000001", "0.0000001", "0.000001", "0.00001", "0.0001", "0.001", "0.01", "0.1", "1", "10", "100", "1000"] (default: 0)
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit, interval=interval)
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)
