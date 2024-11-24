from .api import API
from ..core.account import AccountCore
from ..deserialize import account as deserialize
from ...utils import validate_response


class Account(API):
    def get_coins(self, coin: str = None):
        """All Coins' Information

        GET /api/v2/spot/public/coins

        https://www.bitget.com/api-doc/spot/market/Get-Coin-List

        params:
            coin (str, optional).
        """
        response = validate_response(
            self._query(**AccountCore.get_coins(self, coin=coin))
        )
        json_data = response.json()
        return deserialize.deserialize_coins(json_data, response)


class AsyncAccount(API):
    async def get_coins(self, coin: str = None):
        """All Coins' Information

        GET /api/v2/spot/public/coins

        https://www.bitget.com/api-doc/spot/market/Get-Coin-List

        params:
            coin (str, optional).
        """
        response = validate_response(
            await self._async_query(**AccountCore.get_coins(self, coin=coin))
        )
        json_data = response.json
        return deserialize.deserialize_coins(json_data, response)