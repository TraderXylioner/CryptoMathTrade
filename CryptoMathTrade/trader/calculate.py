from decimal import Decimal


def get_spread(ask: float | Decimal, bid: float | Decimal) -> Decimal:
    return ((Decimal(bid) - Decimal(ask)) / Decimal(bid)) * Decimal(100)
