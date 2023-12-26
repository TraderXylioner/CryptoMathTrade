from decimal import Decimal

from type import Order, OrderList, OrderBook


def __order_type_check(func):
    def wrapper(order: dict[float, float] | Order, *args, **kwargs) -> Order:
        return func(Order.validate_order(order), *args, **kwargs)
    return wrapper


def __orderbook_type_check(func):
    def wrapper(orderbook: OrderList | list[Order] | list[dict[float, float]], *args, **kwargs) -> OrderList:
        return func(OrderBook.validate_orderbook(orderbook), *args, **kwargs)
    return wrapper


def __order_type_check_for_convert_price(func):
    def wrapper(order: dict[float, float] | Order, relative_price: float) -> Order:
        return __order_type_check(func)(order, relative_price)
    return wrapper


def __orderbook_type_check_for_convert_price(func):
    def wrapper(orderbook: OrderList | list[Order] | list[dict[float, float]], relative_price: float) -> OrderList:
        return __orderbook_type_check(func)(orderbook, relative_price)
    return wrapper


def check_fee(fee: Decimal | float) -> Decimal | float:
    if not (0 <= fee < 1):
        raise ValueError(f'fee must be >= 0 and < 1. Please verify that your value is in the decimal form of a percentage (if fee = 1% value must be 0.01), you value is {fee}')
    return fee
