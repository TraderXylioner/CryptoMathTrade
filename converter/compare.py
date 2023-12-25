from decimal import Decimal

from converter.utils import __two_orderbook_type_check
from type import OrderList, Order, ArbitrageDeals, ArbitrageDeal


def get_spread(ask: Decimal, bid: Decimal) -> float:
    return ((bid - ask) / bid) * Decimal(100)


@__two_orderbook_type_check
def calculate_spread(asks: OrderList | list[Order] | list[dict[float, float]],
                     bids: OrderList | list[Order] | list[dict[float, float]],
                     asks_fee: float,
                     bids_fee: float) -> ArbitrageDeals:
    if not (0 <= asks_fee < 1) or not (0 <= bids_fee < 1):
        raise ValueError('fee must be >= 0 and < 1. Please verify that your value is in the decimal form of a percentage (if fee = 1% value must be 0.01)')
    deals = ArbitrageDeals()
    asks_fee, bids_fee = Decimal(asks_fee), Decimal(bids_fee)
    while min(len(asks), len(bids)) > 0: # разнести по функциям
        ask = asks[0]
        bid = bids[0]
        adjusted_ask_price = ask.price * (Decimal(1) + asks_fee)
        adjusted_bid_price = bid.price * (Decimal(1) - bids_fee)
        spread = get_spread(adjusted_ask_price, adjusted_bid_price)
        if not spread > 0:
            break

        difference_in_volume = bid.volume - ask.volume
        if difference_in_volume < 0:
            asks[0].volume = difference_in_volume * -1
            bids.pop(0)
        elif difference_in_volume == 0:
            bids.pop(0)
            asks.pop(0)
        else:
            bids[0].volume = difference_in_volume
            asks.pop(0)

        if ask.volume >= bid.volume:
            volume = bid.volume
        else:
            volume = ask.volume
        deals.append(ArbitrageDeal(ask.price, bid.price, volume, spread))
    return deals
