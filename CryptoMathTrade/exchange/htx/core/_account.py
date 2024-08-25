from .._urls import URLS
from ..._core import Core


class AccountCore(Core):
    def get_balance_args(self, AccountObj, **params):
        """Query Assets

        GET /v1/account/accounts

        https://www.htx.com/en-us/opend/newApiPages/?id=7ec4b429-7773-11ed-9966-0242ac110003

        """
        return self.return_args(method='GET',
                                url=URLS.BASE_URL + URLS.GET_BALANCE,
                                params=AccountObj.get_payload(params),
                                )
