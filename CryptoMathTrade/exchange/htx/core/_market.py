from .._api import API
from .._urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(('symbol',))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /market/depth

        https://huobiapi.github.io/docs/spot/v1/en/#get-market-depth

        when type is set to "step0", the default value of "depth" is 150 instead of 20.

        step0	No market depth aggregation
        step1	Aggregation level = precision*10
        step2	Aggregation level = precision*100
        step3	Aggregation level = precision*1000
        step4	Aggregation level = precision*10000
        step5	Aggregation level = precision*100000

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 20 or 150; max 20 or 150.

            type (str, optional): Market depth aggregation level, details below	step0, step1, step2, step3, step4, step5. Default step0.
        """
        replace_param(params, 'limit', 'depth')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=params)

    @check_require_params(('symbol',))
    def get_trades(self, **params) -> dict:
        """Recent Trades List

        GET /market/history/trade

        https://huobiapi.github.io/docs/spot/v1/en/#get-the-most-recent-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 1; max 2000.
        """
        replace_param(params, 'limit', 'size')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=params)

    def get_ticker(self, **params) -> dict:
        """24hr Ticker Price Change Statistics

        GET /market/detail/merged or /market/tickers

        https://huobiapi.github.io/docs/spot/v1/en/#get-latest-aggregated-ticker
        or
        https://huobiapi.github.io/docs/spot/v1/en/#get-latest-tickers-for-all-pairs

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        _url = URLS.TICKER_URL if params.get('symbol') else URLS.TICKERS_URL
        return self.return_args(method='GET', url=URLS.BASE_URL + _url, params=params)

    def get_symbols(self, **params) -> dict:
        """Query Symbols

        GET /v2/settings/common/symbols

        https://huobiapi.github.io/docs/spot/v1/en/#get-all-supported-trading-symbol-v2
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.SYMBOLS_URL, params=params)

    @check_require_params(('symbol', 'interval'))
    def get_kline(self, **params) -> dict:
        """Historical K-line data

        GET /market/history/kline

        https://huobiapi.github.io/docs/spot/v1/en/#get-klines-candles

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1min, 5min, 15min, 30min, 60min, 4hour, 1day, 1mon, 1week, 1year).

            limit (int, optional): Default 150; max 2000.
        """
        replace_param(params, 'interval', 'period')
        replace_param(params, 'limit', 'size')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.KLINE_URL, params=params)

# TODO: WebSocketMarketCore

# class WebSocketMarketCore(Core):
#     def get_depth_args(self, **kwargs) -> dict:
#         """Partial Book Depth Streams
#
#         Stream Names: market.{symbol}.depth.{type}
#
#         https://www.htx.com/en-us/opend/newApiPages/?id=7ec5342e-7773-11ed-9966-0242ac110003
#
#         param:
#             symbol (str): the trading pair
#
#             type (str, optional): Market depth aggregation level, details below	step0, step1, step2, step3, step4, step5. Default step0.
#
#         when type is set to "step0", the default value of "depth" is 150 instead of 20.
#
#         step0	No market depth aggregation
#         step1	Aggregation level = precision*10
#         step2	Aggregation level = precision*100
#         step3	Aggregation level = precision*1000
#         step4	Aggregation level = precision*10000
#         step5	Aggregation level = precision*100000
#
#         """
#         check_require_params(kwargs, ('symbol',))
#         return self.return_args(method='sub',
#                                 url=URLS.WS_BASE_URL,
#                                 params=f'market.{kwargs["symbol"].lower()}.depth.{kwargs["type"]}',
#                                 )
#
#     def get_trades_args(self, **kwargs) -> dict:
#         """Trade Streams
#
#          The Trade Streams push raw trade information; each trade has a unique buyer and seller.
#          Update Speed: Real-time
#
#          Stream Name: market.{symbol}.trade.detail
#
#          https://www.htx.com/en-us/opend/newApiPages/?id=7ec53b69-7773-11ed-9966-0242ac110003
#
#          param:
#             symbol (str): the trading pair
#          """
#         check_require_params(kwargs, ('symbol',))
#         return self.return_args(method='sub',
#                                 url=URLS.WS_BASE_URL,
#                                 params=f'market.{kwargs["symbol"].lower()}.trade.detail',
#                                 )
