from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /api/v3/depth

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 5000. If limit > 5000, then the response will truncate to 5000.
        """
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params
        )

    @check_require_params(("symbol",))
    def get_trades(self, **params) -> dict:
        """Recent Trades List
        Get recent trades (up to last 500).

        GET /api/v3/trades

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#recent-trades-list

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 500; max 1000.
        """
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.TRADES_URL, params=params
        )

    def get_ticker(self, **params) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.TICKER_URL, params=params
        )

    def get_symbols(self, **params) -> dict:
        """Query Symbols

        GET /open/api/v2/market/symbols

        https://mexcdevelop.github.io/apidocs/spot_v2_en/#all-symbols
        """
        return self.return_args(
            method="GET", url=URLS.BASE2_URL + URLS.SYMBOLS_URL, params=params
        )

    @check_require_params(("symbol", "interval"))
    def get_kline(self, **params) -> dict:
        """Historical K-line data

        GET /api/v3/klines

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#kline-candlestick-data

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1m, 5m, 15m, 30m, 60m, 4h, 1d, 1W, 1M).

            limit (int, optional): Default 500; max 1000.

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.
        """
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.KLINE_URL, params=params
        )


# TODO: WebSocketMarketCore

# class WebSocketMarketCore(Core):
#     def get_depth_args(self, **kwargs) -> dict:
#         """Partial Book Depth Streams
#
#         Stream Names: spot@public.limit.depth.v3.api@<symbol>@<level>.
#
#         https://mexcdevelop.github.io/apidocs/spot_v3_en/#partial-book-depth-streams
#
#         param:
#             symbol (str): the trading pair
#
#             limit (int, optional): limit the results. Valid are 5, 10, or 20.
#
#         """
#         check_require_params(kwargs, ('symbol',))
#         return self.return_args(method='SUBSCRIPTION',
#                                 url=URLS.WS_BASE_URL,
#                                 params=f'spot@public.limit.depth.v3.api@{kwargs["symbol"].upper()}@{kwargs["limit"]}',
#                                 )
#
#     def get_trades_args(self, **kwargs) -> dict:
#         """Trade Streams
#
#          The Trade Streams push raw trade information; each trade has a unique buyer and seller.
#          Update Speed: Real-time
#
#          Stream Name: spot@public.deals.v3.api@<symbol>
#
#          https://mexcdevelop.github.io/apidocs/spot_v3_en/#trade-streams
#
#          param:
#             symbol (str): the trading pair
#          """
#         check_require_params(kwargs, ('symbol',))
#         return self.return_args(method='SUBSCRIPTION',
#                                 url=URLS.WS_BASE_URL,
#                                 params=f'spot@public.deals.v3.api@{kwargs["symbol"].upper()}',
#                                 )
