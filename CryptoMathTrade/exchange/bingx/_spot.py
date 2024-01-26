from ._api import API
from CryptoMathTrade.type import Side, TimeInForce
from .core import get_orders_args


class Spot(API):
    def get_orders(self,
                   symbol: str,
                   orderId: int | None = None,
                   clientOrderID: int | None = None,
                   recvWindow: int | None = None,
                   ):
        return self._query(
            **get_orders_args(self, symbol=symbol, orderId=orderId, clientOrderID=clientOrderID, recvWindow=recvWindow))

    #def get_open_order(self,
    #                   symbol: str,
    #                   orderId: int | None = None,
    #                   origClientOrderId: str | None = None,
    #                   recvWindow: int | None = None,
    #                   ):
    #    return self._query(
    #        **get_open_order_args(self, symbol=symbol, orderId=orderId, origClientOrderId=origClientOrderId,
    #                              recvWindow=recvWindow))
#
    #def get_open_orders(self,
    #                    symbol: str | None = None,
    #                    recvWindow: int | None = None,
    #                    ):
    #    return self._query(**get_open_orders_args(self, symbol=symbol, recvWindow=recvWindow))
#
    #def delete_open_orders(self,
    #                       symbol: str,
    #                       recvWindow: int | None = None,
    #                       ):
    #    return self._query(**delete_open_orders_args(self, symbol=symbol, recvWindow=recvWindow))
#
    #def new_market_order(self,
    #                     symbol: str,
    #                     side: Side | str,
    #                     quantity: float | None = None,
    #                     quoteOrderQty: float | None = None,
    #                     ):
    #    return self._query(**new_order_args(self, symbol=symbol, side=side, type='MARKET', quantity=quantity, quoteOrderQty=quoteOrderQty))
#
    #def new_limit_order(self,
    #                    symbol: str,
    #                    side: Side | str,
    #                    timeInForce: TimeInForce | str,
    #                    quantity: float,
    #                    price: float,
    #                    ):
    #    return self._query(**new_order_args(self, symbol=symbol, side=side, type='LIMIT', timeInForce=timeInForce, quantity=quantity, price=price))
#