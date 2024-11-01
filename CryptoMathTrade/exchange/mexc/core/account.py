from ..api.api import API
from ..urls import URLS


class AccountCore(API):
    def get_coins(self, **params) -> dict:
        """All Coins' Information

        GET /api/v3/capital/config/getall

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#query-symbol-commission
        """
        return self.return_args(
            method="GET",
            url=URLS.BASE_URL + URLS.COINS_URL,
            params=self.get_payload(params),
        )
