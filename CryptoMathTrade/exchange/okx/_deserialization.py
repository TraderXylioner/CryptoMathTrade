import time

from ..errors import ResponseError
from ...types import OrderBook, Trade, Ticker, Order, Side, Symbol, Kline
from .._response import Response
from ...types.account import Balance


def _deserialize_depth(data, response) -> Response[OrderBook, object]:
    if not data.get('data'):
        raise ResponseError(data)

    data = data['data'][0]
    return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in data['asks']],
                                   bids=[Order(price=bid[0], volume=bid[1]) for bid in data['bids']],
                                   ),
                    response_object=response,
                    )


def _serialize_trades(data, response) -> Response[list[Trade], object]:
    if not data.get('data'):
        raise ResponseError(data)

    data = data['data']
    return Response(data=[Trade(id=trade.get('tradeId'),
                                price=trade.get('px'),
                                quantity=trade.get('sz'),
                                side=Side.BUY if trade['side'] == 'buy' else Side.SELL,
                                time=trade.get('ts'),
                                ) for trade in data],
                    response_object=response,
                    )


def _serialize_ticker(data, response) -> Response[list[Ticker], object]:
    if not data.get('data'):
        raise ResponseError(data)

    data = data['data']
    return Response(data=[Ticker(symbol=ticker.get('instId').replace("-SWAP", ""),
                                 openPrice=ticker.get('open24h'),
                                 highPrice=ticker.get('high24h'),
                                 lowPrice=ticker.get('low24h'),
                                 lastPrice=ticker.get('last'),
                                 volume=ticker.get('vol24h'),
                                 quoteVolume=ticker.get('volCcy24h'),
                                 closeTime=ticker.get('ts'),
                                 ) for ticker in data], response_object=response)


def _deserialize_symbols(data, response) -> Response[list[Symbol], object]:
    if not data.get('data'):
        raise ResponseError(data)

    data = data['data']
    return Response(data=[Symbol(symbol=i.get('instId'),
                                 firstCoin=i.get('baseCcy'),
                                 secondCoin=i.get('quoteCcy'),
                                 minQty=i.get('minSz'),
                                 maxQty=i.get('maxTwapSz'),
                                 status=i.get('state'),
                                 timeOnline=i.get('listTime'),
                                 ) for i in data], response_object=response)


def _deserialize_kline(data, response) -> Response[list[Kline], object]:
    if not data.get('data'):
        raise ResponseError(data)

    data = data['data']
    return Response(data=[Kline(openTime=i[0],
                                openPrice=i[1],
                                highPrice=i[2],
                                lowerPrice=i[3],
                                closePrice=i[4],
                                closeTime=int(time.time()),
                                amount=i[5]
                                ) for i in data],
                    response_object=response)


def _serialize_balance(data, response):
    if 'data' not in data:
        raise Exception(data)
    return Response(data=[Balance(asset=i['ccy'],
                                  free=i['availBal'],
                                  locked=i['frozenBal']) for i in data['data'][0]['details']],
                    response_object=response,
                    )
