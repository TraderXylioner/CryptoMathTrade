from type import Order, OrderBook


def __order_type_check(func):
    def wrapper(order: dict[float, float] | Order, *args, **kwargs) -> Order:
        if isinstance(order, Order):
            _order = order
        elif isinstance(order, dict):
            _order = Order.from_dict(order)
        else:
            raise TypeError('order must be valid dict or Order')
        return func(_order, *args, **kwargs)
    return wrapper


def __orderbook_type_check(func):
    def wrapper(orderbook: OrderBook | list[Order] | list[dict[float, float]], *args, **kwargs) -> OrderBook:
        if isinstance(orderbook, OrderBook):
            _orderbook = orderbook
        elif isinstance(orderbook, list) and all(isinstance(item, Order) for item in orderbook):
            _orderbook = OrderBook(orderbook)
        elif isinstance(orderbook, list) and all(isinstance(item, dict) for item in orderbook):
            _orderbook = OrderBook(orderbook)
        else:
            raise TypeError('element must be a valid OrderBook, list of Orders, or list of order dictionaries')

        return func(_orderbook, *args, **kwargs)

    return wrapper


def __order_type_check_for_converter(func):
    def wrapper(order: dict[float, float] | Order, relative_price: float) -> Order:
        return __order_type_check(func)(order, relative_price)
    return wrapper


def __orderbook_type_check_for_converter(func):
    def wrapper(orderbook: OrderBook | list[Order] | list[dict[float, float]], relative_price: float) -> OrderBook:
        return __orderbook_type_check(func)(orderbook, relative_price)
    return wrapper
