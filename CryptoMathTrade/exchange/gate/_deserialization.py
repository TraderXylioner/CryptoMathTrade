import time

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
                                quantity=trade.get('amount'),
                                side=Side.BUY if trade.get('side') == 'buy' else Side.SELL,
                                time=trade.get('create_time'),
                                ) for trade in data],
                    response_object=response,
                    )


def _deserialize_ticker(data, response) -> Response[list[Ticker], object]:
    if not data:
        raise ResponseError(data)

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


def _deserialize_symbols(data, response) -> Response[list[Symbol], object]:
    if not data:
        raise ResponseError(data)

    return Response(data=[Symbol(symbol=i.get('id'),
                                 firstCoin=i.get('base'),
                                 secondCoin=i.get('quote'),
                                 minQty=i.get('min_quote_amount'),
                                 maxQty=i.get('max_quote_amount'),
                                 status=i.get('trade_status'),
                                 ) for i in data], response_object=response)


def _deserialize_kline(data, response) -> Response[list[Kline], object]:
    if not data:
        raise ResponseError(data)

    return Response(data=[Kline(openTime=i[0],
                                openPrice=i[5],
                                highPrice=i[3],
                                lowerPrice=i[4],
                                closePrice=i[2],
                                closeTime=int(time.time()),
                                amount=i[6]
                                ) for i in data],
                    response_object=response)


def _serialize_balance(data, response):
    return Response(data=[Balance(asset=i['currency'],
                                  free=i['available'],
                                  locked=i['locked'],
                                  ) for i in data],
                    response_object=response,
                    )
