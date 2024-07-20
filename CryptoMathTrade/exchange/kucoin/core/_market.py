from .._api import API
from .._urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(('symbol',))
    def get_depth(self, **kwargs) -> dict:
        """Get orderbook.

        GET /api/v1/market/orderbook/level2_100

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-part-order-book-aggregated-

        param:
            symbol (str): the trading pair
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=kwargs)

    @check_require_params(('symbol',))
    def get_trades(self, **kwargs) -> dict:
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /api/v1/market/histories

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-trade-histories

        params:
            symbol (str): the trading pair
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=kwargs)

    def get_ticker(self, **kwargs) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v1/market/stats or /api/v1/market/allTickers

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-24hr-stats
        or
        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-all-tickers

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        _url = URLS.TICKER_URL if kwargs.get('symbol') else URLS.TICKERS_URL
        return self.return_args(method='GET', url=URLS.BASE_URL + _url, params=kwargs)

    def get_symbols(self, **kwargs) -> dict:
        """Query Symbols

        GET /api/v2/symbols

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-symbols-list
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.SYMBOLS_URL, params=kwargs)

    @check_require_params(('symbol', 'interval'))
    def get_kline(self, **kwargs) -> dict:
        """Historical K-line data

        GET /api/v1/market/candles

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-klines

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1min, 3min, 5min, 15min, 30min, 1hour, 2hour, 4hour, 6hour, 8hour, 12hour, 1day, 1week, 1month).

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.
        """
        replace_param(kwargs, 'interval', 'type')
        replace_param(kwargs, 'startTime', 'startAt')
        replace_param(kwargs, 'endTime', 'endAt')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.KLINE_URL, params=kwargs)

# TODO: WSMarketCore

# class WSMarketCore(Core):
#     def __init__(self,
#                  token: str,
#                  proxies=None,
#                  headers=None,
#                  cookies=None,
#                  auth=None,
#                  ):
#         super().__init__(proxies=proxies, headers=headers, cookies=cookies, auth=auth)
#         self.token = token
#
#     def get_depth_args(self, **kwargs) -> dict:
#         """Partial Book Depth Streams
#
#         Stream Names: /spotMarket/level2Depth{limit}:{symbol}
#
#         https://www.kucoin.com/docs/websocket/spot-trading/public-channels/level2-5-best-ask-bid-orders
#
#         param:
#             symbol (str): the trading pair
#
#             limit (int, optional): limit the results. Valid are 5 or 50.
#
#         """
#         check_require_params(kwargs, ('symbol',))
#         return self.return_args(method='subscribe',
#                                 url=f'{URLS.WS_BASE_URL}?token={self.token}',
#                                 params=f'/spotMarket/level2Depth{kwargs["limit"]}:{kwargs["symbol"].upper()}',
#                                 )
#
#     def get_trades_args(self, **kwargs) -> dict:
#         """Trade Streams
#
#          The Trade Streams push raw trade information; each trade has a unique buyer and seller.
#          Update Speed: Real-time
#
#          Stream Name: /market/match:{symbol}
#
#          https://www.kucoin.com/docs/websocket/spot-trading/public-channels/match-execution-data
#
#          param:
#             symbol (str): the trading pair
#          """
#         check_require_params(kwargs, ('symbol',))
#         return self.return_args(method='subscribe',
#                                 url=f'{URLS.WS_BASE_URL}?token={self.token}',
#                                 params=f'/market/match:{kwargs["symbol"].upper()}',
#                                 )
