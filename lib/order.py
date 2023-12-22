from pydantic import BaseModel


class Order(BaseModel):
    price: float
    volume: float

    def __init__(self, price: float, volume: float):
        super().__init__(price=price, volume=volume)
