from ._api import API
from .core import AccountCore
from .._response import Response
from ..utils import validate_response


class Account(API):
    def get_balance(self, asset: str | None = None):
        """Query Assets

        POST /sapi/v3/asset/getUserAsset

        https://binance-docs.github.io/apidocs/spot/en/#user-asset-user_data

        params:
            asset (int, optional): If asset is blank, then query all positive assets user have.
        """
        response = validate_response(self._query(**AccountCore(headers=self.headers).get_balance_args(self,
                                                                                                      asset=asset,
                                                                                                      )))
        json_data = response.json()
        return Response(data=json_data,
                        response_object=response,
                        )
