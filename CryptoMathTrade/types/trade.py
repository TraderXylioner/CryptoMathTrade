from pydantic import BaseModel

from .order import Side


class Trade(BaseModel):
    id: int
    price: float
    quantity: float
    side: Side
    time: int
    # quoteQuantity: float = price * quantity
