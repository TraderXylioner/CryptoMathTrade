from functools import wraps

from CryptoMathTrade.exchange.errors import ResponseError


def validate_data(func):
    @wraps(func)
    def wrapper(data: dict, *args, **kwargs):
        if not data:
            raise ResponseError(data)
        return func(data, *args, **kwargs)

    return wrapper
