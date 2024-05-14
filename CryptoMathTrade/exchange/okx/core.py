from ._urls import URLS
from .._core import Core
from ..utils import _convert_kwargs_to_dict


class MarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Get orderbook.

        GET /api/v5/market/books

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 1; max 400.
        """
        if 'symbol' in params:
            params['instId'] = params['symbol']
            params.pop('symbol')
        if 'limit' in params:
            params['sz'] = params['limit']
            params.pop('limit')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=params)

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Recent Trades List
        Get recent trades (up to last 500).

        GET /api/v5/market/trades

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 500.
        """
        if 'symbol' in params:
            params['instId'] = params['symbol']
            params.pop('symbol')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=params)

    @_convert_kwargs_to_dict
    def get_ticker_args(self, params: dict) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v5/market/ticker or /api/v5/market/tickers

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-ticker
        or
        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-tickers

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        _url = URLS.TICKER_URL if 'symbol' in params else URLS.TICKERS_URL
        if 'symbol' in params:
            params['instId'] = params['symbol'] + '-SWAP'
            params.pop('symbol')
        else:
            params['instType'] = 'SPOT'
        return self.return_args(method='GET', url=URLS.BASE_URL + _url, params=params)


class WSMarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Partial Book Depth Streams

        Stream Names: books

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-order-book-channel

        param:
            symbol (str): the trading pair

        """
        return self.return_args(method='subscribe',
                                url=URLS.WS_BASE_URL,
                                params=[{"channel": "books", "instId": params['symbol']}],
                                )

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
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
                                params=[{"channel": "trades", "instId": params['symbol']}],
                                )
