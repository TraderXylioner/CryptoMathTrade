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
                                price=trade.get('px'),
                                quantity=trade.get('sz'),
                                side=Side.BUY if trade['side'] == 'buy' else Side.SELL,
                                time=trade.get('ts'),
                                ) for trade in data],
                    response_object=response,
                    )


def _serialize_ticker(data, response):
    return Response(data=[Ticker(symbol=ticker.get('instId').replace("-SWAP", ""),
                                 openPrice=ticker.get('open24h'),
                                 highPrice=ticker.get('high24h'),
                                 lowPrice=ticker.get('low24h'),
                                 lastPrice=ticker.get('last'),
                                 volume=ticker.get('vol24h'),
                                 quoteVolume=ticker.get('volCcy24h'),
                                 closeTime=ticker.get('ts'),
                                 ) for ticker in data], response_object=response)
