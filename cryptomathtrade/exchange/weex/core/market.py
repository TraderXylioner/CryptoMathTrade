from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /api/v2/market/depth

        https://www.weex.com/api-doc/spot/MarketDataAPI/GetDepthData

        param:
            symbol (str): the trading pair

            limit (int, optional): 	Number of entries (Only 15 and 200)

            type (str, optional): Default: step0: no aggregation.Values: step0, step1, step2, step3, step4, step5
        """
        # params['symbol'] += '_SPBL'
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params
        )
