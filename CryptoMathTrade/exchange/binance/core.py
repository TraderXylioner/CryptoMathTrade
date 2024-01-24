from .urls import BASE_URL, DEPTH_URL, TRADES_URL, TICKER_URL, GET_ORDERS_URL, OPEN_ORDERS_URL, ORDER_URL, \
    GET_DEPOSIT_ADDRESS, WS_BASE_URL
from ..utils import convert_kwargs_to_dict


# WS Market
@convert_kwargs_to_dict
def ws_get_depth_args(params: dict) -> dict:
    """Partial Book Depth Streams

    Top bids and asks, Valid are 5, 10, or 20.

    Stream Names: <symbol>@depth<levels> OR <symbol>@depth<levels>@100ms.

    param:
        symbol (str): the trading pair

    Update Speed: 1000ms or 100ms
    """
    return {'method': 'SUBSCRIBE', 'url': WS_BASE_URL, 'params': f'{params["symbol"]}@depth'}


@convert_kwargs_to_dict
def ws_get_trades_args(params: dict) -> dict:
    """Trade Streams

     The Trade Streams push raw trade information; each trade has a unique buyer and seller.

     Stream Name: <symbol>@trade

     param:
        symbol (str): the trading pair

     Update Speed: Real-time
     """
    return {'method': 'SUBSCRIBE', 'url': WS_BASE_URL, 'params': f'{params["symbol"]}@trade'}


# Market
@convert_kwargs_to_dict
def get_depth_args(params: dict) -> dict:
    """Get orderbook.

    GET /api/v3/depth

    https://binance-docs.github.io/apidocs/spot/en/#order-book

    param:
        symbol (str): the trading pair
        limit (int, optional): limit the results. Default 100; max 5000. If limit > 5000, then the response will truncate to 5000.
    """
    return {'method': 'GET', 'url': BASE_URL + DEPTH_URL, 'params': params}


@convert_kwargs_to_dict
def get_trades_args(params: dict) -> dict:
    """Recent Trades List
    Get recent trades (up to last 500).

    GET /api/v3/trades

    https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list

    params:
        symbol (str): the trading pair
        limit (int, optional): limit the results. Default 500; max 1000.
    """
    return {'method': 'GET', 'url': BASE_URL + TRADES_URL, 'params': params}


@convert_kwargs_to_dict
def get_ticker_args(params: dict) -> dict:
    """24hr Ticker Price Change Statistics

    GET /api/v3/ticker/24hr

    https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

    params:
        symbol (str, optional): the trading pair
        symbols (list, optional): list of trading pairs
    """
    if params.get('symbol') and params.get('symbols'):
        raise ValueError('symbol and symbols cannot be sent together.')
    return {'method': 'GET', 'url': BASE_URL + TICKER_URL, 'params': params}


# Spot
@convert_kwargs_to_dict
def get_orders_args(SpotObj, params: dict) -> dict:
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
    return {'method': 'GET', 'url': BASE_URL + GET_ORDERS_URL, 'params': SpotObj.get_payload(params)}


@convert_kwargs_to_dict
def get_open_order_args(SpotObj, params: dict) -> dict:
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
        raise ValueError('Param "origClientOrderId" or "orderId" must be sent, but both were empty/null!')
    return {'method': 'GET', 'url': BASE_URL + ORDER_URL, 'params': SpotObj.get_payload(params)}


@convert_kwargs_to_dict
def get_open_orders_args(SpotObj, params: dict) -> dict:
    """Current Open Orders (USER_DATA)

    Get all open orders on a symbol.

    GET /api/v3/openOrders

    https://binance-docs.github.io/apidocs/spot/en/#current-open-orders-user_data

    params:
        symbol (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    return {'method': 'GET', 'url': BASE_URL + OPEN_ORDERS_URL, 'params': SpotObj.get_payload(params)}


@convert_kwargs_to_dict
def cancel_open_orders_args(SpotObj, params: dict) -> dict:
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
    return {'method': 'DELETE', 'url': BASE_URL + OPEN_ORDERS_URL, 'params': SpotObj.get_payload(params)}


@convert_kwargs_to_dict
def new_order_args(SpotObj, params: dict) -> dict:
    return {'method': 'POST', 'url': BASE_URL + ORDER_URL, 'params': SpotObj.get_payload(params)}


# Account
@convert_kwargs_to_dict
def get_deposit_address_args(AccountObj, params: dict) -> dict:
    return {'method': 'GET', 'url': BASE_URL + GET_DEPOSIT_ADDRESS, 'params': AccountObj.get_payload(params)}
