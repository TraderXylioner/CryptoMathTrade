from ..api.api import API
from ..urls import URLS


class AccountCore(API):
    def get_coins(self, **params) -> dict:
        """All Coins' Information

        GET /api/v3/currencies

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-currency-list

        params:
            coin (str, optional).
        """
        coin = f"/{params.get('coin')}" if params.get("coin") else ""
        return self.return_args(
            method="GET",
            url=URLS.BASE_URL + URLS.COINS_URL + coin,
            params=params,
        )
