from ._api import API
from .core import SpotCore
from .._response import Response
from ...types import Side, TimeInForce
from ..utils import validate_response


class Spot(API):
    def get_orders(self,
                   symbol: str,
                   limit: int = 500,
                   orderId: int | None = None,
                   startTime: int | None = None,
                   endTime: int | None = None,
                   recvWindow: int | None = None,
                   ) -> Response:
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

            recvWindow (int, optional): The value cannot be greater than 60000
        """
        response = validate_response(self._query(
            **SpotCore(headers=self.headers).get_orders_args(self,
                                                             symbol=symbol,
                                                             limit=limit,
                                                             orderId=orderId,
                                                             startTime=startTime,
                                                             endTime=endTime,
                                                             recvWindow=recvWindow,
                                                             )))
        json_data = response.json()
        return Response(data=json_data,
                        response_object=response,
                        )

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
        response = validate_response(self._query(**SpotCore(headers=self.headers).get_open_order_args(self,
                                                                                                      symbol=symbol,
                                                                                                      orderId=orderId,
                                                                                                      origClientOrderId=origClientOrderId,
                                                                                                      recvWindow=recvWindow,
                                                                                                      )))
        json_data = response.json()
        return Response(data=json_data,
                        response_object=response,
                        )

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
        response = validate_response(self._query(
            **SpotCore(headers=self.headers).get_open_orders_args(self,
                                                                  symbol=symbol,
                                                                  recvWindow=recvWindow,
                                                                  )))
        json_data = response.json()
        return Response(data=json_data,
                        response_object=response,
                        )

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
        response = validate_response(self._query(**SpotCore(headers=self.headers).cancel_open_order_args(self,
                                                                                                         symbol=symbol,
                                                                                                         orderId=orderId,
                                                                                                         origClientOrderId=origClientOrderId,
                                                                                                         newClientOrderId=newClientOrderId,
                                                                                                         recvWindow=recvWindow,
                                                                                                         )))
        json_data = response.json()
        return Response(data=json_data,
                        response_object=response,
                        )

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

            recvWindow (int, optional): The value cannot be greater than 60000
        """
        response = validate_response(self._query(
            **SpotCore(headers=self.headers).cancel_open_orders_args(self, symbol=symbol, recvWindow=recvWindow)))
        json_data = response.json()
        return Response(data=json_data,
                        response_object=response,
                        )

    def new_market_order(self,
                         symbol: str,
                         side: Side,
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
        response = validate_response(self._query(
            **SpotCore(headers=self.headers).new_order_args(self,
                                                            symbol=symbol,
                                                            side=side.value,
                                                            type='MARKET',
                                                            quantity=quantity,
                                                            quoteOrderQty=quoteOrderQty,
                                                            )))
        json_data = response.json()
        return Response(data=json_data,
                        response_object=response,
                        )

    def new_limit_order(self,
                        symbol: str,
                        side: Side,
                        quantity: float,
                        price: float,
                        timeInForce: TimeInForce = TimeInForce.GTC,
                        ):
        """New Limit Order (TRADE)

        Post a new order

        POST /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#new-order-trade

        params:
            symbol (str)

            side (str)

            quantity (float, optional)

            price (float, optional)

            timeInForce (str, optional)
        """
        response = validate_response(self._query(**SpotCore(headers=self.headers).new_order_args(self,
                                                                                                 symbol=symbol,
                                                                                                 side=side.value,
                                                                                                 type='LIMIT',
                                                                                                 quantity=quantity,
                                                                                                 price=price,
                                                                                                 timeInForce=timeInForce.value,
                                                                                                 )))
        json_data = response.json()
        return Response(data=json_data,
                        response_object=response,
                        )
