from type import Order


class Deal(Order):
    ...


class Deals:
    def __init__(self, deals: list[Deal] | list[dict[float, float]] | None = None):
        self.deals = self.validate_deals(deals)

    @staticmethod
    def validate_deals(deals: list[Deal] | list[dict[float, float]] | None) -> list:
        if not deals:
            return []
        elif all(isinstance(item, Deal) for item in deals):
            return deals
        elif all(isinstance(item, dict) for item in deals):
            return [Deal.from_dict(deal) for deal in deals]
        else:
            raise TypeError('value must be a valid list of Deals or list of deal dictionaries')

    def __repr__(self):
        return f'{self.deals}'

    def __len__(self):
        return len(self.deals)

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
