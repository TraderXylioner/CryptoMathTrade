from CryptoMathTrade.trader.utils import __order_type_check_for_convert_price, __orderbook_type_check_for_convert_price
from CryptoMathTrade.type import Order, OrderList
from decimal import Decimal


@__order_type_check_for_convert_price
def convert_price_in_order(order: Order, relative_price: float) -> Order:
    """
    Function converting order relative to relative_price.
    For example, if the order is on pair BTC/ETH = 18 (for 18 ETH you can buy 1 BTC),
    ETH/USDT = 2000, and you want to convert in USDT.
    18 x 2000 = 36000 price BTC in USDT.
    """
    return Order(price=order.price * Decimal(relative_price), volume=order.volume)


@__orderbook_type_check_for_convert_price
def convert_price_in_orderbook(orderbook: OrderList, relative_price: float) -> OrderList:
    return OrderList([convert_price_in_order(order, relative_price) for order in orderbook.orders])
