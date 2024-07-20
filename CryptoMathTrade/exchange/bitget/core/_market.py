from .._api import API
from .._urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(('symbol',))
    def get_depth(self, **kwargs) -> dict:
        """Get orderbook.

        GET /api/v2/spot/market/orderbook

        https://www.bitget.com/api-doc/spot/market/Get-Orderbook

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 150; max 150.

            type (str, optional) The value enums：step0，step1，step2，step3，step4，step5. Default: step0.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=kwargs)

    @check_require_params(('symbol',))
    def get_trades(self, **kwargs) -> dict:
        """Recent Trades List

        GET /api/v2/spot/market/fills

        https://www.bitget.com/api-doc/spot/market/Get-Recent-Trades

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 100; max 500.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=kwargs)

    def get_ticker(self, **kwargs) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v2/spot/market/tickers

        https://www.bitget.com/api-doc/spot/market/Get-Tickers

        params:
            symbol (str, optional): the trading pair.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TICKER_URL, params=kwargs)

    def get_symbols(self, **kwargs) -> dict:
        """Query Symbols

        GET /api/v2/spot/public/symbols

        https://www.bitget.com/api-doc/spot/market/Get-Symbols

        params:
            symbol (str, optional): the trading pair.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.SYMBOLS_URL, params=kwargs)

    @check_require_params(('symbol', 'interval'))
    def get_kline(self, **kwargs) -> dict:
        """Historical K-line data

        GET /api/v2/spot/market/candles

        https://www.bitget.com/api-doc/spot/market/Get-Candle-Data

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1m, 3m, 5m can query for one month,15m can query for 52 days,30m can query for 62 days,1H can query for 83 days,2H can query for 120 days,4H can query for 240 days,6H can query for 360 days.).

            limit (int, optional): Default 100; max 1000.

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.
        """
        replace_param(kwargs, 'interval', 'granularity')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.KLINE_URL, params=kwargs)

# TODO: WSMarketCore

# class WSMarketCore(Core):
#     def get_depth_args(self, **kwargs) -> dict:
#         """Partial Book Depth Streams
#
#         Stream Names: books{limit}
#
#         https://www.bitget.com/api-doc/spot/websocket/public/Depth-Channel
#
#         params:
#             symbol (str): the trading pair.
#
#             limit (int, optional): limit the results. Valid are 1, 5 or 15.
#
#         """
#         check_require_params(kwargs, ('symbol',))
#         chanel = f'books{kwargs["limit"]}' if 'limit' in kwargs else 'books'
#         return self.return_args(method='subscribe',
#                                 url=URLS.WS_BASE_URL,
#                                 params=[{'instType': 'SPOT',
#                                          'channel': chanel,
#                                          'instId': kwargs['symbol'],
#                                          }]
#                                 )
#
#     def get_trades_args(self, **kwargs) -> dict:
#         """Trade Streams
#
#          The Trade Streams push raw trade information; each trade has a unique buyer and seller.
#          Update Speed: Real-time
#
#          Stream Name: trade
#
#         https://www.bitget.com/api-doc/spot/websocket/public/Trades-Channel
#
#          params:
#             symbol (str): the trading pair.
#          """
#         check_require_params(kwargs, ('symbol',))
#         return self.return_args(method='subscribe',
#                                 url=URLS.WS_BASE_URL,
#                                 params=[{'instType': 'SPOT',
#                                          'channel': 'trade',
#                                          'instId': kwargs['symbol'],
#                                          }]
#                                 )
