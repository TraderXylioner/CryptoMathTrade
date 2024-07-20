from .._api import API
from .._urls import URLS
from ...utils import check_require_params, replace_param


class MarketCore(API):
    @check_require_params(('symbol',))
    def get_depth(self, **kwargs) -> dict:
        """Get orderbook.

        GET /api/v5/market/books

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 1; max 400.
        """
        replace_param(kwargs, 'symbol', 'instId')
        replace_param(kwargs, 'limit', 'sz')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=kwargs)

    @check_require_params(('symbol',))
    def get_trades(self, **kwargs) -> dict:
        """Recent Trades List
        Get recent trades (up to last 500).

        GET /api/v5/market/trades

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 500.
        """
        replace_param(kwargs, 'symbol', 'instId')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=kwargs)

    def get_ticker(self, **kwargs) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v5/market/ticker or /api/v5/market/tickers

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-ticker
        or
        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-tickers

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        _url = URLS.TICKER_URL if kwargs.get('symbol') else URLS.TICKERS_URL
        if kwargs.get('symbol'):
            kwargs['symbol'] += '-SWAP'
            replace_param(kwargs, 'symbol', 'instId')
        else:
            kwargs['instType'] = 'SPOT'
        return self.return_args(method='GET', url=URLS.BASE_URL + _url, params=kwargs)

    def get_symbols(self, **kwargs) -> dict:
        """Query Symbols

        GET /api/v5/public/instruments

        https://www.okx.com/docs-v5/en/#public-data-rest-api-get-instruments

        params:
            symbol (str, optional): the trading pair
        """
        kwargs['instType'] = 'SPOT'
        replace_param(kwargs, 'symbol', 'instId')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.SYMBOLS_URL, params=kwargs)

    @check_require_params(('symbol',))
    def get_kline(self, **kwargs) -> dict:
        """Historical K-line data

        GET /api/v5/market/history-candles

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-candlesticks-history

        params:
            symbol (str): the trading pair.

            interval (str, optional): Default 1m; Time interval (1s, 1m, 3m, 5m, 15m, 30m, 1H, 2H, 4H, 6H, 12H, 1D, 2D, 3D, 1W, 1M, 3M).

            limit (int, optional): Default 100; max 100.

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.
        """
        replace_param(kwargs, 'symbol', 'instId')
        replace_param(kwargs, 'startTime', 'after')
        replace_param(kwargs, 'endTime', 'before')
        replace_param(kwargs, 'interval', 'bar')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.KLINE_URL, params=kwargs)

# TODO: WSMarketCore

# class WSMarketCore(Core):
#     def get_depth_args(self, **kwargs) -> dict:
#         """Partial Book Depth Streams
#
#         Stream Names: books
#
#         https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-order-book-channel
#
#         param:
#             symbol (str): the trading pair
#
#         """
#         return self.return_args(method='subscribe',
#                                 url=URLS.WS_BASE_URL,
#                                 params=[{"channel": "books", "instId": kwargs['symbol']}],
#                                 )
#
#     def get_trades_args(self, **kwargs) -> dict:
#         """Trade Streams
#
#          The Trade Streams push raw trade information; each trade has a unique buyer and seller.
#          Update Speed: Real-time
#
#          Stream Name: trades
#
#          https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-trades-channel
#
#          param:
#             symbol (str): the trading pair
#          """
#         return self.return_args(method='subscribe',
#                                 url=URLS.WS_BASE_URL,
#                                 params=[{"channel": "trades", "instId": kwargs['symbol']}],
#                                 )
