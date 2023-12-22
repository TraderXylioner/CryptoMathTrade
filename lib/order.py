class Order:
    def __init__(self, price: float, volume: float):
        self.price: float = price
        self.volume: float = volume

    def __repr__(self):
        return f'{self.__class__.__name__}{vars(self)}'

    @classmethod
    def from_dict(cls, order_data: dict[float, float]) -> 'Order':
        price = order_data.get("price")
        volume = order_data.get("volume")
        return cls(price=price, volume=volume)
