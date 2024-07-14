from decimal import Decimal

from pydantic import BaseModel


class Symbol(BaseModel):
    symbol: str
    minQty: Decimal
    maxQty: Decimal
    status: str | int
    minNotional: Decimal = None
    maxNotional: Decimal = None
    tickSize: Decimal = None
    stepSize: Decimal = None
    apiStateSell: bool = None
    apiStateBuy: bool = None
    timeOnline: int = None
