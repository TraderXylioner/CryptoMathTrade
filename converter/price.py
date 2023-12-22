from type import Order, OrderBook


# def __check_converted(func):
#     def wrapper(order: Order, *args, **kwargs):
#         if order.order_type == 'converted':
#             raise ValueError('order already converted')
#         elif order.order_type == 'native':
#             return func(order, *args, **kwargs)
#         else:
#             raise ValueError('order undefined')
#     return wrapper


# @__check_converted
def convert_price_from_order(order: dict, price: float) -> Order:
    _order = Order.from_dict(order)
    return Order(price=price, volume=_order.volume)


# @__check_converted
def convert_price_from_orderbook(orderbook: OrderBook, price: float):
    ...
