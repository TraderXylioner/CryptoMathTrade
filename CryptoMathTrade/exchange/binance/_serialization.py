from ...types import OrderBook, Trade, Ticker, Order, Side
from .._response import Response


def _serialize_depth(data, response):
    return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in data['asks']],
                                   bids=[Order(price=bid[0], volume=bid[1]) for bid in data['bids']],
                                   ),
                    response_object=response,
                    )


def _serialize_trades(data, response):
    return Response(data=[Trade(id=trade.get('id'),
                                price=trade.get('price'),
                                quantity=trade.get('qty'),
                                side=Side.SELL if trade.get('isBuyerMaker') else Side.BUY,
                                time=trade.get('time'),
                                ) for trade in data],
                    response_object=response,
                    )


def _serialize_ticker(data, response):
    if isinstance(data, list):
        data = [Ticker(**ticker) for ticker in data]
    elif isinstance(data, dict):
        data = [Ticker(**data)]
    else:
        raise Exception(data)

    return Response(data=data, response_object=response)
