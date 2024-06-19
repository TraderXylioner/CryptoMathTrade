from ._api import API
from ._serialization import _serialize_balance
from .core import AccountCore
from .._response import Response
from ..utils import validate_response


class Account(API):
    def get_balance(self) -> Response:
        """Query Assets

        GET /openApi/spot/v1/account/balance

        https://bingx-api.github.io/docs/#/en-us/common/account-api.html#Query%20Assets
        """
        response = validate_response(self._query(**AccountCore.get_balance(self)))
        json_data = response.json()
        return _serialize_balance(json_data, response)


class AsyncAccount(API):
    async def get_balance(self) -> Response:
        """Query Assets

        GET /openApi/spot/v1/account/balance

        https://bingx-api.github.io/docs/#/en-us/common/account-api.html#Query%20Assets
        """
        response = validate_response(await self._async_query(**AccountCore.get_balance(self)))
        json_data = response.json
        return _serialize_balance(json_data, response)
