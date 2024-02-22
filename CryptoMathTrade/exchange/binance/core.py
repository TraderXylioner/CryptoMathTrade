from ._urls import URLS
from ..utils import _convert_kwargs_to_dict


class Core:
    # WS Market
    @classmethod
    @_convert_kwargs_to_dict
    def ws_get_depth_args(cls, params: dict) -> dict:
        """Partial Book Depth Streams

        Top bids and asks, Valid are 5, 10, or 20.

        Stream Names: <symbol>@depth<levels> OR <symbol>@depth<levels>@100ms.

        param:
            symbol (str): the trading pair

        Update Speed: 1000ms or 100ms
        """
        return {'method': 'SUBSCRIBE', 'url': URLS.WS_BASE_URL, 'params': f'{params["symbol"]}@depth'}

    @classmethod
    @_convert_kwargs_to_dict
    def ws_get_trades_args(cls, params: dict) -> dict:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.

         Stream Name: <symbol>@trade

         param:
            symbol (str): the trading pair

         Update Speed: Real-time
         """
        return {'method': 'SUBSCRIBE', 'url': URLS.WS_BASE_URL, 'params': f'{params["symbol"]}@trade'}

    # Market
    @classmethod
    @_convert_kwargs_to_dict
    def get_depth_args(cls, params: dict) -> dict:
        """Get orderbook.

        GET /api/v3/depth

        https://binance-docs.github.io/apidocs/spot/en/#order-book

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 100; max 5000. If limit > 5000, then the response will truncate to 5000.
        """
        return {'method': 'GET', 'url': URLS.BASE_URL + URLS.DEPTH_URL, 'params': params}

    @classmethod
    @_convert_kwargs_to_dict
    def get_trades_args(cls, params: dict) -> dict:
        """Recent Trades List
        Get recent trades (up to last 500).

        GET /api/v3/trades

        https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list

        params:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 500; max 1000.
        """
        return {'method': 'GET', 'url': URLS.BASE_URL + URLS.TRADES_URL, 'params': params}

    @classmethod
    @_convert_kwargs_to_dict
    def get_ticker_args(cls, params: dict) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair
            symbols (list, optional): list of trading pairs
        """
        if params.get('symbol') and params.get('symbols'):
            raise ValueError('symbol and symbols cannot be sent together.')  # custom error
        return {'method': 'GET', 'url': URLS.BASE_URL + URLS.TICKER_URL, 'params': params}

    # Spot
    @classmethod
    @_convert_kwargs_to_dict
    def get_orders_args(cls, SpotObj, params: dict) -> dict:
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
        return {'method': 'GET', 'url': URLS.BASE_URL + URLS.GET_ORDERS_URL, 'params': SpotObj.get_payload(params)}

    @classmethod
    @_convert_kwargs_to_dict
    def get_open_order_args(cls, SpotObj, params: dict) -> dict:
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
            raise ValueError('Param "origClientOrderId" or "orderId" must be sent, but both were empty/null!')   # custom error
        return {'method': 'GET', 'url': URLS.BASE_URL + URLS.ORDER_URL, 'params': SpotObj.get_payload(params)}

    @classmethod
    @_convert_kwargs_to_dict
    def get_open_orders_args(cls, SpotObj, params: dict) -> dict:
        """Current Open Orders (USER_DATA)

        Get all open orders on a symbol.

        GET /api/v3/openOrders

        https://binance-docs.github.io/apidocs/spot/en/#current-open-orders-user_data

        params:
            symbol (str, optional)
            recvWindow (int, optional): The value cannot be greater than 60000
        """
        return {'method': 'GET', 'url': URLS.BASE_URL + URLS.OPEN_ORDERS_URL, 'params': SpotObj.get_payload(params)}

    @classmethod
    @_convert_kwargs_to_dict
    def cancel_open_order_args(cls, SpotObj, params: dict) -> dict:
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
        return {'method': 'DELETE', 'url': URLS.BASE_URL + URLS.ORDER_URL, 'params': SpotObj.get_payload(params)}

    @classmethod
    @_convert_kwargs_to_dict
    def cancel_open_orders_args(cls, SpotObj, params: dict) -> dict:
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
        return {'method': 'DELETE', 'url': URLS.BASE_URL + URLS.OPEN_ORDERS_URL, 'params': SpotObj.get_payload(params)}

    @classmethod
    @_convert_kwargs_to_dict
    def new_order_args(cls, SpotObj, params: dict) -> dict:
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
        return {'method': 'POST', 'url': URLS.BASE_URL + URLS.ORDER_URL, 'params': SpotObj.get_payload(params)}

    # Account
    @classmethod
    @_convert_kwargs_to_dict
    def get_deposit_address_args(cls, AccountObj, params: dict) -> dict:
        return {'method': 'GET', 'url': URLS.BASE_URL + URLS.GET_DEPOSIT_ADDRESS, 'params': AccountObj.get_payload(params)}
