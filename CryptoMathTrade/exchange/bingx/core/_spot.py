from .._api import API
from .._urls import URLS


class SpotCore(API):
    def get_orders(self, **kwargs) -> dict:
        """All Orders (USER_DATA)

        Get all account orders; active, canceled, or filled.

        GET /openApi/spot/v1/trade/historyOrders

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Query%20Order%20History

        params:
            symbol (str).

            orderId (int, optional).

            status: (str, optional) FILLED / CANCELED / FAILED.

            type: (str, optional) MARKET / LIMIT / TAKE_STOP_LIMIT / TAKE_STOP_MARKET / TRIGGER_LIMIT / TRIGGER_MARKET.

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.

            pageIndex: (int, optional), Default: 1.

            pageSize: (int, optional), Default: 100, Max 100.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.GET_ORDERS_URL, params=self.get_payload(kwargs))

    def get_open_order(self, **kwargs) -> dict:
        """Query Order (USER_DATA)

        Check an order's status.

        GET /openApi/spot/v1/trade/query

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Query%20Orders

        params:
            symbol (str)

            orderId (int, optional)

            clientOrderID (str, optional)
        """
        if not kwargs.get('orderId') and not kwargs.get('origClientOrderId'):
            raise ValueError('Param "origClientOrderId" or "orderId" must be sent, but both were empty/null!')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.ORDER_URL, params=self.get_payload(kwargs))

    def get_open_orders(self, **kwargs) -> dict:
        """Current Open Orders (USER_DATA)

        Get all open orders on a symbol.

        GET /api/v3/openOrders

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Query%20Open%20Orders

        params:
            symbol (str, optional)
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.OPEN_ORDERS_URL, params=self.get_payload(kwargs))

    def cancel_open_order(self, **kwargs) -> dict:
        """Cancel Order (TRADE)

        Cancel an active order.

        POST /openApi/spot/v1/trade/cancel

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Cancel%20an%20Order

        params:
            symbol (str)

            orderId (int, optional)

            clientOrderID (str, optional)
        """
        if not kwargs.get('orderId') and not kwargs.get('origClientOrderId'):
            raise ValueError('Param "origClientOrderId" or "orderId" must be sent, but both were empty/null!')
        return self.return_args(method='POST',
                                url=URLS.BASE_URL + URLS.CANCEL_ORDER_URL,
                                params=self.get_payload(kwargs),
                                )

    def cancel_open_orders(self, **kwargs) -> dict:
        """Cancel Orders (TRADE)

        Cancel an active orders.

        POST /openApi/spot/v1/trade/cancelOpenOrders

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Cancel%20orders%20by%20symbol

        params:
            symbol (str, optional)
        """
        return self.return_args(method='POST',
                                url=URLS.BASE_URL + URLS.CANCEL_ORDERS_URL,
                                params=self.get_payload(kwargs),
                                )

    def new_order(self, **kwargs) -> dict:
        """New Market/Limit Order (TRADE)

        Post a new order

        POST /openApi/spot/v1/trade/order

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Create%20an%20Order

        params:
        for market order:

            symbol (str)

            side (Side)

            quantity (float, optional)

            quoteOrderQty (float, optional)

        for limit order:

            symbol (str)

            side (Side)

            price (float)

            quantity (float, optional)

            quoteOrderQty (float, optional)

            timeInForce (str, optional). Default: GTC.
        """
        if not kwargs.get('quantity') and not kwargs.get('quoteOrderQty'):
            raise ValueError('Param "quoteOrderQty" or "quantity" must be sent, but both were empty/null!')
        return self.return_args(method='POST',
                                url=URLS.BASE_URL + URLS.CREATE_ORDER_URL,
                                params=self.get_payload(kwargs),
                                )


# TODO: add newClientOrderId to create order
