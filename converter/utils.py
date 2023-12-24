from type import Order, OrderList


def check_order(order):
    if isinstance(order, Order):
        order = order
    elif isinstance(order, dict):
        order = Order.from_dict(order)
    else:
        raise TypeError('order must be valid dict or Order')
    return order


def check_orderbook(orderbook):
    if isinstance(orderbook, OrderList):
        orderbook = orderbook
    elif isinstance(orderbook, list) and all(isinstance(item, Order) for item in orderbook):
        orderbook = OrderList(orderbook)
    elif isinstance(orderbook, list) and all(isinstance(item, dict) for item in orderbook):
        orderbook = OrderList(orderbook)
    else:
        raise TypeError('element must be a valid OrderBook, list of Orders, or list of order dictionaries')
    return orderbook


def __order_type_check(func):
    def wrapper(order: dict[float, float] | Order, *args, **kwargs) -> Order:
        return func(check_order(order), *args, **kwargs)
    return wrapper


def __orderbook_type_check(func):
    def wrapper(orderbook: OrderList | list[Order] | list[dict[float, float]], *args, **kwargs) -> OrderList:
        return func(check_orderbook(orderbook), *args, **kwargs)
    return wrapper


def __two_orderbook_type_check(func):
    def wrapper(first_orderbook: OrderList | list[Order] | list[dict[float, float]],
                second_orderbook: OrderList | list[Order] | list[dict[float, float]],
                *args, **kwargs) -> OrderList:
        return func(check_orderbook(first_orderbook), check_orderbook(second_orderbook), *args, **kwargs)
    return wrapper
