from pydantic import BaseModel

from .order import Order


class Deal(Order):
    """
    Model representing a deal, which inherits from the Order model.

    params:
        price (Decimal): The price of the deal.

        volume (Decimal): The volume of the deal.
    """


class Deals(BaseModel):
    """
    Model representing a collection of deals.

    params:
        deals (list[Deal]): A list of Deal objects, each representing an individual deal.
    """
    deals: list[Deal] = []
