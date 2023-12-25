from decimal import Decimal

from type.utils import validate_order_list


class Order:
    def __init__(self, price: float, volume: float):
        self.price: Decimal = Decimal(price)
        self.volume: Decimal = Decimal(volume)

    def __repr__(self):
        return f'{self.__dict__}'

    @classmethod
    def from_dict(cls, order_data: dict[float, float]) -> 'Order':
        price = order_data.get("price")
        volume = order_data.get("volume")
        if not price:
            raise ValueError("'price' must be present in order_data")
        if not volume:
            raise ValueError("'volume' must be present in order_data")

        return cls(price=Decimal(price), volume=Decimal(volume))


class OrderList:
    def __init__(self, orders: list[Order] | list[dict[float, float]]):
        self.orders = validate_order_list(orders)

    def __repr__(self):
        if not all(isinstance(order, Order) for order in self.orders):
            raise TypeError('All items in orders must be of type Order')

        return f'{self.orders}'

    def __len__(self):
        return len(self.orders)

    def __getitem__(self, index):
        return self.orders[index]

    def __setitem__(self, index, value):
        self.orders[index] = value

    def __delitem__(self, index):
        del self.orders[index]

    def pop(self, index=None):
        if index is None:
            index = -1
        item = self.orders.pop(index)
        return item

    def append(self, order):
        self.orders.append(order)


class OrderBook:
    def __init__(self,
                 asks: OrderList | list[Order] | list[dict[float, float]],
                 bids: OrderList | list[Order] | list[dict[float, float]]):
        self.asks = validate_order_list(asks)
        self.bids = validate_order_list(bids)

    def __repr__(self):
        return f'asks: {self.asks}\nbids: {self.bids}'
