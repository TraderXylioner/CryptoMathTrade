from decimal import Decimal


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
