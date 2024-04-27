import time

from ...types import OrderBook, Trade, Ticker, Order, Side
from .._response import Response


def _serialize_depth(data, response):
    return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in data['asks']],
                                   bids=[Order(price=bid[0], volume=bid[1]) for bid in data['bids']],
                                   ),
                    response_object=response,
                    )


def _serialize_trades(data, response):
    return Response(data=[Trade(id=trade.get('tradeId'),
                                price=trade.get('price'),
                                quantity=trade.get('size'),
                                side=Side.BUY if trade.get('side') == 'buy' else Side.SELL,
                                time=trade.get('ts'),
                                ) for trade in data],
                    response_object=response,
                    )


def _serialize_ticker(data, response):
    return Response(data=[Ticker(symbol=ticker.get('symbol'),
                                 priceChange=float(ticker['open']) - float(ticker['lastPr']),
                                 priceChangePercent=((float(ticker['open']) - float(ticker['lastPr'])) / (
                                     float(ticker['open'] if float(ticker['open']) else 1))) * 100,
                                 openPrice=ticker.get('open'),
                                 highPrice=ticker.get('high24h'),
                                 lowPrice=ticker.get('low24h'),
                                 lastPrice=ticker.get('lastPr'),
                                 volume=ticker.get('baseVolume'),
                                 quoteVolume=ticker.get('quoteVolume'),
                                 # openTime=ticker.get('openTime'),
                                 closeTime=ticker.get('ts'),
                                 ) for ticker in data],
                    response_object=response,
                    )
