from functools import wraps

from ...errors import ResponseError


def validate_data(func):
    @wraps(func)
    def wrapper(data: dict, *args, **kwargs):
        if not data.get("data"):
            raise ResponseError(data)
        return func(data, *args, **kwargs)

    return wrapper
