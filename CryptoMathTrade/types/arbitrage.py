from decimal import Decimal

from pydantic import BaseModel


class ArbitrageDeal(BaseModel):
    """
    Model representing an arbitrage deal.

    params:
        price_buy (Decimal): The price at which the asset is bought.

        price_sell (Decimal): The price at which the asset is sold.

        volume (Decimal): The volume of the asset involved in the deal.

        fee_buy (Decimal): The fee percentage applied when buying the asset.

        fee_sell (Decimal): The fee percentage applied when selling the asset.

        spread (Decimal): The calculated spread between the buy and sell prices,taking into account the buy and sell fees.
         Initialized to None,it is automatically calculated upon object creation.
    """
    price_buy: Decimal
    price_sell: Decimal
    volume: Decimal
    fee_buy: Decimal
    fee_sell: Decimal
    spread: Decimal = None

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of ArbitrageDeal.
        Calculates the spread automatically using the provided prices and fees.
        """
        super().__init__(*args, **kwargs)
        self.spread = self.calculate_spread()

    def calculate_spread(self):
        """
        Method to calculate the spread based on the buy and sell prices and fees.
        """
        from ..trader.utils import get_spread
        return get_spread(
            ask=self.price_buy * (Decimal(1) + self.fee_buy),
            bid=self.price_sell * (Decimal(1) - self.fee_sell)
        )
