from decimal import Decimal
from enum import Enum

from pydantic import BaseModel


class TimeInForce(Enum):
    """
    GTC	Good Til Canceled An order will be on the book unless the order is canceled.

    IOC	Immediate Or Cancel An order will try to fill the order as much as it can before the order expires.

    FOK	Fill or Kill An order will expire if the full order cannot be filled upon execution.


    Good till canceled (GTC)
    The order will remain valid until it is fully executed or manually canceled by the trader. GTC is suitable for
    traders who are willing to wait for all contracts to be completed at a specified price and can flexibly cancel
    unconcluded contracts at any time.

    Fill or Kill (FOK)
    The order must be immediately executed at the order price or better, otherwise, it will be completely canceled and
    partially filled contracts will not be allowed. This execution strategy is more commonly used by scalping traders or
    day traders looking for short-term market opportunities.

    Immediate or Cancel (IOC)
    The order must be filled immediately at the order limit price or better. If the order cannot be filled immediately,
    the unfilled contracts will be canceled. IOC is usually used to avoid large orders being executed at a price that
    deviates from the ideal price. With this set, the contracts that fail to trade at the specified price will be canceled.
    """
    GTC = 'GTC'
    IOC = 'IOC'
    FOK = 'FOK'


class Side(Enum):
    BUY = 'BUY'
    SELL = 'SELL'


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

    params:
        asks (list[Order]): List of sell orders (asks).

        bids (list[Order]): List of buy orders (bids).
    """
    asks: list[Order]
    bids: list[Order]
