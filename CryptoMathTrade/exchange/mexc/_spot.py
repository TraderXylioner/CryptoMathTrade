from ._api import API
from ._deserialization import _deserialize_orders, _deserialize_order
from .core import SpotCore
from .._response import Response
from ...types import Side, TimeInForce, FullOrder
from ..utils import validate_response


class Spot(API):
    def get_orders(self,
                   symbol: str,
                   limit: int = 500,
                   startTime: int = None,
                   endTime: int = None,
                   ) -> Response[list[FullOrder], object]:
        """All Orders (USER_DATA)

        Get all account orders; active, canceled, or filled.

        GET /api/v3/allOrders

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#all-orders

        params:
            symbol (str)

            limit (int, optional): Default 500; max 1000.

            startTime (int, optional)

            endTime (int, optional)
        """
        response = validate_response(self._query(
            **SpotCore.get_orders(self, symbol=symbol, limit=limit, startTime=startTime, endTime=endTime)))
        json_data = response.json()
        return _deserialize_orders(json_data, response)

    def get_open_order(self,
                       symbol: str,
                       orderId: int = None,
                       clientOrderID: str = None,
                       ) -> Response[FullOrder, object]:
        """Query Order (USER_DATA)

        Check an order's status.

        GET /api/v3/order

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#query-order

        params:
            symbol (str)

            orderId (int, optional)

            clientOrderID (str, optional)
        """
        response = validate_response(
            self._query(**SpotCore.get_open_order(self, symbol=symbol, orderId=orderId, clientOrderID=clientOrderID)))
        json_data = response.json()
        return _deserialize_order(json_data, response)

    def get_open_orders(self, symbol: str) -> Response[list[FullOrder], object]:
        """Current Open Orders (USER_DATA)

        Get all open orders on a symbol.

        GET /api/v3/openOrders

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#current-open-orders

        params:
            symbol (str)
        """
        response = validate_response(self._query(**SpotCore.get_open_orders(self, symbol=symbol)))
        json_data = response.json()
        return _deserialize_orders(json_data, response)

    def cancel_open_order(self,
                          symbol: str,
                          orderId: int = None,
                          clientOrderID: str = None,
                          newClientOrderId: str = None,
                          ) -> Response[FullOrder, object]:
        """Cancel Order (TRADE)

        Cancel an active order.

        DELETE /api/v3/order

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#cancel-order

        params:
            symbol (str)

            orderId (int, optional)

            clientOrderID (str, optional)

            newClientOrderId (str, optional)
        """
        response = validate_response(self._query(
            **SpotCore.cancel_open_order(self, symbol=symbol, orderId=orderId, clientOrderID=clientOrderID,
                                         newClientOrderId=newClientOrderId)))
        json_data = response.json()
        return _deserialize_order(json_data, response)

    def cancel_open_orders(self, symbol: str) -> Response[list[FullOrder], object]:
        """Cancel Order (TRADE)

        Cancel an active order.

        DELETE /api/v3/openOrders

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#cancel-all-open-orders-on-a-symbol

        params:
            symbol (str)
        """
        response = validate_response(self._query(**SpotCore.cancel_open_orders(self, symbol=symbol)))
        json_data = response.json()
        return _deserialize_orders(json_data, response)

    def new_market_order(self,
                         symbol: str,
                         side: Side,
                         quantity: float = None,
                         quoteOrderQty: float = None,
                         ) -> Response[FullOrder, object]:
        """New Market Order (TRADE)

        Post a new order

        POST /api/v3/order

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#new-order

        params:
            symbol (str)

            side (str)

            quantity (float, optional)

            quoteOrderQty (float, optional)
        """
        response = validate_response(self._query(
            **SpotCore.new_order(self, symbol=symbol, side=side.value, type="MARKET", quantity=quantity,
                                 quoteOrderQty=quoteOrderQty)))
        json_data = response.json()
        return _deserialize_order(json_data, response)

    def new_limit_order(self,
                        symbol: str,
                        side: Side,
                        price: float,
                        quantity: float,
                        timeInForce: TimeInForce = TimeInForce.GTC,
                        ) -> Response[FullOrder, object]:
        """New Limit Order (TRADE)

        Post a new order

        POST /api/v3/order

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#new-order

        params:
            symbol (str)

            side (str)

            price (float)

            quantity (float)
        """
        response = validate_response(self._query(
            **SpotCore.new_order(self, symbol=symbol, side=side.value, type="LIMIT", price=price, quantity=quantity,
                                 timeInForce=timeInForce.value)))
        json_data = response.json()
        return _deserialize_order(json_data, response)
