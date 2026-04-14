from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /spot/api/spot/market/depth

        param:
            symbol (str): the trading pair
        """

        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params
        )
