from .api import API
from ..core.spot import SpotCore
from ...utils import validate_response
from ..deserialize import spot as deserialize
from ....types import TimeInForce, Side


class Spot(API):
    def get_orders(
        self,
        symbol: str,
        orderId: int = None,
        status: str = None,
        type: str = None,
        startTime: int = None,
        endTime: int = None,
        pageIndex: int = None,
        pageSize: int = None,
    ):
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
        response = validate_response(
            self._query(
                **SpotCore.get_orders(
                    self,
                    symbol=symbol,
                    orderId=orderId,
                    status=status,
                    type=type,
                    startTime=startTime,
                    endTime=endTime,
                    pageIndex=pageIndex,
                    pageSize=pageSize,
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_orders(json_data, response)

    def get_open_order(
        self, symbol: str, orderId: int = None, clientOrderID: str = None
    ):
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
            self._query(
                **SpotCore.get_open_order(
                    self, symbol=symbol, orderId=orderId, clientOrderID=clientOrderID
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_order(json_data, response)

    def get_open_orders(self, symbol: str = None):
        """Current Open Orders (USER_DATA)

        Get all open orders on a symbol.

        GET /api/v3/openOrders

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Query%20Open%20Orders

        params:
            symbol (str, optional).
        """
        response = validate_response(
            self._query(**SpotCore.get_open_orders(self, symbol=symbol))
        )
        json_data = response.json()
        return deserialize.deserialize_orders(json_data, response)

    def cancel_open_order(
        self, symbol: str, orderId: int = None, clientOrderID: str = None
    ):
        """Cancel Order (TRADE)

        Cancel an active order.

        POST /openApi/spot/v1/trade/cancel

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Cancel%20an%20Order

        params:
            symbol (str).

            orderId (int, optional).

            clientOrderID (str, optional).
        """
        response = validate_response(
            self._query(
                **SpotCore.cancel_open_order(
                    self, symbol=symbol, orderId=orderId, clientOrderID=clientOrderID
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_order(json_data, response)

    def cancel_open_orders(self, symbol: str = None):
        """Cancel Orders (TRADE)

        Cancel an active orders.

        POST /openApi/spot/v1/trade/cancelOpenOrders

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Cancel%20orders%20by%20symbol

        params:
            symbol (str, optional).
        """
        response = validate_response(
            self._query(**SpotCore.cancel_open_orders(self, symbol=symbol))
        )
        json_data = response.json()
        return deserialize.deserialize_orders(json_data, response)

    def new_market_order(
        self,
        symbol: str,
        side: Side,
        quantity: float = None,
        quoteOrderQty: float = None,
        newClientOrderId: str = None,
    ):
        """New Market Order (TRADE)

        Post a new order

        POST /openApi/spot/v1/trade/order

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Create%20an%20Order

        params:
            symbol (str).

            side (Side).

            quantity (float, optional).

            quoteOrderQty (float, optional).

            newClientOrderId (str, optional). Only letters, numbers and _,Customized order ID for users, with a limit of characters from 1 to 40. Different orders cannot use the same newClientOrderId,Only supports a query range of 2 hours
        """
        response = validate_response(
            self._query(
                **SpotCore.new_order(
                    self,
                    symbol=symbol,
                    side=side.value,
                    type="MARKET",
                    quantity=quantity,
                    quoteOrderQty=quoteOrderQty,
                    newClientOrderId=newClientOrderId,
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_order(json_data, response)

    def new_limit_order(
        self,
        symbol: str,
        side: Side,
        price: float,
        quantity: float = None,
        quoteOrderQty: float = None,
        timeInForce: TimeInForce = TimeInForce.GTC,
        newClientOrderId: str = None,
    ):
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

            newClientOrderId (str, optional). Only letters, numbers and _,Customized order ID for users, with a limit of characters from 1 to 40. Different orders cannot use the same newClientOrderId,Only supports a query range of 2 hours
        """
        response = validate_response(
            self._query(
                **SpotCore.new_order(
                    self,
                    symbol=symbol,
                    side=side.value,
                    type="LIMIT",
                    quantity=quantity,
                    quoteOrderQty=quoteOrderQty,
                    price=price,
                    timeInForce=timeInForce.value,
                    newClientOrderId=newClientOrderId,
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_order(json_data, response)


class AsyncSpot(API):
    async def get_orders(
        self,
        symbol: str,
        orderId: int = None,
        status: str = None,
        type: str = None,
        startTime: int = None,
        endTime: int = None,
        pageIndex: int = None,
        pageSize: int = None,
    ):
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
        response = validate_response(
            await self._async_query(
                **SpotCore.get_orders(
                    self,
                    symbol=symbol,
                    orderId=orderId,
                    status=status,
                    type=type,
                    startTime=startTime,
                    endTime=endTime,
                    pageIndex=pageIndex,
                    pageSize=pageSize,
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_orders(json_data, response)

    async def get_open_order(
        self, symbol: str, orderId: int = None, clientOrderID: str = None
    ):
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
            await self._async_query(
                **SpotCore.get_open_order(
                    self, symbol=symbol, orderId=orderId, clientOrderID=clientOrderID
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_order(json_data, response)

    async def get_open_orders(self, symbol: str = None):
        """Current Open Orders (USER_DATA)

        Get all open orders on a symbol.

        GET /api/v3/openOrders

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Query%20Open%20Orders

        params:
            symbol (str, optional).
        """
        response = validate_response(
            await self._async_query(**SpotCore.get_open_orders(self, symbol=symbol))
        )
        json_data = response.json
        return deserialize.deserialize_orders(json_data, response)

    async def cancel_open_order(
        self, symbol: str, orderId: int = None, clientOrderID: str = None
    ):
        """Cancel Order (TRADE)

        Cancel an active order.

        POST /openApi/spot/v1/trade/cancel

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Cancel%20an%20Order

        params:
            symbol (str).

            orderId (int, optional).

            clientOrderID (str, optional).
        """
        response = validate_response(
            await self._async_query(
                **SpotCore.cancel_open_order(
                    self, symbol=symbol, orderId=orderId, clientOrderID=clientOrderID
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_order(json_data, response)

    async def cancel_open_orders(self, symbol: str = None):
        """Cancel Orders (TRADE)

        Cancel an active orders.

        POST /openApi/spot/v1/trade/cancelOpenOrders

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Cancel%20orders%20by%20symbol

        params:
            symbol (str, optional).
        """
        response = validate_response(
            await self._async_query(**SpotCore.cancel_open_orders(self, symbol=symbol))
        )
        json_data = response.json
        return deserialize.deserialize_orders(json_data, response)

    async def new_market_order(
        self,
        symbol: str,
        side: Side,
        quantity: float = None,
        quoteOrderQty: float = None,
        newClientOrderId: str = None,
    ):
        """New Market Order (TRADE)

        Post a new order

        POST /openApi/spot/v1/trade/order

        https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Create%20an%20Order

        params:
            symbol (str).

            side (Side).

            quantity (float, optional).

            quoteOrderQty (float, optional).

            newClientOrderId (str, optional). Only letters, numbers and _,Customized order ID for users, with a limit of characters from 1 to 40. Different orders cannot use the same newClientOrderId,Only supports a query range of 2 hours
        """
        response = validate_response(
            await self._async_query(
                **SpotCore.new_order(
                    self,
                    symbol=symbol,
                    side=side.value,
                    type="MARKET",
                    quantity=quantity,
                    quoteOrderQty=quoteOrderQty,
                    newClientOrderId=newClientOrderId,
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_order(json_data, response)

    async def new_limit_order(
        self,
        symbol: str,
        side: Side,
        price: float,
        quantity: float = None,
        quoteOrderQty: float = None,
        timeInForce: TimeInForce = TimeInForce.GTC,
        newClientOrderId: str = None,
    ):
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

           newClientOrderId (str, optional). Only letters, numbers and _,Customized order ID for users, with a limit of characters from 1 to 40. Different orders cannot use the same newClientOrderId,Only supports a query range of 2 hours
        """
        response = validate_response(
            await self._async_query(
                **SpotCore.new_order(
                    self,
                    symbol=symbol,
                    side=side.value,
                    type="LIMIT",
                    quantity=quantity,
                    quoteOrderQty=quoteOrderQty,
                    price=price,
                    timeInForce=timeInForce.value,
                    newClientOrderId=newClientOrderId,
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_order(json_data, response)
