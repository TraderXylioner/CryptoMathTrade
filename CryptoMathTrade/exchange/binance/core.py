from .urls import BASE_URL, DEPTH_URL, TRADES_URL, TICKER_URL, GET_ORDERS_URL, OPEN_ORDERS_URL, ORDER_URL, \
    GET_DEPOSIT_ADDRESS, WS_BASE_URL
from CryptoMathTrade.exchange.utils import convert_kwargs_to_dict


'''need add check required args'''


# WS Market
@convert_kwargs_to_dict
def ws_get_depth_args(params: dict) -> dict:
    return {'method': 'SUBSCRIBE', 'url': WS_BASE_URL, 'params': f'{params["symbol"]}@depth'}


@convert_kwargs_to_dict
def ws_get_trades_args(params: dict) -> dict:
    return {'method': 'SUBSCRIBE', 'url': WS_BASE_URL, 'params': f'{params["symbol"]}@trade'}


# Market
@convert_kwargs_to_dict
def get_depth_args(params: dict) -> dict:
    return {'method': 'GET', 'url': BASE_URL + DEPTH_URL, 'params': params}


@convert_kwargs_to_dict
def get_trades_args(params: dict) -> dict:
    return {'method': 'GET', 'url': BASE_URL + TRADES_URL, 'params': params}


@convert_kwargs_to_dict
def get_price_args(params: dict) -> dict:
    return {'method': 'GET', 'url': BASE_URL + PRICE_URL, 'params': params}


@convert_kwargs_to_dict
def get_ticker_args(params: dict) -> dict:
    if params.get('symbol') and params.get('symbols'):
        raise ValueError('symbol and symbols cannot be sent together.')
    return {'method': 'GET', 'url': BASE_URL + TICKER_URL, 'params': params}


# Spot
@convert_kwargs_to_dict
def get_orders_args(SpotObj, params: dict) -> dict:
    return {'method': 'GET', 'url': BASE_URL + GET_ORDERS_URL, 'params': SpotObj.get_payload(params)}


@convert_kwargs_to_dict
def get_open_order_args(SpotObj, params: dict) -> dict:
    if not params.get('orderId') and not params.get('origClientOrderId'):
        raise ValueError('Param "origClientOrderId" or "orderId" must be sent, but both were empty/null!')
    return {'method': 'GET', 'url': BASE_URL + ORDER_URL, 'params': SpotObj.get_payload(params)}


@convert_kwargs_to_dict
def get_open_orders_args(SpotObj, params: dict) -> dict:
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
