from .._urls import URLS
from ..._core import Core


class AccountCore(Core):
    def get_balance_args(self, AccountObj, **kwargs) -> dict:
        """Query Assets

        GET /openApi/spot/v1/account/balance

        https://bingx-api.github.io/docs/#/en-us/common/account-api.html#Query%20Assets

        params:
            recvWindow (int, optional): The value cannot be greater than 60000
        """
        return self.return_args(method='GET',
                                url=URLS.BASE_URL + URLS.GET_BALANCE,
                                params=AccountObj.get_payload(kwargs),
                                )
