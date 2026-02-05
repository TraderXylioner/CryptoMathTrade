from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /markets/{symbol}/orderBook

        https://ourbitdevelop.github.io/apidocs/spot_v3_en/#market-data-endpoints

        param:
            symbol (str): symbol name

            limit (int, optional): maximum number of records returned. The default value of limit is 10. Valid limit values are: 5, 10, 20, 50, 100, 150.
        """
        symbol = params.pop('symbol')
        return self.return_args(method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL.replace("{symbol}", symbol), params=params)
