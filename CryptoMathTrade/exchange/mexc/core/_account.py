from .._urls import URLS
from ..._core import Core


class AccountCore(Core):
    def get_balance_args(self, AccountObj, **kwargs):
        """Query Assets

        GET /api/v3/account

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#account-information
        """
        return self.return_args(method='GET',
                                url=URLS.BASE_URL + URLS.GET_BALANCE,
                                params=AccountObj.get_payload(kwargs),
                                )
