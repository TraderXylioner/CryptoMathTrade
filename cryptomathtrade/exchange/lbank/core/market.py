from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        ...
        """Get orderbook.

        GET /v2/depth.do

        https://www.lbank.com/docs/index.html#depth-information

        param:
            symbol (str): the trading pair

            limit (int, optional): The count of returned items.(1-200)
        """
        replace_param(params, "limit", "size")
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params
        )

    def get_ticker(self, **params) -> dict:
        """24hr Ticker Price Change Statistics

        GET /v2/ticker/24hr.do

        https://www.lbank.com/docs/index.html#24hr-ticker

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        if not params.get("symbol"):
            params["symbol"] = "all"
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.TICKER_URL, params=params
        )
