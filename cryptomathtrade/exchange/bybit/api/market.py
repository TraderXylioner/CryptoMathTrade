from .api import API
from ..deserialize import market as deserialize
from ..core.market import MarketCore
from ...utils import validate_response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 1):
        """Get orderbook.

        GET /v5/market/orderbook

        https://bybit-exchange.github.io/docs/v5/market/orderbook

        params:
            symbol (str): the trading pair.

            limit (int, optional): Default 1; max 200.
        """
        response = validate_response(
            self._query(**MarketCore.get_depth(self, symbol=symbol, limit=limit))
        )
        json_data = response.json()
        return deserialize.deserialize_depth(json_data, response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = 1):
        """Get orderbook.

        GET /v5/market/orderbook

        https://bybit-exchange.github.io/docs/v5/market/orderbook

        params:
            symbol (str): the trading pair.

            limit (int, optional): Default 1; max 200.
        """
        response = validate_response(
            await self._async_query(
                **MarketCore.get_depth(self, symbol=symbol, limit=limit)
            )
        )
        json_data = response.json
        return deserialize.deserialize_depth(json_data, response)
