from pydantic import BaseModel


class Trade(BaseModel):
    id: int
    price: float
    qty: float
    time: int
    isBuyerMaker: bool | None = None
    quoteQty: float | None = None
    isBestMatch: bool | None = None
