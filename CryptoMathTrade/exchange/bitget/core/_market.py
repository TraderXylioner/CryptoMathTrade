from .._urls import URLS
from ..._core import Core
from ...utils import check_require_params


class MarketCore(Core):
    def get_depth_args(self, **kwargs) -> dict:
        """Get orderbook.

        GET /api/v2/spot/market/orderbook

        https://www.bitget.com/api-doc/spot/market/Get-Orderbook

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 150; max 150.

            type (str, optional) The value enums：step0，step1，step2，step3，step4，step5. Default: step0.
        """
        check_require_params(kwargs, ('symbol',))
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=kwargs)

    def get_trades_args(self, **kwargs) -> dict:
        """Recent Trades List

        GET /api/v2/spot/market/fills

        https://www.bitget.com/api-doc/spot/market/Get-Recent-Trades

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Default 100; max 500.
        """
        check_require_params(kwargs, ('symbol',))
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=kwargs)

    def get_ticker_args(self, **kwargs) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v2/spot/market/tickers

        https://www.bitget.com/api-doc/spot/market/Get-Tickers

        params:
            symbol (str, optional): the trading pair.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TICKER_URL, params=kwargs)


class WSMarketCore(Core):
    def get_depth_args(self, **kwargs) -> dict:
        """Partial Book Depth Streams

        Stream Names: books{limit}

        https://www.bitget.com/api-doc/spot/websocket/public/Depth-Channel

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Valid are 1, 5 or 15.

        """
        check_require_params(kwargs, ('symbol',))
        chanel = f'books{kwargs["limit"]}' if 'limit' in kwargs else 'books'
        return self.return_args(method='subscribe',
                                url=URLS.WS_BASE_URL,
                                params=[{'instType': 'SPOT',
                                         'channel': chanel,
                                         'instId': kwargs['symbol'],
                                         }]
                                )

    def get_trades_args(self, **kwargs) -> dict:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: trade

        https://www.bitget.com/api-doc/spot/websocket/public/Trades-Channel

         params:
            symbol (str): the trading pair.
         """
        check_require_params(kwargs, ('symbol',))
        return self.return_args(method='subscribe',
                                url=URLS.WS_BASE_URL,
                                params=[{'instType': 'SPOT',
                                         'channel': 'trade',
                                         'instId': kwargs['symbol'],
                                         }]
                                )
