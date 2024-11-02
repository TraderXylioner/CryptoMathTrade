from ..api.api import API
from ..urls import URLS
from ...errors import ParameterValueError
from ...utils import replace_param, check_require_params


class SpotCore(API):
    @check_require_params(("symbol",))
    def get_orders(self, **params) -> dict:
        """All Orders (USER_DATA)

        Get all account orders; active, canceled, or filled.

        GET /api/v3/allOrders

        https://binance-docs.github.io/apidocs/spot/en/#all-orders-user_data

        params:
            symbol (str)

            limit (int, optional): Default 500; max 1000.

            orderId (int, optional)

            startTime (int, optional)

            endTime (int, optional)
        """
        return self.return_args(
            method="GET",
            url=URLS.BASE_URL + URLS.GET_ORDERS_URL,
            params=self.get_payload(params),
        )

    @check_require_params(("symbol",))
    def get_open_order(self, **params) -> dict:
        """Query Order (USER_DATA)

        Check an order's status.

        GET /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#query-order-user_data

        params:
            symbol (str)

            orderId (int, optional)

            clientOrderID (str, optional)
        """
        replace_param(params, "clientOrderID", "origClientOrderId")
        if not params.get("orderId") and not params.get("origClientOrderId"):
            raise ParameterValueError(
                'Param "clientOrderID" or "orderId" must be sent, but both were empty/null!'
            )
        return self.return_args(
            method="GET",
            url=URLS.BASE_URL + URLS.ORDER_URL,
            params=self.get_payload(params),
        )

    def get_open_orders(self, **params) -> dict:
        """Current Open Orders (USER_DATA)

        Get all open orders on a symbol.

        GET /api/v3/openOrders

        https://binance-docs.github.io/apidocs/spot/en/#current-open-orders-user_data

        params:
            symbol (str, optional)
        """
        return self.return_args(
            method="GET",
            url=URLS.BASE_URL + URLS.OPEN_ORDERS_URL,
            params=self.get_payload(params),
        )

    @check_require_params(("symbol",))
    def cancel_open_order(self, **params) -> dict:
        """Cancel Order (TRADE)

        Cancel an active order.

        DELETE /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#cancel-order-trade

        params:
            symbol (str)

            orderId (int, optional)

            clientOrderID (str, optional)

            newClientOrderId (str, optional)
        """
        replace_param(params, "clientOrderID", "origClientOrderId")
        return self.return_args(
            method="DELETE",
            url=URLS.BASE_URL + URLS.CANCEL_ORDER_URL,
            params=self.get_payload(params),
        )

    @check_require_params(("symbol",))
    def cancel_open_orders(self, **params) -> dict:
        """Cancel Order (TRADE)

        Cancel an active order.

        DELETE /api/v3/openOrders

        https://binance-docs.github.io/apidocs/spot/en/#cancel-all-open-orders-on-a-symbol-trade

        params:
            symbol (str)
        """
        return self.return_args(
            method="DELETE",
            url=URLS.BASE_URL + URLS.CANCEL_ORDERS_URL,
            params=self.get_payload(params),
        )

    @check_require_params(("symbol", "side"))
    def new_order(self, **params) -> dict:
        """New Order (TRADE)

        Post a new order

        POST /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#new-order-trade

        params:
        for market order:
            symbol (str)

            side (str)

            quantity (float, optional)

            quoteOrderQty (float, optional)

        for limit order:
            symbol (str)

            side (str)

            price (float)

            quantity (float)

            timeInForce (str, optional)  # TODO:
        """
        return self.return_args(
            method="POST",
            url=URLS.BASE_URL + URLS.CREATE_ORDER_URL,
            params=self.get_payload(params),
        )
