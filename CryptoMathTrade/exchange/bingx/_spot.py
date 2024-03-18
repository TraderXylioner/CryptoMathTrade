from ._api import API
from .core import SpotCore
from CryptoMathTrade.types import Side, TimeInForce
from .._response import Response
from ..utils import validate_response


class Spot(API):
    def get_orders(self,
                   symbol: str,
                   orderId: int | None = None,
                   startTime: int | None = None,
                   endTime: int | None = None,
                   pageIndex: int | None = None,
                   pageSize: int | None = None,
                   status: str | None = None,
                   type: str | None = None,
                   recvWindow: int | None = None,
                   ) -> Response:
        """All Orders (USER_DATA)

        Get all account orders; active, canceled, or filled.

        GET /openApi/spot/v1/trade/historyOrders

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Query%20Order%20History

        params:
            symbol (str)

            orderId (int, optional)

            startTime (int, optional)

            endTime (int, optional)

            pageIndex: (int, optional)

            pageSize: (int, optional)

            status: (str, optional)

            type: (str, optional)

            recvWindow (int, optional): The value cannot be greater than 60000
        """
        response = validate_response(self._query(
            **SpotCore(headers=self.headers).get_orders_args(self,
                                                             symbol=symbol,
                                                             orderId=orderId,
                                                             startTime=startTime,
                                                             endTime=endTime,
                                                             pageIndex=pageIndex,
                                                             pageSize=pageSize,
                                                             status=status,
                                                             type=type,
                                                             recvWindow=recvWindow,
                                                             )))
        json_data = response.json()
        return Response(data=json_data,
                        response_object=response,
                        )

    def get_open_order(self,
                       symbol: str,
                       orderId: int | None = None,
                       clientOrderID: str | None = None,
                       recvWindow: int | None = None,
                       ):
        """Query Order (USER_DATA)

        Check an order's status.

        GET /openApi/spot/v1/trade/query

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Query%20Orders

        params:
            symbol (str)

            orderId (int, optional)

            clientOrderID (str, optional)

            recvWindow (int, optional): The value cannot be greater than 60000
        """
        response = validate_response(self._query(**SpotCore(headers=self.headers).get_open_order_args(self,
                                                                                                      symbol=symbol,
                                                                                                      orderId=orderId,
                                                                                                      clientOrderID=clientOrderID,
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

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Query%20Open%20Orders

        params:
            symbol (str, optional)

            recvWindow (int, optional): The value cannot be greater than 60000
        """
        response = validate_response(self._query(
            **SpotCore(headers=self.headers).get_open_orders_args(self,
                                                                  symbol=symbol,
                                                                  recvWindow=recvWindow,
                                                                  )))
        json_data = response.json()['data']
        return Response(data=json_data,
                        response_object=response,
                        )

    def cancel_open_order(self,
                          symbol: str,
                          orderId: int | None = None,
                          clientOrderID: str | None = None,
                          recvWindow: int | None = None,
                          ):
        """Cancel Order (TRADE)

        Cancel an active order.

        POST /openApi/spot/v1/trade/cancel

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Cancel%20an%20Order

        params:
            symbol (str)

            orderId (int, optional)

            clientOrderID (str, optional)

            recvWindow (int, optional): The value cannot be greater than 60000
        """
        response = validate_response(self._query(**SpotCore(headers=self.headers).cancel_open_order_args(self,
                                                                                                         symbol=symbol,
                                                                                                         orderId=orderId,
                                                                                                         clientOrderID=clientOrderID,
                                                                                                         recvWindow=recvWindow,
                                                                                                         )))
        json_data = response.json()
        return Response(data=json_data,
                        response_object=response,
                        )

    def cancel_open_orders(self,
                           symbol: str | None = None,
                           recvWindow: int | None = None,
                           ):
        """Cancel Orders (TRADE)

        Cancel an active orders.

        POST /openApi/spot/v1/trade/cancelOpenOrders

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Cancel%20orders%20by%20symbol

        params:
            symbol (str, optional)

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

        POST /openApi/spot/v1/trade/order

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Create%20an%20Order

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

        POST /openApi/spot/v1/trade/order

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Create%20an%20Order

        params:
            symbol (str)

            side (str)

            quantity (float)

            price (float)

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
