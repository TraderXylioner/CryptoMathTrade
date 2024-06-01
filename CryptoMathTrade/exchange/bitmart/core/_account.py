from .._urls import URLS
from ..._core import Core
from ...utils import replace_param


class AccountCore(Core):
    def get_balance_args(self, AccountObj, **kwargs):
        """Query Assets

        GET /account/v1/wallet

        https://developer-pro.bitmart.com/en/spot/#get-account-balance-keyed

        params:
            asset (int, optional): If asset is blank, then query all positive assets user have.
        """
        replace_param(kwargs, 'asset', 'currency')
        return self.return_args(method='GET',
                                url=URLS.BASE_URL + URLS.GET_BALANCE,
                                params=AccountObj.get_payload(kwargs),
                                )
