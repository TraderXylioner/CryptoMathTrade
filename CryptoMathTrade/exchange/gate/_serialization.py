import time

from ...types import OrderBook, Trade, Ticker, Order, Side
from .._response import Response
from ...types.balance import Balance


def _serialize_depth(data, response):
    return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in data['asks']],
                                   bids=[Order(price=bid[0], volume=bid[1]) for bid in data['bids']],
                                   ),
                    response_object=response,
                    )


def _serialize_trades(data, response):
    return Response(data=[Trade(id=trade.get('id'),
                                price=trade.get('price'),
                                quantity=trade.get('amount'),
                                side=Side.BUY if trade.get('side') == 'buy' else Side.SELL,
                                time=trade.get('create_time'),
                                ) for trade in data],
                    response_object=response,
                    )


def _serialize_ticker(data, response):
    return Response(data=[Ticker(symbol=ticker.get('currency_pair'),
                                 openPrice=float(ticker.get('last')) / (
                                         1 + float(ticker.get('change_percentage')) / 100),
                                 highPrice=ticker.get('high_24h'),
                                 lowPrice=ticker.get('low_24h'),
                                 lastPrice=ticker.get('last'),
                                 volume=ticker.get('base_volume'),
                                 quoteVolume=ticker.get('quote_volume'),
                                 closeTime=int(time.time()),
                                 ) for ticker in data], response_object=response)


def _serialize_balance(data, response):
    return Response(data=[Balance(asset=i['currency'],
                                  free=i['available'],
                                  locked=i['locked'],
                                  ) for i in data],
                    response_object=response,
                    )
