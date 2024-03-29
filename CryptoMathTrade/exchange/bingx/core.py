from ._urls import URLS
from .._core import Core
from ..utils import _convert_kwargs_to_dict, get_timestamp


class MarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Get orderbook.

        GET /openApi/spot/v1/market/depth

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20depth%20information

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 1000. If limit > 1000, then the response will truncate to 1000

            recvWindow (int, optional).
        """
        params['limit'] = min(int(params.get('limit', 100)), 1000)
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=params)

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /openApi/spot/v1/market/trades

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20transaction%20records

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 100

            recvWindow (int, optional).
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=params)

    @_convert_kwargs_to_dict
    def get_ticker_args(self, params: dict) -> dict:
        """24hr Ticker Price Change Statistics

        GET /openApi/spot/v1/ticker/24hr

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#24-hour%20price%20changes

        params:
            symbol (str, optional): the trading pair.
        """
        params['timestamp'] = get_timestamp()
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TICKER_URL, params=params)


class SpotCore(Core):
    @_convert_kwargs_to_dict
    def get_orders_args(self, SpotObj, params):
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.GET_ORDERS_URL, params=SpotObj.get_payload(params))

    @_convert_kwargs_to_dict
    def get_open_order_args(self, SpotObj, params):
        if not params.get('orderId') and not params.get('origClientOrderId'):
            raise ValueError('Param "origClientOrderId" or "orderId" must be sent, but both were empty/null!')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.ORDER_URL, params=SpotObj.get_payload(params))

    @_convert_kwargs_to_dict
    def get_open_orders_args(self, SpotObj, params):
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.OPEN_ORDERS_URL, params=SpotObj.get_payload(params))

    @_convert_kwargs_to_dict
    def cancel_open_order_args(self, SpotObj, params: dict) -> dict:
        return self.return_args(method='POST', url=URLS.BASE_URL + URLS.CANCEL_ORDER_URL, params=SpotObj.get_payload(params))

    @_convert_kwargs_to_dict
    def cancel_open_orders_args(self, SpotObj, params: dict) -> dict:
        return self.return_args(method='POST', url=URLS.BASE_URL + URLS.CANCEL_ORDERS_URL, params=SpotObj.get_payload(params))

    @_convert_kwargs_to_dict
    def new_order_args(self, SpotObj, params: dict) -> dict:
        return self.return_args(method='POST', url=URLS.BASE_URL + URLS.CREATE_ORDER_URL, params=SpotObj.get_payload(params))


class WSMarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Partial Book Depth Streams

        Top bids and asks.

        Stream Names: <symbol>@depth<levels>.

        param:
            symbol (str): the trading pair
        """
        return self.return_args(method='sub', url=URLS.WS_BASE_URL, params=f'{params["symbol"]}@depth')

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: <symbol>@trade

         param:
            symbol (str): the trading pair
         """
        return self.return_args(method='sub', url=URLS.WS_BASE_URL, params=f'{params["symbol"]}@trade')


class AccountCore(Core):
    @_convert_kwargs_to_dict
    def get_balance_args(self, AccountObj, params):
        """Query Assets

        GET /openApi/spot/v1/account/balance

        https://bingx-api.github.io/docs/#/en-us/common/account-api.html#Query%20Assets

        params:
            recvWindow (int, optional): The value cannot be greater than 60000
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.GET_BALANCE, params=AccountObj.get_payload(params))
