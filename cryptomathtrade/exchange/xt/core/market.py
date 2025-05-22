from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /v4/public/depth

        https://doc.xt.com/#market3depth

        param:
            symbol (str): the trading pair

            limit (int, optional): 100	minimum number of queries is 100	1~500
        """
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params
        )
