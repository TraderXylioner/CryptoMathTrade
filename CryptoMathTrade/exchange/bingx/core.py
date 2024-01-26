from ._urls import URLS
from ..utils import _convert_kwargs_to_dict, get_timestamp


# WS Market
@_convert_kwargs_to_dict
def ws_get_depth_args(params: dict) -> dict:
    """Partial Book Depth Streams

    Top bids and asks.

    Stream Names: <symbol>@depth<levels>.

    param:
        symbol (str): the trading pair
    """
    return {'method': 'sub', 'url': URLS.WS_BASE_URL, 'params': f'{params["symbol"]}@depth'}


@_convert_kwargs_to_dict
def ws_get_trades_args(params: dict) -> dict:
    """Trade Streams

     The Trade Streams push raw trade information; each trade has a unique buyer and seller.

     Stream Name: <symbol>@trade

     param:
        symbol (str): the trading pair

     Update Speed: Real-time
     """
    return {'method': 'sub', 'url': URLS.WS_BASE_URL, 'params': f'{params["symbol"]}@trade'}


# Market
@_convert_kwargs_to_dict
def get_depth_args(params: dict) -> dict:
    """Get orderbook.

    GET /openApi/spot/v1/market/depth

    https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20depth%20information

    param:
        symbol (str): the trading pair
        limit (int, optional): limit the results. Default 100; max 1000. If limit > 1000, then the response will truncate to 1000
        recvWindow (int, optional).
    """
    params['limit'] = min(int(params.get('limit', 100)), 1000)
    return {'method': 'GET', 'url': URLS.BASE_URL + URLS.DEPTH_URL, 'params': params}


@_convert_kwargs_to_dict
def get_trades_args(params: dict) -> dict:
    """Recent Trades List
    Get recent trades (up to last 100).

    GET /openApi/spot/v1/market/trades

    https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20transaction%20records

    params:
        symbol (str): the trading pair
        limit (int, optional): limit the results. Default 100; max 100
        recvWindow (int, optional).
    """
    return {'method': 'GET', 'url': URLS.BASE_URL + URLS.TRADES_URL, 'params': params}


@_convert_kwargs_to_dict
def get_ticker_args(params: dict) -> dict:
    """24hr Ticker Price Change Statistics

    GET /openApi/spot/v1/ticker/24hr

    https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#24-hour%20price%20changes

    params:
        symbol (str, optional): the trading pair.
    """
    params['timestamp'] = get_timestamp()
    return {'method': 'GET', 'url': URLS.BASE_URL + URLS.TICKER_URL, 'params': params}


# Spot
@_convert_kwargs_to_dict
def get_orders_args(SpotObj, params):
    return {'method': 'GET', 'url': URLS.BASE_URL + URLS.GET_ORDERS_URL, 'params': SpotObj.get_payload(params)}
#
#
# @convert_kwargs_to_dict
# def get_open_order_args(SpotObj, params):
#     if not params.get('orderId') and not params.get('origClientOrderId'):
#         raise ValueError('Param "origClientOrderId" or "orderId" must be sent, but both were empty/null!')
#     return {'method': 'GET', 'url': BASE_URL + ORDER_URL, 'params': SpotObj.get_payload(params)}
#
#
# @convert_kwargs_to_dict
# def get_open_orders_args(SpotObj, params):
#     return {'method': 'GET', 'url': BASE_URL + OPEN_ORDERS_URL, 'params': SpotObj.get_payload(params)}
#
#
# @convert_kwargs_to_dict
# def delete_open_orders_args(SpotObj, params):
#     return {'method': 'DELETE', 'url': BASE_URL + OPEN_ORDERS_URL, 'params': SpotObj.get_payload(params)}
#
#
# @convert_kwargs_to_dict
# def new_order_args(SpotObj, params):
#     return {'method': 'POST', 'url': BASE_URL + ORDER_URL, 'params': SpotObj.get_payload(params)}
#
#
# # Account
# @convert_kwargs_to_dict
# def get_deposit_address_args(AccountObj, params):
#     return {'method': 'GET', 'url': BASE_URL + GET_DEPOSIT_ADDRESS, 'params': AccountObj.get_payload(params)}
