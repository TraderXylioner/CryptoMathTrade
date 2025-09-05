from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /api/v3/depth

        https://ourbitdevelop.github.io/apidocs/spot_v3_en/#market-data-endpoints

        param:
            symbol (str): the trading pair

            limit (int, optional): Number of entries (default: 100) max 5000
        """
        return self.return_args(method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params)
