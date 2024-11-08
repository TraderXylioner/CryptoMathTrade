from ..api.api import API
from ..urls import URLS


class AccountCore(API):
    def get_coins(self, **params) -> dict:
        """All Coins' Information

        GET /api/v2/spot/public/coins

        https://www.bitget.com/api-doc/spot/market/Get-Coin-List

        params:
            coin (str, optional).
        """
        return self.return_args(
            method="GET",
            url=URLS.BASE_URL + URLS.COINS_URL,
            params=params,
        )
