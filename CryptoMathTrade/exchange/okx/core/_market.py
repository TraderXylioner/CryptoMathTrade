from .._urls import URLS
from ..._core import Core
from ...utils import check_require_params, replace_param


class MarketCore(Core):
    def get_depth_args(self, **kwargs) -> dict:
        """Get orderbook.

        GET /api/v5/market/books

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 1; max 400.
        """
        check_require_params(kwargs, ('symbol',))
        replace_param(kwargs, 'symbol', 'instId')
        replace_param(kwargs, 'limit', 'sz')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=kwargs)

    def get_trades_args(self, **kwargs) -> dict:
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

    def get_ticker_args(self, **kwargs) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v5/market/ticker or /api/v5/market/tickers

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-ticker
        or
        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-tickers

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        _url = URLS.TICKER_URL if 'symbol' in kwargs else URLS.TICKERS_URL
        if 'symbol' in kwargs:
            kwargs['symbol'] += '-SWAP'
            replace_param(kwargs, 'symbol', 'instId')
        else:
            kwargs['instType'] = 'SPOT'
        return self.return_args(method='GET', url=URLS.BASE_URL + _url, params=kwargs)


class WSMarketCore(Core):
    def get_depth_args(self, **kwargs) -> dict:
        """Partial Book Depth Streams

        Stream Names: books

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-order-book-channel

        param:
            symbol (str): the trading pair

        """
        return self.return_args(method='subscribe',
                                url=URLS.WS_BASE_URL,
                                params=[{"channel": "books", "instId": kwargs['symbol']}],
                                )

    def get_trades_args(self, **kwargs) -> dict:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: trades

         https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-trades-channel

         param:
            symbol (str): the trading pair
         """
        return self.return_args(method='subscribe',
                                url=URLS.WS_BASE_URL,
                                params=[{"channel": "trades", "instId": kwargs['symbol']}],
                                )
