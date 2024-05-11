from ._urls import URLS
from .._core import Core
from ..errors import ParameterValueError
from ..utils import _convert_kwargs_to_dict


class MarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Get orderbook.

        GET /api/v3/depth

        https://binance-docs.github.io/apidocs/spot/en/#order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 5000. If limit > 5000, then the response will truncate to 5000.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=params)

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Recent Trades List
        Get recent trades (up to last 500).

        GET /api/v3/trades

        https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 500; max 1000.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=params)

    @_convert_kwargs_to_dict
    def get_ticker_args(self, params: dict) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair

            symbols (list, optional): list of trading pairs
        """
        if params.get('symbol') and params.get('symbols'):
            raise ParameterValueError(msg='symbol and symbols cannot be sent together.')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TICKER_URL, params=params)


class SpotCore(Core):
    @_convert_kwargs_to_dict
    def get_orders_args(self, SpotObj, params: dict) -> dict:
        """All Orders (USER_DATA)

        Get all account orders; active, canceled, or filled.

        GET /api/v3/allOrders

        https://binance-docs.github.io/apidocs/spot/en/#all-orders-user_data

        params:
            symbol (str)

            orderId (int, optional)

            startTime (int, optional)

            endTime (int, optional)

            limit (int, optional): Default 500; max 1000.

            recvWindow (int, optional): The value cannot be greater than 60000
        """
        return self.return_args(method='GET',
                                url=URLS.BASE_URL + URLS.GET_ORDERS_URL,
                                params=SpotObj.get_payload(params),
                                )

    @_convert_kwargs_to_dict
    def get_open_order_args(self, SpotObj, params: dict) -> dict:
        """Query Order (USER_DATA)

        Check an order's status.

        GET /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#query-order-user_data

        params:
            symbol (str)

            orderId (int, optional)

            origClientOrderId (str, optional)

            recvWindow (int, optional): The value cannot be greater than 60000
        """
        if not params.get('orderId') and not params.get('origClientOrderId'):
            raise ParameterValueError('Param "origClientOrderId" or "orderId" must be sent, but both were empty/null!')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.ORDER_URL, params=SpotObj.get_payload(params))

    @_convert_kwargs_to_dict
    def get_open_orders_args(self, SpotObj, params: dict) -> dict:
        """Current Open Orders (USER_DATA)

        Get all open orders on a symbol.

        GET /api/v3/openOrders

        https://binance-docs.github.io/apidocs/spot/en/#current-open-orders-user_data

        params:
            symbol (str, optional)

            recvWindow (int, optional): The value cannot be greater than 60000
        """
        return self.return_args(method='GET',
                                url=URLS.BASE_URL + URLS.OPEN_ORDERS_URL,
                                params=SpotObj.get_payload(params),
                                )

    @_convert_kwargs_to_dict
    def cancel_open_order_args(self, SpotObj, params: dict) -> dict:
        """Cancel Order (TRADE)

        Cancel an active order.

        DELETE /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#cancel-order-trade

        params:
            symbol (str)

            orderId (int, optional)

            origClientOrderId (str, optional)

            newClientOrderId (str, optional)

            recvWindow (int, optional): The value cannot be greater than 60000
        """
        return self.return_args(method='DELETE', url=URLS.BASE_URL + URLS.CANCEL_ORDER_URL, params=SpotObj.get_payload(params))

    @_convert_kwargs_to_dict
    def cancel_open_orders_args(self, SpotObj, params: dict) -> dict:
        """Cancel Order (TRADE)

        Cancel an active order.

        DELETE /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#cancel-order-trade

        params:
            symbol (str)

            recvWindow (int, optional): The value cannot be greater than 60000
        """
        return self.return_args(method='DELETE',
                                url=URLS.BASE_URL + URLS.CANCEL_ORDERS_URL,
                                params=SpotObj.get_payload(params),
                                )

    @_convert_kwargs_to_dict
    def new_order_args(self, SpotObj, params: dict) -> dict:
        """New Order (TRADE)

        Post a new order

        POST /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#new-order-trade

        params:
            symbol (str)

            side (str)

            old_type (str)

            timeInForce (str, optional)

            quantity (float, optional)

            quoteOrderQty (float, optional)

            price (float, optional)

            newClientOrderId (str, optional): A unique id among open orders. Automatically generated if not sent.

            strategyId (int, optional)

            strategyType (int, optional): The value cannot be less than 1000000.

            stopPrice (float, optional): Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.

            icebergQty (float, optional): Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.

            newOrderRespType (str, optional): Set the response JSON. ACK, RESULT, or FULL;
                    MARKET and LIMIT order types default to FULL, all other orders default to ACK.

            recvWindow (int, optional): The value cannot be greater than 60000
        """
        return self.return_args(method='POST', url=URLS.BASE_URL + URLS.CREATE_ORDER_URL, params=SpotObj.get_payload(params))


class AccountCore(Core):
    @_convert_kwargs_to_dict
    def get_balance_args(self, AccountObj, params):
        """Query Assets

        POST /sapi/v3/asset/getUserAsset

        https://binance-docs.github.io/apidocs/spot/en/#user-asset-user_data

        params:
            asset (int, optional): If asset is blank, then query all positive assets user have.
        """
        return self.return_args(method='POST',
                                url=URLS.BASE_URL + URLS.GET_BALANCE,
                                params=AccountObj.get_payload(params),
                                )


class WSMarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Partial Book Depth Streams

        Stream Names: <symbol>@depth<levels> OR <symbol>@depth<levels>@100ms.

        https://binance-docs.github.io/apidocs/spot/en/#partial-book-depth-streams

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Valid are 5, 10, or 20.

            interval (int, optional): 1000ms or 100ms.
        """

        return self.return_args(method='SUBSCRIBE',
                                url=URLS.WS_BASE_URL,
                                params=f'{params["symbol"].lower()}@depth{params["limit"]}@{params["update_time"]}ms',
                                )

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: <symbol>@trade

         https://binance-docs.github.io/apidocs/spot/en/#trade-streams

         param:
            symbol (str): the trading pair
         """
        return self.return_args(method='SUBSCRIBE', url=URLS.WS_BASE_URL, params=f'{params["symbol"].lower()}@trade')
