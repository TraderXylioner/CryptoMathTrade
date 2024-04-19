from decimal import Decimal
from enum import Enum

from pydantic import BaseModel


class Order(BaseModel):
    """
    Model representing an individual order.

    Attributes:
        price (Decimal): The price of the order.
        volume (Decimal): The volume of the order.
    """
    price: Decimal
    volume: Decimal  #

    symbol: str = None
    orderId: None = None
    origQty: None = None  #
    executedQty: None = None
    cummulativeQuoteQty: None = None
    status: None = None
    type: None = None
    side: None = None
    time: None = None
    updateTime: None = None
    origQuoteOrderQty: None = None
    clientOrderID: None = None


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
