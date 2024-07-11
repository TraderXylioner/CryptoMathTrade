from ..errors import ResponseError
from ...types import OrderBook, Trade, Ticker, Order, Side, Balance, Kline, FullOrder
from .._response import Response
from ...types.symbol import Symbol


def _deserialize_listen_key(data, response):
    if 'listenKey' not in data:
        raise ResponseError(data)
    return Response(data=data['listenKey'], response_object=response)


def _deserialize_depth(data, response):
    if 'msg' in data:
        raise ResponseError(data)

    data = data['data']
    data['asks'] = data['asks'][::-1]
    return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in data['asks']],
                                   bids=[Order(price=bid[0], volume=bid[1]) for bid in data['bids']], ),
                    response_object=response, )


def _deserialize_trades(data, response):
    if 'msg' in data:
        raise ResponseError(data)

    data = data['data']
    return Response(data=[Trade(id=trade.get('id'),
                                price=trade.get('price'),
                                quantity=trade.get('qty'),
                                side=Side.SELL if trade.get('buyerMaker') else Side.BUY,
                                time=trade.get('time'),
                                ) for trade in data],
                    response_object=response, )


def _deserialize_ticker(data, response):
    if 'msg' in data:
        raise ResponseError(data)

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


def _deserialize_kline(data, response):
    if 'msg' in data:
        raise ResponseError(data)

    data = data['data']
    return Response(data=[Kline(openTime=i[0],
                                openPrice=i[1],
                                highPrice=i[2],
                                lowerPrice=i[3],
                                closePrice=i[4],
                                transactionPrice=i[5],
                                closeTime=i[6],
                                amount=i[7]
                                ) for i in data],
                    response_object=response)


def _deserialize_balance(data, response):
    if 'data' not in data:
        raise ResponseError(data)

    return Response(data=[Balance(**i) for i in data['data']['balances']],
                    response_object=response,
                    )


def _deserialize_trades_for_ws(data, response):
    if 'data' not in data:
        raise ResponseError(data)
    data = data['data']
    return Response(data=[Trade(id=data.get('t'),
                                price=data.get('p'),
                                quantity=data.get('q'),
                                side=Side.SELL if data.get('m') else Side.BUY,
                                time=data.get('T'),
                                )],
                    response_object=response,
                    )


def _deserialize_account_update_for_ws(data, response):
    return Response(data=data, response_object=response)


def _deserialize_coins(data, response):
    if 'data' not in data:
        raise ResponseError(data)
    data = data['data']
    return Response(data=data, response_object=response)


def _deserialize_deposit_address(data, response):
    if 'data' not in data:
        raise ResponseError(data)
    data = data['data']
    return Response(data=data, response_object=response)


def _deserialize_withdraw(data, response):
    return Response(data=data, response_object=response)


def _deserialize_deposit_history(data, response):
    return Response(data=data, response_object=response)


def _deserialize_withdraw_history(data, response):
    return Response(data=data, response_object=response)


def _deserialize_symbols(data, response):
    if 'data' not in data:
        raise ResponseError(data)
    data = data['data']
    return Response(data=[Symbol(**i) for i in data['symbols']],
                    response_object=response,
                    )


def _deserialize_order(data, response):
    if 'data' not in data:
        raise ResponseError(data)
    data = data['data']
    return Response(data=FullOrder(**data),
                    response_object=response,
                    )


def _deserialize_orders(data, response):
    if 'data' not in data:
        raise ResponseError(data)
    data = data['data']
    return Response(data=[FullOrder(**i) for i in data['orders']] if data['orders'] else [],
                    response_object=response,
                    )
