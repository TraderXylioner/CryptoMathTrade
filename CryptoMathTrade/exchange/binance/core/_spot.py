from .._urls import URLS
from ..._core import Core
from ...errors import ParameterValueError
from ...utils import _convert_kwargs_to_dict


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
        return self.return_args(method='DELETE',
                                url=URLS.BASE_URL + URLS.CANCEL_ORDER_URL,
                                params=SpotObj.get_payload(params),
                                )

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
        return self.return_args(method='POST',
                                url=URLS.BASE_URL + URLS.CREATE_ORDER_URL,
                                params=SpotObj.get_payload(params),
                                )
