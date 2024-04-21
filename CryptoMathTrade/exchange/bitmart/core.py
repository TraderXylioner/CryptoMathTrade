from ._urls import URLS
from .._core import Core
from ..utils import _convert_kwargs_to_dict


class MarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Get orderbook.

        GET /spot/quotation/v3/books

        https://developer-pro.bitmart.com/en/spot/#get-depth-v3

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 35; max 50.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=params)

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Recent Trades List
        Get recent trades (up to last 50).

        GET /spot/quotation/v3/trades

        https://developer-pro.bitmart.com/en/spot/#get-recent-trades-v3

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 50; max 50.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=params)

    @_convert_kwargs_to_dict
    def get_ticker_args(self, params: dict) -> dict:
        """24hr Ticker Price Change Statistics

        GET /spot/quotation/v3/ticker or /spot/quotation/v3/tickers

        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-a-trading-pair-v3
        or
        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-all-pairs-v3

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        _url = URLS.TICKER_URL if 'symbol' in params else URLS.TICKERS_URL
        return self.return_args(method='GET', url=URLS.BASE_URL + _url, params=params)
