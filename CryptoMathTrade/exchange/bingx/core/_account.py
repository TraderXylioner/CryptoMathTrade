from .._api import API
from .._urls import URLS


class AccountCore(API):
    def get_balance(self, **kwargs) -> dict:
        """Query Assets

        GET /openApi/spot/v1/account/balance

        https://bingx-api.github.io/docs/#/en-us/common/account-api.html#Query%20Assets
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.GET_BALANCE, params=self.get_payload(kwargs))
