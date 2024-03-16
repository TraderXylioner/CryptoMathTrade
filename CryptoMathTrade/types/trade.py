from pydantic import BaseModel


class Trade(BaseModel):
    id: int
    price: float
    quantity: float
    time: int
    # quoteQuantity: float = price * quantity
    # isBuyerMaker: bool | None = None
    # isBestMatch: bool | None = None
