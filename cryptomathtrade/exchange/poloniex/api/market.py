from ..api.api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 10):
        """Get orderbook.

        GET /markets/{symbol}/orderBook

        https://ourbitdevelop.github.io/apidocs/spot_v3_en/#market-data-endpoints

        param:
            symbol (str): symbol name

            limit (int, optional): maximum number of records returned. The default value of limit is 10. Valid limit values are: 5, 10, 20, 50, 100, 150.
        """
        response = validate_response(
            self._query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json()
        return deserialize.deserialize_depth(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = 10):
        """Get orderbook.

        GET /markets/{symbol}/orderBook

        https://ourbitdevelop.github.io/apidocs/spot_v3_en/#market-data-endpoints

        param:
            symbol (str): symbol name

            limit (int, optional): maximum number of records returned. The default value of limit is 10. Valid limit values are: 5, 10, 20, 50, 100, 150.
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)
