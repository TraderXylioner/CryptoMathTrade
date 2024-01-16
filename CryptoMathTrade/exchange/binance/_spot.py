from CryptoMathTrade.exchange.binance.api import API
from CryptoMathTrade.exchange.binance.setting import GET_ORDERS_URL, OPEN_ORDERS_URL, ORDER_URL


class Spot(API):
    def __init__(self, api_key=None, api_secret=None, **kwargs):
        super().__init__(api_key, api_secret, **kwargs)

    def get_orders(self,
                   symbol: str,
                   orderId: int | None = None,
                   startTime: int | None = None,
                   endTime: int | None = None,
                   limit: int | None = None,
                   recvWindow: int | None = None,
                   ):
        params = {'symbol': symbol,
                  'orderId': orderId,
                  'startTime': startTime,
                  'endTime': endTime,
                  'limit': limit,
                  'recvWindow': recvWindow
                  }
        return self.sign_request('GET', GET_ORDERS_URL, params)

    def get_open_order(self,
                       symbol: str,
                       orderId: int | None = None,
                       origClientOrderId: str | None = None,
                       recvWindow: int | None = None,
                       ):
        params = {'symbol': symbol,
                  'orderId': orderId,
                  'origClientOrderId': origClientOrderId,
                  'recvWindow': recvWindow,
                  }
        if not orderId and not origClientOrderId:
            raise ValueError('Param "origClientOrderId" or "orderId" must be sent, but both were empty/null!')
        return self.sign_request('GET', ORDER_URL, params)

    def get_open_orders(self,
                        symbol: str | None = None,
                        recvWindow: int | None = None,
                        ):
        params = {'symbol': symbol,
                  'recvWindow': recvWindow
                  }
        return self.sign_request('GET', OPEN_ORDERS_URL, params)

    def delete_open_orders(self,
                           symbol: str,
                           recvWindow: int | None = None,
                           ):
        params = {'symbol': symbol,
                  'recvWindow': recvWindow
                  }
        return self.sign_request('DELETE', OPEN_ORDERS_URL, params)

    # def new_order(self,
    #               symbol: str,
    #               side,
    #               type,
    #               timeInForce: str | None = None,
    #               quantity: float | None = None,
    #               price: float | None = None,
    #               ):
    #     params = {'symbol': symbol,
    #               'side': side,
    #               'type': type,
    #               'timeInForce': timeInForce,
    #               'quantity': quantity,
    #               'price': price,
    #               }
    #     return self.sign_request('POST', ORDER_URL, params)
