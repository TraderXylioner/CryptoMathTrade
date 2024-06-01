from .._urls import URLS
from ..._core import Core
from ...utils import check_require_params


class MarketCore(Core):
    def get_depth_args(self, **kwargs) -> dict:
        """Get orderbook.

        GET /spot/quotation/v3/books

        https://developer-pro.bitmart.com/en/spot/#get-depth-v3

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 35; max 50.
        """
        check_require_params(kwargs, ('symbol',))
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=kwargs)

    def get_trades_args(self, **kwargs) -> dict:
        """Recent Trades List

        GET /spot/quotation/v3/trades

        https://developer-pro.bitmart.com/en/spot/#get-recent-trades-v3

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 50; max 50.
        """
        check_require_params(kwargs, ('symbol',))
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=kwargs)

    def get_ticker_args(self, **kwargs) -> dict:
        """24hr Ticker Price Change Statistics

        GET /spot/quotation/v3/ticker or /spot/quotation/v3/tickers

        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-a-trading-pair-v3
        or
        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-all-pairs-v3

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        _url = URLS.TICKER_URL if 'symbol' in kwargs else URLS.TICKERS_URL
        return self.return_args(method='GET', url=URLS.BASE_URL + _url, params=kwargs)


class WSMarketCore(Core):
    def get_depth_args(self, **kwargs) -> dict:
        """Partial Book Depth Streams

        Stream Names: spot/depth{limit}:{symbol}

        https://developer-pro.bitmart.com/en/spot/#public-depth-all-channel

        param:

            symbol (str): the trading pair

            limit (int, optional): limit the results. Valid are 5, 20 or 50.

        """
        return self.return_args(method='subscribe',
                                url=URLS.WS_BASE_URL,
                                params=f'spot/depth{kwargs["limit"]}:{kwargs["symbol"]}',
                                )

    def get_trades_args(self, **kwargs) -> dict:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: spot/trade:{symbol}

        https://developer-pro.bitmart.com/en/spot/#public-trade-channel-2

         param:
            symbol (str): the trading pair
         """
        return self.return_args(method='subscribe',
                                url=URLS.WS_BASE_URL,
                                params=f'spot/trade:{kwargs["symbol"]}',
                                )
