from decimal import Decimal
from enum import Enum

from pydantic import BaseModel


class Order(BaseModel):
    """
    Model representing an individual order.

    params:
        price (Decimal): The price of the order.

        volume (Decimal): The volume of the order.
    """
    price: Decimal
    volume: Decimal


class FullOrder(BaseModel):
    symbol: str
    orderId: int
    price: Decimal
    # StopPrice: Decimal
    origQty: Decimal
    executedQty: Decimal
    cummulativeQuoteQty: Decimal
    status: str
    type: str
    side: Side
    # time: int
    # updateTime: int
    # origQuoteOrderQty: Decimal
    # clientOrderID: str
    # fee: Decimal


class OrderBook(BaseModel):
    """
    Model representing an order book with both buy and sell orders.

    Attributes:
        asks (list[Order]): List of sell orders (asks).
        bids (list[Order]): List of buy orders (bids).
    """
    asks: list[Order]
    bids: list[Order]


class TimeInForce(Enum):
    """
    GTC	Good Til Canceled An order will be on the book unless the order is canceled.

    IOC	Immediate Or Cancel An order will try to fill the order as much as it can before the order expires.

    FOK	Fill or Kill An order will expire if the full order cannot be filled upon execution.
    """
    GTC = 'GTC'
    IOC = 'IOC'
    FOK = 'FOK'


class Side(Enum):
    BUY = 'BUY'
    SELL = 'SELL'
