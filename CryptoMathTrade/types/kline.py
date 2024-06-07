from decimal import Decimal

from pydantic import BaseModel


class Kline(BaseModel):
    """
    Model representing a Kline (candlestick) data point for market analysis.

    Attributes:
        openTime (int): The timestamp for when the candlestick opened.
        openPrice (Decimal): The price at which the candlestick opened.
        highPrice (Decimal): The highest price during the candlestick's time period.
        lowerPrice (Decimal): The lowest price during the candlestick's time period.
        closePrice (Decimal): The price at which the candlestick closed.
        transactionPrice (Decimal): The price of the last transaction within the candlestick's time period.
        closeTime (int): The timestamp for when the candlestick closed.
        amount (Decimal): The total amount (volume) of the asset traded during the candlestick's time period.
    """
    openTime: int
    openPrice: Decimal
    highPrice: Decimal
    lowerPrice: Decimal
    closePrice: Decimal
    transactionPrice: Decimal
    closeTime: int
    amount: Decimal

