from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /v3/order_book

        https://docs.digifinex.com/en-ww/spot/v3/rest.html#get-orderbook

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Limit of depth, default 10, maximum 150
        """
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params
        )
