from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /api/v1/depth

        https://www.bitrue.com/api_docs_includes_file/spot/index.html#market-data-endpoints

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Default 100; max 1000. Valid limits:[5, 10, 20, 50, 100, 500, 1000]
        """
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params
        )
