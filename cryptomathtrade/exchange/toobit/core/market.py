from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /quote/v1/depth

        https://api-docs.toobit.com/api/spot-market-data.html#order-book

        param:
            symbol (str): the trading pair

            limit (int, optional):Default 100; Notes: If you set limit=0, a lot of data will be returned.
        """
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params
        )
