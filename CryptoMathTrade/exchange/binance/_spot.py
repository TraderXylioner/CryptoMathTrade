from ._api import API
from .core import Core
from CryptoMathTrade.types import Side, TimeInForce


class Spot(API):
    def get_orders(self,
                   symbol: str,
                   orderId: int | None = None,
                   startTime: int | None = None,
                   endTime: int | None = None,
                   limit: int | None = None,
                   recvWindow: int | None = None,
                   ):
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
        return self._query(
            **Core.get_orders_args(self, symbol=symbol, orderId=orderId, startTime=startTime, endTime=endTime,
                                   limit=limit,
                                   recvWindow=recvWindow))

    def get_open_order(self,
                       symbol: str,
                       orderId: int | None = None,
                       origClientOrderId: str | None = None,
                       recvWindow: int | None = None,
                       ):
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
        return self._query(
            **Core.get_open_order_args(self, symbol=symbol, orderId=orderId, origClientOrderId=origClientOrderId,
                                       recvWindow=recvWindow))

    def get_open_orders(self,
                        symbol: str | None = None,
                        recvWindow: int | None = None,
                        ):
        """Current Open Orders (USER_DATA)

        Get all open orders on a symbol.

        GET /api/v3/openOrders

        https://binance-docs.github.io/apidocs/spot/en/#current-open-orders-user_data

        params:
            symbol (str, optional)
            recvWindow (int, optional): The value cannot be greater than 60000
        """
        return self._query(**Core.get_open_orders_args(self, symbol=symbol, recvWindow=recvWindow))

    def cancel_open_order(self,
                          symbol: str,
                          orderId: int | None = None,
                          origClientOrderId: str | None = None,
                          newClientOrderId: str | None = None,
                          recvWindow: int | None = None,
                          ):
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
        return self._query(
            **Core.cancel_open_order_args(self, symbol=symbol, orderId=orderId, origClientOrderId=origClientOrderId,
                                          newClientOrderId=newClientOrderId, recvWindow=recvWindow))

    def cancel_open_orders(self,
                           symbol: str,
                           recvWindow: int | None = None,
                           ):
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
        return self._query(**Core.cancel_open_orders_args(self, symbol=symbol, recvWindow=recvWindow))

    def new_market_order(self,
                         symbol: str,
                         side: Side | str,
                         quantity: float | None = None,
                         quoteOrderQty: float | None = None,
                         ):
        """New Market Order (TRADE)

        Post a new order

        POST /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#new-order-trade

        params:
            symbol (str)
            side (str)
            quantity (float, optional)
            quoteOrderQty (float, optional)
        """
        return self._query(**Core.new_order_args(self, symbol=symbol, side=side, type='MARKET', quantity=quantity,
                                                 quoteOrderQty=quoteOrderQty))

    def new_limit_order(self,
                        symbol: str,
                        side: Side | str,
                        timeInForce: TimeInForce | str,
                        quantity: float,
                        price: float,
                        ):
        """New Limit Order (TRADE)

        Post a new order

        POST /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#new-order-trade

        params:
            symbol (str)
            side (str)
            timeInForce (str, optional)
            quantity (float, optional)
            price (float, optional)
        """
        return self._query(
            **Core.new_order_args(self, symbol=symbol, side=side, type='LIMIT', timeInForce=timeInForce,
                                  quantity=quantity,
                                  price=price))
