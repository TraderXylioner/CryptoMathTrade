from .._api import API
from .._urls import URLS
from ...utils import replace_param


class AccountCore(API):
    def get_balance_args(self, AccountObj, **params) -> dict:
        """Query Assets

        GET /api/v2/spot/account/assets

        https://www.bitget.com/api-doc/spot/account/Get-Account-Assets

        params:
            asset (str, optional): default all coin
        """
        replace_param(params, 'asset', 'coin')
        self.headers = AccountObj.get_payload(path=URLS.GET_BALANCE, method='GET', payload=params)
        return self.return_args(method='GET',
                                url=URLS.BASE_URL + URLS.GET_BALANCE,
                                params=params
                                )
