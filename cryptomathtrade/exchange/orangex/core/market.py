from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /public/get_order_book

        https://openapi-docs.orangex.com/#get-order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): Not defined or 0 = full order book. Depth = 100 means 100 for each bid/ask side. Default = 100.
        """
        if not params["limit"]:
            params["limit"] = 100
        params["symbol"] = params["symbol"] + "-SPOT"
        replace_param(params, "limit", "depth")
        replace_param(params, "symbol", "instrument_name")
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params
        )
