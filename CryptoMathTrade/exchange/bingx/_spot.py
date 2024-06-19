from ._api import API
from .core import SpotCore
from CryptoMathTrade.types import Side, TimeInForce
from .._response import Response
from ..utils import validate_response
from ._serialization import _serialize_order, _serialize_orders


class Spot(API):
    def get_orders(self,
                   symbol: str,
                   orderId: int = None,
                   startTime: int = None,
                   endTime: int = None,
                   pageIndex: int = None,
                   pageSize: int = None,
                   status: str = None,
                   type: str = None,
                   ) -> Response:
        """All Orders (USER_DATA)

        Get all account orders; active, canceled, or filled.

        GET /openApi/spot/v1/trade/historyOrders

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Query%20Order%20History

        params:
            symbol (str).

            orderId (int, optional).

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.

            pageIndex: (int, optional), Default: 1.

            pageSize: (int, optional), Default: 100, Max 100.

            status: (str, optional) FILLED / CANCELED / FAILED.

            type: (str, optional) MARKET / LIMIT / TAKE_STOP_LIMIT / TAKE_STOP_MARKET / TRIGGER_LIMIT / TRIGGER_MARKET.
        """
        response = validate_response(self._query(**SpotCore.get_orders(self,
                                                                       symbol=symbol,
                                                                       orderId=orderId,
                                                                       startTime=startTime,
                                                                       endTime=endTime,
                                                                       pageIndex=pageIndex,
                                                                       pageSize=pageSize,
                                                                       status=status,
                                                                       type=type,
                                                                       )))
        json_data = response.json()
        return _serialize_orders(json_data, response)

    def get_open_order(self, symbol: str, orderId: int = None, clientOrderID: str = None) -> Response:
        """Query Order (USER_DATA)

        Check an order's status.

        GET /openApi/spot/v1/trade/query

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Query%20Orders

        params:
            symbol (str).

            orderId (int, optional).

            clientOrderID (str, optional).
        """
        response = validate_response(
            self._query(**SpotCore.get_open_order(self, symbol=symbol, orderId=orderId, clientOrderID=clientOrderID)))
        json_data = response.json()
        return _serialize_order(json_data, response)

    def get_open_orders(self, symbol: str = None) -> Response:
        """Current Open Orders (USER_DATA)

        Get all open orders on a symbol.

        GET /api/v3/openOrders

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Query%20Open%20Orders

        params:
            symbol (str, optional).
        """
        response = validate_response(self._query(**SpotCore.get_open_orders(self, symbol=symbol)))
        json_data = response.json()
        return _serialize_orders(json_data, response)

    def cancel_open_order(self, symbol: str, orderId: int = None, clientOrderID: str = None) -> Response:
        """Cancel Order (TRADE)

        Cancel an active order.

        POST /openApi/spot/v1/trade/cancel

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Cancel%20an%20Order

        params:
            symbol (str).

            orderId (int, optional).

            clientOrderID (str, optional).
        """
        response = validate_response(self._query(
            **SpotCore.cancel_open_order(self, symbol=symbol, orderId=orderId, clientOrderID=clientOrderID)))
        json_data = response.json()
        return _serialize_order(json_data, response)

    def cancel_open_orders(self, symbol: str = None) -> Response:
        """Cancel Orders (TRADE)

        Cancel an active orders.

        POST /openApi/spot/v1/trade/cancelOpenOrders

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Cancel%20orders%20by%20symbol

        params:
            symbol (str, optional).
        """
        response = validate_response(self._query(**SpotCore.cancel_open_orders(self, symbol=symbol)))
        json_data = response.json()
        return _serialize_orders(json_data, response)

    def new_market_order(self,
                         symbol: str,
                         side: Side,
                         quantity: float = None,
                         quoteOrderQty: float = None,
                         ) -> Response:
        """New Market Order (TRADE)

        Post a new order

        POST /openApi/spot/v1/trade/order

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Create%20an%20Order

        params:
            symbol (str).

            side (Side).

            quantity (float, optional).

            quoteOrderQty (float, optional).
        """
        response = validate_response(self._query(**SpotCore.new_order(self,
                                                                      symbol=symbol,
                                                                      side=side.value,
                                                                      type='MARKET',
                                                                      quantity=quantity,
                                                                      quoteOrderQty=quoteOrderQty,
                                                                      )))
        json_data = response.json()
        return _serialize_order(json_data, response)

    def new_limit_order(self,
                        symbol: str,
                        side: Side,
                        price: float,
                        quantity: float = None,
                        quoteOrderQty: float = None,
                        timeInForce: TimeInForce = TimeInForce.GTC,
                        ) -> Response:
        """New Limit Order (TRADE)

        Post a new order

        POST /openApi/spot/v1/trade/order

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Create%20an%20Order

        params:
            symbol (str).

            side (Side).

            price (float).

            quantity (float, optional).

            quoteOrderQty (float, optional).

            timeInForce (str, optional). Default: GTC.
        """
        response = validate_response(self._query(**SpotCore.new_order(self,
                                                                      symbol=symbol,
                                                                      side=side.value,
                                                                      type='LIMIT',
                                                                      quantity=quantity,
                                                                      quoteOrderQty=quoteOrderQty,
                                                                      price=price,
                                                                      timeInForce=timeInForce.value,
                                                                      )))
        json_data = response.json()
        return _serialize_order(json_data, response)
