from decimal import Decimal

from trader.calculate import get_spread


class ArbitrageDeal:
    def __init__(self, price_buy: float,
                 price_sell: float,
                 volume: float,
                 spread: float | None = None,
                 fee_buy: float | Decimal = 0.0,
                 fee_sell: float | Decimal = 0.0):
        self.price_buy: Decimal = Decimal(price_buy)
        self.price_sell: Decimal = Decimal(price_sell)
        self.volume: Decimal = Decimal(volume)
        self.fee_buy: Decimal = Decimal(fee_buy)
        self.fee_sell: Decimal = Decimal(fee_sell)
        self.spread: Decimal = Decimal(spread) if spread else get_spread(self.price_buy * (Decimal(1) + self.fee_buy),
                                                                         self.price_sell * (Decimal(1) - self.fee_sell)
                                                                         )

    def __repr__(self):
        return '{' + f"'price_buy': {float(self.price_buy)}, " \
               f"price_sell: {float(self.price_sell)}, " \
               f"'volume': {float(self.volume)}, " \
               f"'fee_buy': {float(self.fee_buy)}, " \
               f"'fee_sell': {float(self.fee_sell)}, " \
               f"'spread': {float(self.spread)}" + '}'


class ArbitrageDeals:
    def __init__(self, deals: list[ArbitrageDeal] = None):
        self.deals = deals if deals else []

    def __repr__(self):
        return f'{self.__dict__}'

    def __getitem__(self, index):
        return self.deals[index]

    def __setitem__(self, index, value):
        self.deals[index] = value

    def __delitem__(self, index):
        del self.deals[index]

    def pop(self, index=None):
        if index is None:
            index = -1
        item = self.deals.pop(index)
        return item

    def append(self, deal):
        self.deals.append(deal)
