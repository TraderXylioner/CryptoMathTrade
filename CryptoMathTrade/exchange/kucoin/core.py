from ._urls import URLS
from .._core import Core
from ..utils import _convert_kwargs_to_dict


class MarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Get orderbook.

        GET /api/v1/market/orderbook/level2_100

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-part-order-book-aggregated-

        param:
            symbol (str): the trading pair

        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=params)

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /api/v1/market/histories

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-trade-histories

        params:
            symbol (str): the trading pair
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=params)

    @_convert_kwargs_to_dict
    def get_ticker_args(self, params: dict) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v1/market/stats or /api/v1/market/allTickers

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-24hr-stats
        or
        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-all-tickers

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        _url = URLS.TICKER_URL if 'symbol' in params else URLS.TICKERS_URL
        return self.return_args(method='GET', url=URLS.BASE_URL + _url, params=params)


class WSMarketCore(Core):
    def __init__(self,
                 token: str,
                 proxies=None,
                 headers=None,
                 cookies=None,
                 auth=None,
                 ):
        super().__init__(proxies=proxies, headers=headers, cookies=cookies, auth=auth)
        self.token = token

    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Partial Book Depth Streams

        Stream Names: /spotMarket/level2Depth{limit}:{symbol}

        https://www.kucoin.com/docs/websocket/spot-trading/public-channels/level2-5-best-ask-bid-orders

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Valid are 5 or 50.

        """
        return self.return_args(method='subscribe',
                                url=f'{URLS.WS_BASE_URL}?token={self.token}',
                                params=f'/spotMarket/level2Depth{params["limit"]}:{params["symbol"].upper()}',
                                )

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: /market/match:{symbol}

         https://www.kucoin.com/docs/websocket/spot-trading/public-channels/match-execution-data

         param:
            symbol (str): the trading pair
         """
        return self.return_args(method='subscribe',
                                url=f'{URLS.WS_BASE_URL}?token={self.token}',
                                params=f'/market/match:{params["symbol"].upper()}',
                                )
