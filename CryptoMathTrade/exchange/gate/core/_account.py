from .._urls import URLS
from ..._core import Core
from ...utils import replace_param


class AccountCore(Core):
    def get_balance_args(self, AccountObj, **kwargs):
        """Query Assets

        GET /api/v4/spot/accounts

        https://www.gate.io/docs/developers/apiv4/#list-spot-accounts

        params:
            asset (int, optional): If asset is blank, then query all positive assets user have.
        """
        replace_param(kwargs, 'asset', 'currency')
        self.headers = AccountObj.get_payload(path=URLS.GET_BALANCE, method='GET', payload=kwargs)
        return self.return_args(method='GET',
                                url=URLS.BASE_URL + URLS.GET_BALANCE,
                                params=kwargs,
                                )
