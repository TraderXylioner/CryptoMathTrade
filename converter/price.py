from converter.utils import __order_type_check, __orderbook_type_check
from type import Order, OrderList


def __order_type_check_for_converter(func):
    def wrapper(order: dict[float, float] | Order, relative_price: float) -> Order:
        return __order_type_check(func)(order, relative_price)
    return wrapper


def __orderbook_type_check_for_converter(func):
    def wrapper(orderbook: OrderList | list[Order] | list[dict[float, float]], relative_price: float) -> OrderList:
        return __orderbook_type_check(func)(orderbook, relative_price)
    return wrapper


@__order_type_check_for_converter
def convert_price_from_order(order: Order, relative_price: float) -> Order:
    """
    Function converting order relative to relative_price.
    For example, if the order is on pair BTC/ETH = 18 (for 18 ETH you can buy 1 BTC),
    ETH/USDT = 2000, and you want to convert in USDT.
    18 x 2000 = 36000 price BTC in USDT.
    """
    return Order(price=order.price * relative_price, volume=order.volume)  # maybe не создавать новый объект, а менять старый?


@__orderbook_type_check_for_converter
def convert_price_from_orderbook(orderbook: OrderList, relative_price: float) -> OrderList:
    return OrderList([convert_price_from_order(order, relative_price) for order in orderbook.orders])   # maybe не создавать новый объект, а менять старый?
