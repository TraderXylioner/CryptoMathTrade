from .._api import API
from .._urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(('symbol',))
    def get_depth(self, **kwargs) -> dict:
        """Get orderbook.

        GET /api/v4/spot/order_book

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-order-book

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 10; max 5000.
        """
        replace_param(kwargs, 'symbol', 'currency_pair')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=kwargs)

    @check_require_params(('symbol',))
    def get_trades(self, **kwargs) -> dict:
        """Recent Trades List

        GET /api/v4/spot/trades

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-market-trades

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 100; max 1000.
        """
        replace_param(kwargs, 'symbol', 'currency_pair')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=kwargs)

    def get_ticker(self, **kwargs) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v4/spot/tickers

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-ticker-information

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned.
        """
        if 'symbol' in kwargs:
            replace_param(kwargs, 'symbol', 'currency_pair')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TICKER_URL, params=kwargs)

    def get_symbols(self, **kwargs) -> dict:
        """Query Symbols

        GET /api/v4/spot/currency_pairs

        https://www.gate.io/docs/developers/apiv4/en/#list-all-currency-pairs-supported
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.SYMBOLS_URL, params=kwargs)

    @check_require_params(('symbol',))
    def get_kline(self, **kwargs) -> dict:
        """Historical K-line data

        GET /api/v4/spot/candlesticks

        https://www.gate.io/docs/developers/apiv4/en/#market-candlesticks

        params:
            symbol (str): the trading pair.

            interval (str, optional): Time interval (10s, 1m, 5m, 15m, 30m, 1h, 4h, 8h, 1d, 7d, 30d).

            limit (int, optional): Default 500; max 1000.

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.
        """
        replace_param(kwargs, 'symbol', 'currency_pair')
        replace_param(kwargs, 'startTime', 'from')
        replace_param(kwargs, 'endTime', 'to')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.KLINE_URL, params=kwargs)

# TODO: WSMarketCore

# class WSMarketCore(Core):
#     def get_depth_args(self, **kwargs) -> dict:
#         """Partial Book Depth Streams
#
#         Stream Names: spot.order_book_update
#
#         https://www.gate.io/docs/developers/apiv4/ws/en/#changed-order-book-levels
#
#         params:
#
#             symbol (str): the trading pair.
#
#             limit (int, optional): limit the results. Valid are 5, 10, 20, 50 or 100.
#
#             interval (int, optional): 1000ms or 100ms.
#
#         """
#         check_require_params(kwargs, ('symbol',))
#         return self.return_args(method='subscribe',
#                                 url=URLS.WS_BASE_URL,
#                                 params={'channel': 'spot.order_book',
#                                         'payload': [kwargs.get('symbol'),
#                                                     str(kwargs.get('limit')),
#                                                     f'{kwargs.get("interval")}ms'],
#                                         },
#                                 )
#
#     def get_trades_args(self, **kwargs) -> dict:
#         """Trade Streams
#
#          The Trade Streams push raw trade information; each trade has a unique buyer and seller.
#          Update Speed: Real-time
#
#          Stream Name: spot.trades
#
#          https://www.gate.io/docs/developers/apiv4/ws/en/#client-subscription-2
#
#          params:
#             symbol (str): the trading pair.
#          """
#         check_require_params(kwargs, ('symbol',))
#         return self.return_args(method='subscribe',
#                                 url=URLS.WS_BASE_URL,
#                                 params={'channel': 'spot.trades',
#                                         'payload': [kwargs.get('symbol')],
#                                         },
#                                 )
