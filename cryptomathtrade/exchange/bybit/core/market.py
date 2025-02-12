from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, convert_list_to_json_array


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /v5/market/orderbook

        https://bybit-exchange.github.io/docs/v5/market/orderbook

        params:
            symbol (str): the trading pair.

            limit (int, optional): Default 1; max 200.
        """
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params
        )
