from decimal import Decimal

from pydantic import BaseModel


class Symbol(BaseModel):
    id: int | None = None
    symbol: str
    firstCoin: str | None = None
    secondCoin: str | None = None
    minQty: Decimal | None = None
    maxQty: Decimal | None = None
    status: str | int
    minNotional: Decimal | None = None
    maxNotional: Decimal | None = None
    tickSize: Decimal | None = None
    stepSize: Decimal | None = None
    apiStateSell: bool | None = None
    apiStateBuy: bool | None = None
    timeOnline: int | None = None
