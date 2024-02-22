from decimal import Decimal
from pydantic import BaseModel


class Order(BaseModel):
    """
    Model representing an individual order.

    Attributes:
        price (Decimal): The price of the order.
        volume (Decimal): The volume of the order.
    """
    price: Decimal
    volume: Decimal


class OrderBook(BaseModel):
    """
    Model representing an order book with both buy and sell orders.

    Attributes:
        asks (list[Order]): List of sell orders (asks).
        bids (list[Order]): List of buy orders (bids).
    """
    asks: list[Order]
    bids: list[Order]
