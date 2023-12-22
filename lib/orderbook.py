from pydantic import BaseModel
from lib.order import Order


class OrderBook(BaseModel):
    orders: list[Order]

    def __init__(self, orders: list[Order]):
        super().__init__(orders=orders)
