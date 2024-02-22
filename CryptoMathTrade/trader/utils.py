from decimal import Decimal


def check_fee(fee: Decimal | float) -> Decimal:
    if isinstance(fee, float):
        fee = Decimal(fee)
    if not (0 <= fee < 1):
        raise ValueError(f'fee must be >= 0 and < 1. Please verify that your value is in the decimal form of a percentage (if fee = 1% value must be 0.01), you value is {fee}')
    return fee


def get_spread(ask: Decimal | float,
               bid: Decimal | float,
               ) -> Decimal:
    """
    Calculate the spread between bid and ask prices.

    Args:
        ask (Decimal | float): The ask price.
        bid (Decimal | float): The bid price.

    Returns:
        Decimal: The spread expressed as a decimal representation of a percentage.
                It represents the difference between the bid and ask prices,
                divided by the bid price.
    """
    return (Decimal(bid) - Decimal(ask)) / Decimal(bid)
