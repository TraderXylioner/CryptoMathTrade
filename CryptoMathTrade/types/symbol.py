from decimal import Decimal

from pydantic import BaseModel


class Symbol(BaseModel):
    """
    Model representing an individual order.

    params:
        price (Decimal): The price of the order.

        volume (Decimal): The volume of the order.
    """
    symbol: str
    minQty: Decimal
    maxQty: Decimal
    minNotional: Decimal
    maxNotional: Decimal
    status: int
    tickSize: Decimal
    stepSize: Decimal
    apiStateSell: bool
    apiStateBuy: bool
    timeOnline: int
