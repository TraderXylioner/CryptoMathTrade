from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /api/v1/public

        https://www.coinw.com/api-doc/en/spot-trading/market/get-order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Order book depth data levels (5, 20) Default is 5
        """
        params["command"] = "returnOrderBook"
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params
        )
