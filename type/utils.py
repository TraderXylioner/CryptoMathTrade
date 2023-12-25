from type import OrderList, Order


def validate_order_list(orderList: OrderList) -> OrderList:
    if isinstance(orderList, OrderList):
        return orderList
    elif all(isinstance(item, Order) for item in orderList):
        return OrderList(orderList)
    elif all(isinstance(item, dict) for item in orderList):
        return OrderList(orderList)
    else:
        raise TypeError('value must be a valid list of Orders or list of order dictionaries')
