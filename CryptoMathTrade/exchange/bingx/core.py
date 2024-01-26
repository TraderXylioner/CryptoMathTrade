from ._urls import URLS
from ..utils import _convert_kwargs_to_dict, get_timestamp


# WS Market
@_convert_kwargs_to_dict
def ws_get_depth_args(params: dict) -> dict:
    return {'method': 'sub', 'url': URLS.WS_BASE_URL, 'params': f'{params["symbol"]}@depth'}


@_convert_kwargs_to_dict
def ws_get_trades_args(params: dict) -> dict:
    return {'method': 'sub', 'url': URLS.WS_BASE_URL, 'params': f'{params["symbol"]}@trade'}


# Market
@_convert_kwargs_to_dict
def get_depth_args(params: dict) -> dict:
    return {'method': 'GET', 'url': URLS.BASE_URL + URLS.DEPTH_URL, 'params': params}


@_convert_kwargs_to_dict
def get_trades_args(params: dict) -> dict:
    return {'method': 'GET', 'url': URLS.BASE_URL + URLS.TRADES_URL, 'params': params}


@_convert_kwargs_to_dict
def get_ticker_args(params: dict) -> dict:
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
