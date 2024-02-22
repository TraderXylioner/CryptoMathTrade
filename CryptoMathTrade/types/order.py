from decimal import Decimal
from pydantic import BaseModel


class Order(BaseModel):
    price: Decimal
    volume: Decimal
