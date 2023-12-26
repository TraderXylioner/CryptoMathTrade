from CryptoMathTrade.type import Order, OrderList

orders = [{'price': 100.0, 'volume': 0.1},
          {'price': 101.0, 'volume': 0.2},
          {'price': 102.0, 'volume': 0.3},
          {'price': 103.0, 'volume': 0.4},
          {'price': 104.0, 'volume': 0.5},
          ]

o1 = Order.from_dict({'price': 100.0, 'volume': 0.1})
o2 = Order.from_dict({'price': 101.0, 'volume': 0.2})
o3 = Order.from_dict({'price': 102.0, 'volume': 0.3})
o4 = Order.from_dict({'price': 103.0, 'volume': 0.4})
o5 = Order.from_dict({'price': 104.0, 'volume': 0.5})

new_orders = OrderList(orders)
print(new_orders)

new_orders = OrderList([o1, o2, o3, o4, o5])
print(new_orders)
