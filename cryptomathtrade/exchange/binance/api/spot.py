from .api import API
from ..deserialize import spot as deserialize
from ..core.spot import SpotCore
from ...utils import validate_response
from ....types import Side, TimeInForce


class Spot(API):
    def get_orders(
        self,
        symbol: str,
        limit: int = 500,
        orderId: int = None,
        startTime: int = None,
        endTime: int = None,
    ):
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
        response = validate_response(
            self._query(
                **SpotCore.get_orders(
                    self,
                    symbol=symbol,
                    limit=limit,
                    orderId=orderId,
                    startTime=startTime,
                    endTime=endTime,
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_orders(json_data, response)

    def get_open_order(
        self,
        symbol: str,
        orderId: int = None,
        clientOrderID: str = None,
    ):
        """Query Order (USER_DATA)

        Check an order's status.

        GET /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#query-order-user_data

        params:
            symbol (str)

            orderId (int, optional)

            clientOrderID (str, optional)
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

        https://binance-docs.github.io/apidocs/spot/en/#current-open-orders-user_data

        params:
            symbol (str, optional)
        """
        response = validate_response(
            self._query(**SpotCore.get_open_orders(self, symbol=symbol))
        )
        json_data = response.json()
        return deserialize.deserialize_orders(json_data, response)

    def cancel_open_order(
        self,
        symbol: str,
        orderId: int = None,
        clientOrderID: str = None,
        newClientOrderId: str = None,
    ):
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
        response = validate_response(
            self._query(
                **SpotCore.cancel_open_order(
                    self,
                    symbol=symbol,
                    orderId=orderId,
                    clientOrderID=clientOrderID,
                    newClientOrderId=newClientOrderId,
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_order(json_data, response)

    def cancel_open_orders(self, symbol: str):
        """Cancel Order (TRADE)

        Cancel an active order.

        DELETE /api/v3/openOrders

        https://binance-docs.github.io/apidocs/spot/en/#cancel-all-open-orders-on-a-symbol-trade

        params:
            symbol (str)
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
        response = validate_response(
            self._query(
                **SpotCore.new_order(
                    self,
                    symbol=symbol,
                    side=side.value,
                    type="MARKET",
                    quantity=quantity,
                    quoteOrderQty=quoteOrderQty,
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
        quantity: float,
        timeInForce: TimeInForce = TimeInForce.GTC,
    ):
        """New Limit Order (TRADE)

        Post a new order

        POST /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#new-order-trade

        params:
            symbol (str)

            side (str)

            price (float)

            quantity (float)

            timeInForce (str, optional)
        """
        response = validate_response(
            self._query(
                **SpotCore.new_order(
                    self,
                    symbol=symbol,
                    side=side.value,
                    type="LIMIT",
                    price=price,
                    quantity=quantity,
                    timeInForce=timeInForce.value,
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_order(json_data, response)


class AsyncSpot(API):
    async def get_orders(
        self,
        symbol: str,
        limit: int = 500,
        orderId: int = None,
        startTime: int = None,
        endTime: int = None,
    ):
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
        response = validate_response(
            await self._async_query(
                **SpotCore.get_orders(
                    self,
                    symbol=symbol,
                    limit=limit,
                    orderId=orderId,
                    startTime=startTime,
                    endTime=endTime,
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_orders(json_data, response)

    async def get_open_order(
        self,
        symbol: str,
        orderId: int = None,
        clientOrderID: str = None,
    ):
        """Query Order (USER_DATA)

        Check an order's status.

        GET /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#query-order-user_data

        params:
            symbol (str)

            orderId (int, optional)

            clientOrderID (str, optional)
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

        https://binance-docs.github.io/apidocs/spot/en/#current-open-orders-user_data

        params:
            symbol (str, optional)
        """
        response = validate_response(
            await self._async_query(**SpotCore.get_open_orders(self, symbol=symbol))
        )
        json_data = response.json
        return deserialize.deserialize_orders(json_data, response)

    async def cancel_open_order(
        self,
        symbol: str,
        orderId: int = None,
        clientOrderID: str = None,
        newClientOrderId: str = None,
    ):
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
        response = validate_response(
            await self._async_query(
                **SpotCore.cancel_open_order(
                    self,
                    symbol=symbol,
                    orderId=orderId,
                    clientOrderID=clientOrderID,
                    newClientOrderId=newClientOrderId,
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_order(json_data, response)

    async def cancel_open_orders(self, symbol: str):
        """Cancel Order (TRADE)

        Cancel an active order.

        DELETE /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#cancel-order-trade

        params:
            symbol (str)
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
        response = validate_response(
            await self._async_query(
                **SpotCore.new_order(
                    self,
                    symbol=symbol,
                    side=side.value,
                    type="MARKET",
                    quantity=quantity,
                    quoteOrderQty=quoteOrderQty,
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
        quantity: float,
        timeInForce: TimeInForce = TimeInForce.GTC,
    ):
        """New Limit Order (TRADE)

        Post a new order

        POST /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#new-order-trade

        params:
            symbol (str)

            side (str)

            price (float)

            quantity (float)

            timeInForce (str, optional)
        """
        response = validate_response(
            await self._async_query(
                **SpotCore.new_order(
                    self,
                    symbol=symbol,
                    side=side.value,
                    type="LIMIT",
                    price=price,
                    quantity=quantity,
                    timeInForce=timeInForce.value,
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_order(json_data, response)
