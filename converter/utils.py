from type import Order, OrderBook


def __order_type_check(func):
    def wrapper(order: dict[float, float] | Order, relative_price: float) -> Order:
        if isinstance(order, Order):
            _order = order
        elif isinstance(order, dict):
            _order = Order.from_dict(order)
        else:
            raise TypeError('order must be valid dict or Order')
        return func(_order, relative_price)
    return wrapper


def __orderbook_type_check(func):
    def wrapper(orderbook: OrderBook | list[Order] | list[dict[float, float]], relative_price: float) -> Order:
        if isinstance(orderbook, OrderBook):
            _orderbook = orderbook
        elif isinstance(orderbook, list) and all(isinstance(item, Order) for item in orderbook):
            _orderbook = OrderBook(orderbook)
        elif isinstance(orderbook, list) and all(isinstance(item, dict) for item in orderbook):
            _orderbook = OrderBook(orderbook)
        else:
            raise TypeError('element must be a valid OrderBook, list of Orders, or list of order dictionaries')

        return func(_orderbook, relative_price)

    return wrapper
