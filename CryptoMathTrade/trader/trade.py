from decimal import Decimal

from CryptoMathTrade.trader.calculate import get_spread
from CryptoMathTrade.trader.utils import check_fee, __orderbook_type_check
from CryptoMathTrade.type import OrderList, Order, ArbitrageDeals, ArbitrageDeal, Deal, Deals, OrderBook


def calculate_spread(asks: OrderList | list[Order] | list[dict[float, float]],
                     bids: OrderList | list[Order] | list[dict[float, float]],
                     asks_fee: float,
                     bids_fee: float) -> ArbitrageDeals:
    asks, bids = OrderBook.validate_orderbook(asks), OrderBook.validate_orderbook(bids)
    asks_fee, bids_fee = check_fee(Decimal(asks_fee)), check_fee(Decimal(bids_fee))

    deals = ArbitrageDeals()
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

        if ask.volume >= bid.volume:
            volume = bid.volume
        else:
            volume = ask.volume
        deals.append(ArbitrageDeal(price_buy=ask.price,
                                   price_sell=bid.price,
                                   volume=volume,
                                   spread=spread,
                                   fee_buy=asks_fee,
                                   fee_sell=bids_fee)
                     )
    return deals


@__orderbook_type_check
def trade_by_amount(orders: OrderList, amount: float) -> Deals:
    amount = Decimal(amount)
    deals = Deals()

    for order in orders:
        if amount <= 0:
            break

        order_value = order.volume * order.price

        if order_value <= amount:
            deals.append(Deal(order.price, order.volume))
            amount -= order_value
        else:
            remaining_volume = amount / order.price
            deals.append(Deal(order.price, remaining_volume))
            amount = 0

    return deals


@__orderbook_type_check
def trade_by_volume(orders: OrderList, volume: float | Decimal) -> Deals:
    volume = Decimal(volume)
    deals = Deals()

    for order in orders:
        if volume <= 0:
            break
        if order.volume <= volume:
            deals.append(Deal(order.price, order.volume))
            volume -= order.volume
        else:
            deals.append(Deal(order.price, volume))
            volume = 0
    return deals
