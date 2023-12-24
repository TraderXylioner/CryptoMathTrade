from converter.utils import __order_type_check, __orderbook_type_check
from type import Order, OrderBook


@__order_type_check
def convert_price_from_order(order: dict[float, float] | Order, relative_price: float) -> Order:
    """
    Function converting order relative to relative_price.
    For example, if the order is on pair BTC/ETH = 18 (for 18 ETH you can buy 1 BTC),
    ETH/USDT = 2000, and you want to convert in USDT.
    18 x 2000 = 36000 price BTC in USDT.
    """
    return Order(price=order.price * relative_price, volume=order.volume)


@__orderbook_type_check
def convert_price_from_orderbook(orderbook: OrderBook | list[Order] | list[dict[float, float]], relative_price: float):
    return OrderBook([convert_price_from_order(order, relative_price) for order in orderbook.orders])
