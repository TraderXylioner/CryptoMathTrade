from ._urls import URLS
from .._core import Core
from ..utils import _convert_kwargs_to_dict


class MarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Get orderbook.

        GET /api/v2/spot/market/orderbook

        https://www.bitget.com/api-doc/spot/market/Get-Orderbook

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 150; max 150.

            type (str, optional) The value enums：step0，step1，step2，step3，step4，step5. Default: step0.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=params)

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /api/v2/spot/market/fills

        https://www.bitget.com/api-doc/spot/market/Get-Recent-Trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 500.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=params)

    @_convert_kwargs_to_dict
    def get_ticker_args(self, params: dict) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v2/spot/market/tickers

        https://www.bitget.com/api-doc/spot/market/Get-Tickers

        params:
            symbol (str, optional): the trading pair
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TICKER_URL, params=params)
