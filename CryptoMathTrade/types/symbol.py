from decimal import Decimal

from pydantic import BaseModel


class Symbol(BaseModel):
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
