from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /api/v1/depth

        https://docs.backpack.exchange/#tag/Markets/operation/get_depth

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Enum: "5" "10" "20" "50" "100" "500" "1000" Limit on the number of price levels to return on each side. Defaults to 100.
        """
        return self.return_args(method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params)
