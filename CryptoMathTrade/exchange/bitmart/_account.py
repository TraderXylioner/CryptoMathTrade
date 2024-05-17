from ._api import API
from ._serialization import _serialize_balance
from .core import AccountCore
from .._response import Response
from ..utils import validate_response


class Account(API):
    def get_balance(self, asset: str | None = None) -> Response:
        """Query Assets

        GET /account/v1/wallet

        https://developer-pro.bitmart.com/en/spot/#get-account-balance-keyed

        params:
            asset (int, optional): If asset is blank, then query all positive assets user have.
        """
        response = validate_response(self._query(**AccountCore(headers=self.headers).get_balance_args(self,
                                                                                                      asset=asset,
                                                                                                      )))
        json_data = response.json()
        return _serialize_balance(json_data, response)


class AsyncAccount(API):
    async def get_balance(self, asset: str | None = None) -> Response:
        """Query Assets

        GET /account/v1/wallet

        https://developer-pro.bitmart.com/en/spot/#get-account-balance-keyed

        params:
            asset (int, optional): If asset is blank, then query all positive assets user have.
        """
        response = validate_response(
            await self._async_query(**AccountCore(headers=self.headers).get_balance_args(self,
                                                                                         asset=asset,
                                                                                         )))
        json_data = response.json
        return _serialize_balance(json_data, response)
