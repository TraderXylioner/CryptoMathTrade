from dataclasses import dataclass


@dataclass
class Trade:
    id: int
    price: float
    qty: float
    quoteQty: float
    time: int
    isBuyerMaker: bool
    isBestMatch: bool


@dataclass
class Trades:
    trades: list
