class Order:
    def __init__(self, price: float, volume: float):
        self.price: float = price
        self.volume: float = volume

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

        return cls(price=price, volume=volume)


class OrderList:
    def __init__(self, orders: list[Order] | list[dict[float, float]]):
        if all(isinstance(item, Order) for item in orders):
            self.orders = orders
        elif all(isinstance(item, dict) for item in orders):
            self.orders = [Order.from_dict(order) for order in orders]
        else:
            raise TypeError('value must be a valid list of Orders or list of order dictionaries')

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


class OrderBook:
    def __init__(self,
                 asks: OrderList | list[Order] | list[dict[float, float]],
                 bids: OrderList | list[Order] | list[dict[float, float]]):
        if isinstance(asks, OrderList):
            self.asks = asks
        elif all(isinstance(item, Order) for item in asks):
            self.asks = OrderList(asks)
        elif all(isinstance(item, dict) for item in asks):
            self.asks = OrderList(asks)
        else:
            raise TypeError('value must be a valid list of Orders or list of order dictionaries')

        if isinstance(bids, OrderList):
            self.bids = bids
        elif all(isinstance(item, Order) for item in bids):
            self.bids = OrderList(bids)
        elif all(isinstance(item, dict) for item in bids):
            self.bids = OrderList(bids)
        else:
            raise TypeError('value must be a valid list of Orders or list of order dictionaries')

    def __repr__(self):
        return f'asks: {self.asks}\nbids: {self.bids}'
