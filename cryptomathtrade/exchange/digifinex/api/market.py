from ..api.api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 10):
        """Get orderbook.

        GET /v3/order_book

        https://docs.digifinex.com/en-ww/spot/v3/rest.html#get-orderbook

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Limit of depth, default 10, maximum 150
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

        GET /v3/order_book

        https://docs.digifinex.com/en-ww/spot/v3/rest.html#get-orderbook

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Limit of depth, default 10, maximum 150
        """
        response = validate_response(
            await self._async_query(
                **MarketCore(headers=self.headers).get_depth(symbol=symbol, limit=limit)
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)
