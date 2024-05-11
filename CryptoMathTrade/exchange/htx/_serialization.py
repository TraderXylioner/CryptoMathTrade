from ...types import OrderBook, Trade, Ticker, Order, Side
from .._response import Response


def _serialize_depth(data, response):
    return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in data['asks']],
                                   bids=[Order(price=bid[0], volume=bid[1]) for bid in data['bids']],
                                   ),
                    response_object=response,
                    )


def _serialize_trades(data, response):
    return Response(data=[Trade(id=trade['data'][0].get('trade-id'),
                                price=trade['data'][0].get('price'),
                                quantity=trade['data'][0].get('amount'),
                                side=Side.BUY if trade['data'][0].get('direction') == 'buy' else Side.SELL,
                                time=trade['data'][0].get('ts'),
                                ) for trade in data],
                    response_object=response,
                    )


def _serialize_trades_for_ws(data, response):
    return Response(data=[Trade(id=trade.get('tradeId'),
                                price=trade.get('price'),
                                quantity=trade.get('amount'),
                                side=Side.BUY if trade.get('direction') == 'buy' else Side.SELL,
                                time=trade.get('ts'),
                                ) for trade in data],
                    response_object=response,
                    )


def _serialize_ticker(data, symbol, response):
    json_data = data['tick'] if symbol else data['data']
    if isinstance(json_data, list):
        data = [Ticker(symbol=ticker.get('symbol'),
                       openPrice=ticker.get('open'),
                       highPrice=ticker.get('high'),
                       lowPrice=ticker.get('low'),
                       lastPrice=ticker.get('close'),
                       volume=ticker.get('amount'),
                       quoteVolume=ticker.get('vol'),
                       closeTime=data.get('ts'),
                       ) for ticker in json_data]
    elif isinstance(json_data, dict):
        data = [Ticker(symbol=symbol,
                       openPrice=json_data.get('open'),
                       highPrice=json_data.get('high'),
                       lowPrice=json_data.get('low'),
                       lastPrice=json_data.get('close'),
                       volume=json_data.get('amount'),
                       quoteVolume=json_data.get('vol'),
                       closeTime=data.get('ts'),
                       )]
    else:
        raise Exception(json_data)

    return Response(data=data, response_object=response)
