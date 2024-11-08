from ..api.api import API
from ..urls import URLS
from ...utils import replace_param


class AccountCore(API):
    def get_coins(self, **params) -> dict:
        """All Coins' Information

        GET /v1/settings/common/chains

        https://huobiapi.github.io/docs/spot/v1/en/#get-chains-information
        """
        return self.return_args(
            method="GET",
            url=URLS.BASE_URL + URLS.COINS_URL,
            params=params,
        )
