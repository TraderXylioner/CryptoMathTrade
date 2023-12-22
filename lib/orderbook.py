from lib.order import Order


class OrderBook:
    def __init__(self, orders: list[Order]):
        self.orders = [Order.from_dict(order) for order in orders]

    def __repr__(self):
        orders_repr = ', '.join(repr(order) for order in self.orders)
        return f'{self.__class__.__name__}[{orders_repr}]'
