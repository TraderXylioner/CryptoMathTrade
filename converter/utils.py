from type import Order, OrderList, OrderBook


def __order_type_check(func):
    def wrapper(order: dict[float, float] | Order, *args, **kwargs) -> Order:
        return func(Order.validate_order(order), *args, **kwargs)
    return wrapper


def __orderbook_type_check(func):
    def wrapper(orderbook: OrderList | list[Order] | list[dict[float, float]], *args, **kwargs) -> OrderList:
        return func(OrderBook.validate_orderbook(orderbook), *args, **kwargs)
    return wrapper


def __two_orderbook_type_check(func):
    def wrapper(first_orderbook: OrderList | list[Order] | list[dict[float, float]],
                second_orderbook: OrderList | list[Order] | list[dict[float, float]],
                *args, **kwargs) -> OrderList:
        return func(OrderBook.validate_orderbook(first_orderbook), OrderBook.validate_orderbook(second_orderbook), *args, **kwargs)
    return wrapper
