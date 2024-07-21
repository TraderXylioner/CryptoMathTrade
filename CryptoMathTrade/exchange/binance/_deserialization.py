from ...types import OrderBook, Trade, Ticker, Order, Side, FullOrder, Symbol, Kline
from .._response import Response
from ...types.account import Balance, DepositAddress, Coin, DepositHistory, WithdrawHistory, Withdraw


def _deserialize_depth(data, response) -> Response[OrderBook, object]:
    return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in data['asks']],
                                   bids=[Order(price=bid[0], volume=bid[1]) for bid in data['bids']],
                                   ),
                    response_object=response,
                    )


def _deserialize_trades(data, response) -> Response[list[Trade], object]:
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
        raise Exception(data)

    return Response(data=data, response_object=response)


def _deserialize_symbols(data, response) -> Response[list[Symbol], object]:
    # TODO:
    return Response(data=data, response_object=response)


def _deserialize_kline(data, response) -> Response[list[Kline], object]:
    # TODO:
    return Response(data=data, response_object=response)


def _deserialize_trades_for_ws(data, response) -> Response[list[Trade], object]:
    return Response(data=Trade(id=data.get('E'),
                               price=data.get('p'),
                               quantity=data.get('q'),
                               side=Side.SELL if data.get('m') else Side.BUY,
                               time=data.get('T'),
                               ),
                    response_object=response,
                    )


def _deserialize_balance(data, response) -> Response[list[Balance], object]:
    return Response(data=[Balance(**i) for i in data], response_object=response)


def _deserialize_order(data, response) -> Response[FullOrder, object]:
    return Response(data=FullOrder(**data), response_object=response)


def _deserialize_orders(data, response) -> Response[list[FullOrder], object]:
    return Response(data=[FullOrder(**i) for i in data], response_object=response)


def _deserialize_coins(data, response) -> Response[list[Coin], object]:
    return Response(data=[Coin(**i) for i in data], response_object=response)


def _deserialize_deposit_address(data, response) -> Response[list[DepositAddress], object]:
    return Response(data=[DepositAddress(**data)], response_object=response)


def _deserialize_withdraw(data, response) -> Response[Withdraw, object]:
    return Response(data=Withdraw(**data), response_object=response)


def _deserialize_deposit_history(data, response) -> Response[list[DepositHistory], object]:
    return Response(data=[DepositHistory(**i) for i in data], response_object=response)


def _deserialize_withdraw_history(data, response) -> Response[list[WithdrawHistory], object]:
    return Response(data=[WithdrawHistory(**i) for i in data], response_object=response)
