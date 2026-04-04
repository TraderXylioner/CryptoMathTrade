from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /api/spot/instruments/depth

        https://www.tapbit.com/openapi-docs/spot_v2/public/depth/

        param:
            symbol (str): the trading pair

            limit (int, optional): the depth gear with values of 5, 10, 50 and 100. Default: 100.
        """
        if not params["limit"]:
            params["limit"] = 100
        replace_param(params, "limit", "depth")
        replace_param(params, "symbol", "instrument_id")
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params
        )
