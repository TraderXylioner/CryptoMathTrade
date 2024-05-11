from ._urls import URLS
from .._core import Core
from ..utils import _convert_kwargs_to_dict


class MarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Get orderbook.

        GET /api/v4/spot/order_book

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-order-book

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 10; max 5000.
        """
        if 'symbol' in params:
            params['currency_pair'] = params['symbol']
            params.pop('symbol')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=params)

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Recent Trades List

        GET /api/v4/spot/trades

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-market-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 1000.
        """
        if 'symbol' in params:
            params['currency_pair'] = params['symbol']
            params.pop('symbol')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=params)

    @_convert_kwargs_to_dict
    def get_ticker_args(self, params: dict) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v4/spot/tickers

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-ticker-information

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned.
        """
        if 'symbol' in params:
            params['currency_pair'] = params['symbol']
            params.pop('symbol')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TICKER_URL, params=params)


class WSMarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Partial Book Depth Streams

        Stream Names: spot.order_book_update

        https://www.gate.io/docs/developers/apiv4/ws/en/#changed-order-book-levels

        param:

            symbol (str): the trading pair

            limit (int, optional): limit the results. Valid are 5, 10, 20, 50 or 100.

            interval (int, optional): 1000ms or 100ms.

        """
        return self.return_args(method='subscribe',
                                url=URLS.WS_BASE_URL,
                                params={'channel': 'spot.order_book',
                                        'payload': [params.get('symbol'),
                                                    str(params.get('limit')),
                                                    f'{params.get("interval")}ms'],
                                        },
                                )

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: spot.trades

         https://www.gate.io/docs/developers/apiv4/ws/en/#client-subscription-2

         param:
            symbol (str): the trading pair
         """
        return self.return_args(method='subscribe',
                                url=URLS.WS_BASE_URL,
                                params={'channel': 'spot.trades',
                                        'payload': [params.get('symbol')],
                                        },
                                )
