from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /public/orderbook

        https://docs.whitebit.com/api-reference/market-data/orderbook

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Orders depth quantity: 0 - 100. Not defined or 0 will return 100 entries.

        """
        _url = f"{URLS.BASE_URL}{URLS.DEPTH_URL}/{params['symbol']}"
        params.pop("symbol")
        return self.return_args(method="GET", url=_url, params=params)
