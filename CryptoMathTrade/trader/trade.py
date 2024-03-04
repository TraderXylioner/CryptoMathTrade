from decimal import Decimal

from CryptoMathTrade.types import Order, Deals, Deal


def trade_by_amount(orders: list[Order], amount: Decimal | float) -> Deals:
    """
    Executes trades based on a specified target amount to spend.

    Args:
        orders (list[Order]): The list of orders available for trading.
        amount (Decimal | float): The target amount to spend.
            It can be specified as a Decimal or a float.

    Returns:
        Deals: A collection of deals representing the executed trades.
    """
    if isinstance(amount, float):
        amount = Decimal(amount)
    deals = Deals()

    for order in orders:
        if amount <= 0:
            break

        order_value = order.volume * order.price

        if order_value <= amount:
            deals.deals.append(Deal(price=order.price, volume=order.volume))
        else:
            remaining_volume = amount / order.price
            deals.deals.append(Deal(price=order.price, volume=remaining_volume))
            amount = 0

    return deals


def trade_by_volume(orders: list[Order], volume: float | Decimal) -> Deals:
    """
    Executes trades based on a specified target volume to buy or sell.

    Args:
        orders (list[Order]): The list of orders available for trading.
        volume (Decimal | float): The target volume to buy.
            It can be specified as a Decimal or a float.

    Returns:
        Deals: A collection of deals representing the executed trades.
    """
    if isinstance(volume, float):
        volume = Decimal(volume)
    deals = Deals()

    for order in orders:
        if volume <= 0:
            break

        if order.volume <= volume:
            deals.deals.append(Deal(price=order.price, volume=order.volume))
            volume -= order.volume
        else:
            deals.deals.append(Deal(price=order.price, volume=volume))
            volume = 0

    return deals
