from ..._response import Response
from ....types import (
    OrderBook,
    Trade,
    Ticker,
    Order,
    Side,
    Symbol,
    Kline,
)


def deserialize_depth(data, response) -> Response[OrderBook, object]:
    return Response(
        data=OrderBook(
            asks=[Order(price=ask[0], volume=ask[1]) for ask in data["asks"]],
            bids=[Order(price=bid[0], volume=bid[1]) for bid in data["bids"]],
        ),
        response_object=response,
    )


def deserialize_trades(data, response) -> Response[list[Trade], object]:
    return Response(
        data=[
            Trade(
                id=trade.get("id"),
                price=trade.get("price"),
                quantity=trade.get("qty"),
                side=Side.SELL if trade.get("isBuyerMaker") else Side.BUY,
                time=trade.get("time"),
            )
            for trade in data
        ],
        response_object=response,
    )


def deserialize_ticker(data, response) -> Response[list[Ticker], object]:
    if isinstance(data, list):
        data = [Ticker(**ticker) for ticker in data]
    elif isinstance(data, dict):
        data = [Ticker(**data)]
    else:
        raise Exception(data)

    return Response(data=data, response_object=response)


def deserialize_symbols(data, response) -> Response[list[Symbol], object]:
    # TODO:
    return Response(data=data, response_object=response)


def deserialize_kline(data, response) -> Response[list[Kline], object]:
    # TODO:
    return Response(data=data, response_object=response)


def deserialize_trades_for_ws(data, response) -> Response[list[Trade], object]:
    return Response(
        data=Trade(
            id=data.get("E"),
            price=data.get("p"),
            quantity=data.get("q"),
            side=Side.SELL if data.get("m") else Side.BUY,
            time=data.get("T"),
        ),
        response_object=response,
    )
