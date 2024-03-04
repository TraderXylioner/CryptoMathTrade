from decimal import Decimal

from .utils import check_fee, get_spread
from ..types.order import Order
from ..types.arbitrage import ArbitrageDeal


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


def calculate_spread(asks: list[Order],
                     bids: list[Order],
                     asks_fee: Decimal | float,
                     bids_fee: Decimal | float) -> list[ArbitrageDeal]:
    """
    Calculates arbitrage deals based on the provided ask and bid orders,
    taking into account the ask and bid fees.

    Args:
        asks (list[Order]): The list of ask orders.
        bids (list[Order]): The list of bid orders.
        asks_fee (Decimal | float): The fee percentage for ask orders.
            It can be specified as a Decimal or a float.
        bids_fee (Decimal | float): The fee percentage for bid orders.
            It can be specified as a Decimal or a float.

    Returns:
        list[ArbitrageDeal]: A list of ArbitrageDeal objects representing
        the arbitrage deals calculated.
    """
    asks_fee, bids_fee = check_fee(asks_fee), check_fee(bids_fee)

    deals = []

    while min(len(asks), len(bids)) > 0:
        ask = asks[0]
        bid = bids[0]

        adjusted_ask_price = ask.price * (Decimal(1) + asks_fee)
        adjusted_bid_price = bid.price * (Decimal(1) - bids_fee)

        spread = get_spread(adjusted_ask_price, adjusted_bid_price)

        if spread <= 0:
            break

        difference_in_volume = bid.volume - ask.volume
        if difference_in_volume < 0:
            ask.volume = difference_in_volume * -1
            bids.pop(0)
        elif difference_in_volume == 0:
            bids.pop(0)
            asks.pop(0)
        else:
            bid.volume = difference_in_volume
            asks.pop(0)
        volume = min(ask.volume, bid.volume)
        deals.append(ArbitrageDeal(
            price_buy=ask.price,
            price_sell=bid.price,
            volume=volume,
            fee_buy=asks_fee,
            fee_sell=bids_fee
        ))

    return deals
