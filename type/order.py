from decimal import Decimal


class Order:
    def __init__(self, price: float, volume: float):
        self.price: Decimal = Decimal(price)
        self.volume: Decimal = Decimal(volume)

    def __repr__(self):
        return '{' + f"'price': {float(self.price)}, " \
                     f"'volume': {float(self.volume)}" + '}'

    @classmethod
    def from_dict(cls, order_data: dict[float, float]) -> 'Order':
        price = order_data.get('price')
        volume = order_data.get('volume')
        if not price:
            raise ValueError("'price' must be present in order_data")
        if not volume:
            raise ValueError("'volume' must be present in order_data")

        return cls(price=Decimal(price), volume=Decimal(volume))


class OrderList:
    def __init__(self, orders: list[Order] | list[dict[float, float]]):
        self.orders = self.__validate_order_list(orders)

    @staticmethod
    def __validate_order_list(orders: list[Order] | list[dict[float, float]]) -> list:
        if all(isinstance(item, Order) for item in orders):
            return orders
        elif all(isinstance(item, dict) for item in orders):
            return [Order.from_dict(order) for order in orders]
        else:
            raise TypeError('value must be a valid list of Orders or list of order dictionaries')

    def __repr__(self):
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
        self.asks = self.__validate_orderbook(asks)
        self.bids = self.__validate_orderbook(bids)

    @staticmethod
    def __validate_orderbook(orders: OrderList | list[Order] | list[dict[float, float]]) -> list:
        if isinstance(orders, OrderList):
            return orders
        elif all(isinstance(item, Order) for item in orders):
            return OrderList(orders)
        elif all(isinstance(item, dict) for item in orders):
            return OrderList(orders)
        else:
            raise TypeError('value must be a valid list of Orders or list of order dictionaries')

    def __repr__(self):
        return f'asks: {self.asks}\nbids: {self.bids}'
