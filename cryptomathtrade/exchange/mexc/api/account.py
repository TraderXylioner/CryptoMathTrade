from .api import API
from ..core.account import AccountCore
from ..deserialize import account as deserialize
from ...utils import validate_response


class Account(API):
    def get_coins(self):
        """All Coins' Information

        GET /api/v3/capital/config/getall

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#query-symbol-commission
        """
        response = validate_response(self._query(**AccountCore.get_coins(self)))
        json_data = response.json()
        return deserialize.deserialize_coins(json_data, response)


class AsyncAccount(API):
    async def get_coins(self):
        """All Coins' Information

        GET /api/v3/capital/config/getall

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#query-symbol-commission
        """
        response = validate_response(
            await self._async_query(**AccountCore.get_coins(self))
        )
        json_data = response.json
        return deserialize.deserialize_coins(json_data, response)
