from decimal import Decimal

from pydantic import BaseModel

from ..trader.utils import get_spread


class ArbitrageDeal(BaseModel):
    price_buy: Decimal
    price_sell: Decimal
    volume: Decimal
    fee_buy: Decimal
    fee_sell: Decimal
    spread: Decimal = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spread = self.calculate_spread()

    def calculate_spread(self):
        """
        Method to calculate the spread based on the buy and sell prices and fees.
        """
        return get_spread(
            ask=self.price_buy * (Decimal(1) + self.fee_buy),
            bid=self.price_sell * (Decimal(1) - self.fee_sell)
        )
