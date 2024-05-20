from ._urls import URLS
from .._core import Core
from ..utils import _convert_kwargs_to_dict


class MarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Get orderbook.

        GET /api/v2/spot/market/orderbook

        https://www.bitget.com/api-doc/spot/market/Get-Orderbook

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 150; max 150.

            type (str, optional) The value enums：step0，step1，step2，step3，step4，step5. Default: step0.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=params)

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /api/v2/spot/market/fills

        https://www.bitget.com/api-doc/spot/market/Get-Recent-Trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 500.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=params)

    @_convert_kwargs_to_dict
    def get_ticker_args(self, params: dict) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v2/spot/market/tickers

        https://www.bitget.com/api-doc/spot/market/Get-Tickers

        params:
            symbol (str, optional): the trading pair
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TICKER_URL, params=params)


class WSMarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Partial Book Depth Streams

        Stream Names: books{limit}

        https://www.bitget.com/api-doc/spot/websocket/public/Depth-Channel

        param:

            symbol (str): the trading pair

            limit (int, optional): limit the results. Valid are 1, 5 or 15.

        """
        chanel = f'books{params["limit"]}' if 'limit' in params else 'books'
        return self.return_args(method='subscribe',
                                url=URLS.WS_BASE_URL,
                                params=[{'instType': 'SPOT',
                                         'channel': chanel,
                                         'instId': params['symbol'],
                                         }]
                                )

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: trade

        https://www.bitget.com/api-doc/spot/websocket/public/Trades-Channel

         param:
            symbol (str): the trading pair
         """
        return self.return_args(method='subscribe',
                                url=URLS.WS_BASE_URL,
                                params=[{'instType': 'SPOT',
                                         'channel': 'trade',
                                         'instId': params['symbol'],
                                         }]
                                )


class AccountCore(Core):
    @_convert_kwargs_to_dict
    def get_balance_args(self, AccountObj, params=None):
        """Query Assets

        GET /api/v2/spot/account/assets

        https://www.bitget.com/api-doc/spot/account/Get-Account-Assets

        params:
            coin (str, optional): default all coin
        """
        self.headers = AccountObj.get_payload(path=URLS.GET_BALANCE, method='GET', payload=params)
        return self.return_args(method='GET',
                                url=URLS.BASE_URL + URLS.GET_BALANCE,
                                params=params
                                )
