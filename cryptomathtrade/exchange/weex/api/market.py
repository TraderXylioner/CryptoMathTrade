from ..api.api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 15, type: str = 'step0'):
        """Get orderbook.

        GET /api/v2/market/depth

        https://www.weex.com/api-doc/spot/MarketDataAPI/GetDepthData

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Number of entries (Only 15 and 200)

            type (str, optional): Default: step0: no aggregation.Values: step0, step1, step2, step3, step4, step5
        """
        response = validate_response(
            self._query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit, type=type)
            )
        )
        json_data = response.json()
        return deserialize.deserialize_depth(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = 15, type: str = 'step0'):
        """Get orderbook.

        GET /api/v2/market/depth

        https://www.weex.com/api-doc/spot/MarketDataAPI/GetDepthData

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Number of entries (Only 15 and 200)

            type (str, optional): Default: step0: no aggregation.Values: step0, step1, step2, step3, step4, step5
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit, type=type)
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)
