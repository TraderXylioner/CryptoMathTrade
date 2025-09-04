from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /spot/depth

        https://docs.coinex.com/api/v2/spot/market/http/list-market-depth

        param:
            symbol (str): the trading pair

            limit (int, optional): One of [5, 10, 20, 50] 	Number of entries (default: 50)

            interval (int, optional): Merge interval. One of ["0", "0.00000000001", "0.000000000001", "0.0000000001", "0.000000001", "0.00000001", "0.0000001", "0.000001", "0.00001", "0.0001", "0.001", "0.01", "0.1", "1", "10", "100", "1000"] (default: 0)
        """
        replace_param(params, "symbol", "market")
        if 'limit' not in params:
            params['limit'] = 50
        if 'interval' not in params:
            params['interval'] = 0
        return self.return_args(method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params)
