import time

from ...types import OrderBook, Trade, Ticker, Order, Side
from .._response import Response


def _serialize_depth(data, response):
    data = data['data']
    data['asks'] = data['asks'][::-1]
    return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in data['asks']],
                                   bids=[Order(price=bid[0], volume=bid[1]) for bid in data['bids']],
                                   ),
                    response_object=response,
                    )


def _serialize_trades(data, response):
    data = data['data']
    return Response(data=[Trade(id=trade.get('id'),
                                price=trade.get('price'),
                                quantity=trade.get('qty'),
                                time=trade.get('time'),
                                ) for trade in data],
                    response_object=response,
                    )


def _serialize_ticker(data, response):
    data = data['data']
    return Response(data=[Ticker(symbol=ticker.get('symbol'),
                                 priceChange=ticker.get('priceChange'),
                                 priceChangePercent=ticker.get('priceChangePercent')[:-1],
                                 openPrice=ticker.get('openPrice'),
                                 highPrice=ticker.get('highPrice'),
                                 lowPrice=ticker.get('lowPrice'),
                                 lastPrice=ticker.get('lastPrice'),
                                 volume=ticker.get('volume'),
                                 quoteVolume=ticker.get('quoteVolume'),
                                 openTime=ticker.get('openTime'),
                                 closeTime=ticker.get('closeTime'),
                                 ) for ticker in data],
                    response_object=response,
                    )
