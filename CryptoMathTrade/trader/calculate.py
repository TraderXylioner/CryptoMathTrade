from decimal import Decimal

from CryptoMathTrade.types import Order


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


def convert_price_in_order(order: Order, relative_price: float | Decimal) -> Order:
    """
    Converts the price of an order by applying a relative price factor.

    For example, if the order is on pair BTC/ETH = 18 (for 18 ETH you can buy 1 BTC),
    ETH/USDT = 2000, and you want to convert in USDT.
    18 x 2000 = 36000 price BTC in USDT.

    Args:
        order (Order): The order to be modified.
        relative_price (float | Decimal): The relative price factor to apply.
            It can be specified as a float or a Decimal.

    Returns:
        Order: The modified order with the price converted.
    """
    return Order(price=order.price * Decimal(relative_price), volume=order.volume)


def convert_price_in_order_list(order_list: list[Order], relative_price: float | Decimal) -> list[Order]:
    """
    Converts the prices of a list of orders by applying a relative price factor.

    For example, if the order is on pair BTC/ETH = 18 (for 18 ETH you can buy 1 BTC),
    ETH/USDT = 2000, and you want to convert in USDT.
    18 x 2000 = 36000 price BTC in USDT.

    Args:
        order_list (list[Order]): The list of orders to be modified.
        relative_price (float | Decimal): The relative price factor to apply.
            It can be specified as a float or a Decimal.

    Returns:
        list[Order]: The list of modified orders with the prices converted.
    """
    return [convert_price_in_order(order, relative_price) for order in order_list]
