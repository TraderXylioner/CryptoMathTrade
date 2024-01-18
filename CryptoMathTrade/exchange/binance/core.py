from CryptoMathTrade.exchange.binance.setting import BASE_URL, DEPTH_URL, TRADES_URL, PRICE_URL, TICKER_URL, \
    GET_ORDERS_URL, OPEN_ORDERS_URL, ORDER_URL, GET_DEPOSIT_ADDRESS
from CryptoMathTrade.exchange.utils import convert_kwargs_to_dict


'''need add check required args'''


# Market
@convert_kwargs_to_dict
def get_depth_args(params):
    return {'method': 'GET', 'url': BASE_URL + DEPTH_URL, 'params': params}


@convert_kwargs_to_dict
def get_trades_args(params):
    return {'method': 'GET', 'url': BASE_URL + TRADES_URL, 'params': params}


@convert_kwargs_to_dict
def get_price_args(params):
    return {'method': 'GET', 'url': BASE_URL + PRICE_URL, 'params': params}


@convert_kwargs_to_dict
def get_ticker_args(params):
    if params.get('symbol') and params.get('symbols'):
        raise ValueError('symbol and symbols cannot be sent together.')
    return {'method': 'GET', 'url': BASE_URL + TICKER_URL, 'params': params}


# Spot
@convert_kwargs_to_dict
def get_orders_args(SpotObj, params):
    return {'method': 'GET', 'url': BASE_URL + GET_ORDERS_URL, 'params': SpotObj.get_payload(params)}


@convert_kwargs_to_dict
def get_open_order_args(SpotObj, params):
    if not params.get('orderId') and not params.get('origClientOrderId'):
        raise ValueError('Param "origClientOrderId" or "orderId" must be sent, but both were empty/null!')
    return {'method': 'GET', 'url': BASE_URL + ORDER_URL, 'params': SpotObj.get_payload(params)}


@convert_kwargs_to_dict
def get_open_orders_args(SpotObj, params):
    return {'method': 'GET', 'url': BASE_URL + OPEN_ORDERS_URL, 'params': SpotObj.get_payload(params)}


@convert_kwargs_to_dict
def delete_open_orders_args(SpotObj, params):
    return {'method': 'DELETE', 'url': BASE_URL + OPEN_ORDERS_URL, 'params': SpotObj.get_payload(params)}


@convert_kwargs_to_dict
def new_order_args(SpotObj, params):
    return {'method': 'POST', 'url': BASE_URL + ORDER_URL, 'params': SpotObj.get_payload(params)}


# Account
@convert_kwargs_to_dict
def get_deposit_address_args(AccountObj, params):
    return {'method': 'GET', 'url': BASE_URL + GET_DEPOSIT_ADDRESS, 'params': AccountObj.get_payload(params)}
