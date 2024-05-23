from .._urls import URLS
from ..._core import Core
from ...utils import _convert_kwargs_to_dict


class AccountCore(Core):
    @_convert_kwargs_to_dict
    def get_balance_args(self, AccountObj, params):
        """Query Assets

        POST /sapi/v3/asset/getUserAsset

        https://binance-docs.github.io/apidocs/spot/en/#user-asset-user_data

        params:
            asset (int, optional): If asset is blank, then query all positive assets user have.
        """
        return self.return_args(method='POST',
                                url=URLS.BASE_URL + URLS.GET_BALANCE,
                                params=AccountObj.get_payload(params),
                                )
