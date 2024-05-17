import time

from ...types import OrderBook, Trade, Ticker, Order, Side
from .._response import Response
from ...types.balance import Balance


def _serialize_depth(data, response):
    if 'data' not in data:
        raise Exception(data)
    data = data['data']
    return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in data['asks']],
                                   bids=[Order(price=bid[0], volume=bid[1]) for bid in data['bids']],
                                   ),
                    response_object=response,
                    )


def _serialize_trades(data, response):
    if 'data' not in data:
        raise Exception(data)
    data = data['data']
    return Response(data=[Trade(price=trade[2],
                                quantity=trade[3],
                                side=Side.BUY if trade[4] == 'buy' else Side.SELL,
                                time=trade[1],
                                ) for trade in data],
                    response_object=response,
                    )


def _serialize_trades_for_ws(data, response):
    data = data['data']
    return Response(data=[Trade(price=trade.get('price'),
                                quantity=trade.get('size'),
                                side=Side.BUY if trade.get('side') == 'buy' else Side.SELL,
                                time=trade.get('s_t'),
                                ) for trade in data],
                    response_object=response,
                    )


def _serialize_ticker(data, response):
    if 'data' not in data:
        raise Exception(data)
    data = data['data']
    if isinstance(data, list):
        data = [Ticker(symbol=ticker[0],
                       openPrice=ticker[4],
                       highPrice=ticker[5],
                       lowPrice=ticker[6],
                       lastPrice=ticker[1],
                       volume=ticker[2],
                       quoteVolume=ticker[3],
                       closeTime=ticker[12],
                       ) for ticker in data]
    elif isinstance(data, dict):
        data = [Ticker(symbol=data.get('symbol'),
                       openPrice=data.get('open_24h'),
                       highPrice=data.get('high_24h'),
                       lowPrice=data.get('low_24h'),
                       lastPrice=data.get('last'),
                       volume=data.get('v_24h'),
                       quoteVolume=data.get('qv_24h'),
                       closeTime=data.get('ts'),
                       )]
    else:
        raise Exception(data)

    return Response(data=data, response_object=response)


def _serialize_balance(data, response):
    return Response(data=[Balance(asset=i.get('currency'),
                                  free=i.get('available'),
                                  locked=i.get('frozen'),
                                  ) for i in data['data']['wallet']],
                    response_object=response,
                    )
