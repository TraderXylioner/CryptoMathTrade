from ..errors import ResponseError
from ...types import OrderBook, Trade, Ticker, Order, Side, Symbol, Kline
from .._response import Response
from ...types.account import Balance


def _deserialize_depth(data, response) -> Response[OrderBook, object]:
    if not data:
        raise ResponseError(data)

    return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in data['asks']],
                                   bids=[Order(price=bid[0], volume=bid[1]) for bid in data['bids']],
                                   ),
                    response_object=response,
                    )


def _deserialize_trades(data, response) -> Response[list[Trade], object]:
    if not data:
        raise ResponseError(data)

    return Response(data=[Trade(id=trade.get('id'),
                                price=trade.get('price'),
                                quantity=trade.get('qty'),
                                side=Side.SELL if trade.get('isBuyerMaker') else Side.BUY,
                                time=trade.get('time'),
                                ) for trade in data],
                    response_object=response,
                    )


def _deserialize_ticker(data, response) -> Response[list[Ticker], object]:
    if isinstance(data, list):
        data = [Ticker(**ticker) for ticker in data]
    elif isinstance(data, dict):
        data = [Ticker(**data)]
    else:
        raise ResponseError(data)

    return Response(data=data, response_object=response)


def _deserialize_symbols(data, response) -> Response[list[Symbol], object]:
    if not data:
        raise ResponseError(data)

    data = data['data']
    return Response(data=[Symbol(symbol=i.get('symbol'),
                                 firstCoin=i.get('symbol').split('_')[0],
                                 secondCoin=i.get('symbol').split('_')[1],
                                 minQty=i.get('min_amount'),
                                 maxQty=i.get('max_amount'),
                                 status=i.get('state'),
                                 ) for i in data], response_object=response)


def _deserialize_kline(data, response) -> Response[list[Kline], object]:
    if not data:
        raise ResponseError(data)

    return Response(data=[Kline(openTime=i[0],
                                openPrice=i[1],
                                highPrice=i[2],
                                lowerPrice=i[3],
                                closePrice=i[4],
                                closeTime=i[6],
                                amount=i[5]
                                ) for i in data],
                    response_object=response)


def _serialize_balance(data, response):
    if 'balances' not in data:
        raise Exception(data)
    return Response(data=[Balance(**i) for i in data['balances']],
                    response_object=response,
                    )


def _serialize_depth_for_ws(data, response):
    return Response(data=OrderBook(asks=[Order(price=ask['p'], volume=ask['v']) for ask in data['asks']],
                                   bids=[Order(price=bid['p'], volume=bid['v']) for bid in data['bids']],
                                   ),
                    response_object=response,
                    )


def _serialize_trades_for_ws(data, response):
    return Response(data=[Trade(id=trade.get('id', None),
                                price=trade.get('p'),
                                quantity=trade.get('v'),
                                side=Side.BUY if trade.get('S') == 1 else Side.SELL,
                                time=trade.get('t'),
                                ) for trade in data],
                    response_object=response,
                    )
