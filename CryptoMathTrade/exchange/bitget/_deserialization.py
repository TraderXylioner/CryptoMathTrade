import time

from ..errors import ResponseError
from ...types import OrderBook, Trade, Ticker, Order, Side, Symbol, Kline
from .._response import Response
from ...types.account import Balance


def _deserialize_depth(data, response) -> Response[OrderBook, object]:
    if 'data' not in data:
        raise ResponseError(data)

    data = data['data']
    return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in data['asks']],
                                   bids=[Order(price=bid[0], volume=bid[1]) for bid in data['bids']],
                                   ),
                    response_object=response,
                    )


def _deserialize_trades(data, response) -> Response[list[Trade], object]:
    if 'data' not in data:
        raise ResponseError(data)

    data = data['data']
    return Response(data=[Trade(id=trade.get('tradeId'),
                                price=trade.get('price'),
                                quantity=trade.get('size'),
                                side=Side.BUY if trade.get('side') == 'buy' else Side.SELL,
                                time=trade.get('ts'),
                                ) for trade in data],
                    response_object=response,
                    )


def _deserialize_ticker(data, response) -> Response[list[Ticker], object]:
    if 'data' not in data:
        raise ResponseError(data)

    data = data['data']
    return Response(data=[Ticker(symbol=ticker.get('symbol'),
                                 openPrice=ticker.get('open'),
                                 highPrice=ticker.get('high24h'),
                                 lowPrice=ticker.get('low24h'),
                                 lastPrice=ticker.get('lastPr'),
                                 volume=ticker.get('baseVolume'),
                                 quoteVolume=ticker.get('quoteVolume'),
                                 closeTime=ticker.get('ts'),
                                 ) for ticker in data],
                    response_object=response,
                    )


def _deserialize_symbols(data, response) -> Response[list[Symbol], object]:
    if 'data' not in data:
        raise ResponseError(data)

    data = data['data']
    return Response(data=[Symbol(symbol=i['symbol'],
                                 minQty=i['minTradeAmount'],
                                 maxQty=i['maxTradeAmount'],
                                 status=i['status'],
                                 ) for i in data], response_object=response)


def _deserialize_kline(data, response) -> Response[list[Kline], object]:
    if 'data' not in data:
        raise ResponseError(data)

    data = data['data']
    return Response(data=[Kline(openTime=i[0],
                                openPrice=i[1],
                                highPrice=i[2],
                                lowerPrice=i[3],
                                closePrice=i[4],
                                # transactionPrice=i[5],
                                closeTime=int(time.time()),
                                amount=i[5]
                                ) for i in data],
                    response_object=response)


def _serialize_balance(data, response) -> Response[list[Balance], object]:
    if 'data' not in data:
        raise Exception(data)
    data = data['data']
    return Response(data=[Balance(asset=i['coin'],
                                  free=i['available'],
                                  locked=i['frozen']
                                  ) for i in data],
                    response_object=response,
                    )
