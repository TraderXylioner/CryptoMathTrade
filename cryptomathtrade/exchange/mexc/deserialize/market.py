from ..._response import Response
from .utils import validate_data
from ....types import OrderBook, Trade, Order, Ticker, Side, Symbol, Kline


@validate_data
def deserialize_depth(data, response) -> Response[OrderBook, object]:
    return Response(
        data=OrderBook(
            asks=[Order(price=ask[0], volume=ask[1]) for ask in data["asks"]],
            bids=[Order(price=bid[0], volume=bid[1]) for bid in data["bids"]],
        ),
        response_object=response,
    )


@validate_data
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


@validate_data
def deserialize_ticker(data, response) -> Response[list[Ticker], object]:
    if isinstance(data, list):
        data = [Ticker(**ticker) for ticker in data]
    elif isinstance(data, dict):
        data = [Ticker(**data)]
    return Response(data=data, response_object=response)


@validate_data
def deserialize_symbols(data, response) -> Response[list[Symbol], object]:
    data = data["data"]
    return Response(
        data=[
            Symbol(
                symbol=i.get("symbol"),
                firstCoin=i.get("symbol").split("_")[0],
                secondCoin=i.get("symbol").split("_")[1],
                minQty=i.get("min_amount"),
                maxQty=i.get("max_amount"),
                status=i.get("state"),
            )
            for i in data
        ],
        response_object=response,
    )


@validate_data
def deserialize_kline(data, response) -> Response[list[Kline], object]:
    return Response(
        data=[
            Kline(
                openTime=i[0],
                openPrice=i[1],
                highPrice=i[2],
                lowerPrice=i[3],
                closePrice=i[4],
                closeTime=i[6],
                amount=i[5],
            )
            for i in data
        ],
        response_object=response,
    )


@validate_data
def deserialize_depth_for_ws(data, response):
    return Response(
        data=OrderBook(
            asks=[Order(price=ask["p"], volume=ask["v"]) for ask in data["asks"]],
            bids=[Order(price=bid["p"], volume=bid["v"]) for bid in data["bids"]],
        ),
        response_object=response,
    )


@validate_data
def deserialize_trades_for_ws(data, response):
    return Response(
        data=[
            Trade(
                id=trade.get("id", None),
                price=trade.get("p"),
                quantity=trade.get("v"),
                side=Side.BUY if trade.get("S") == 1 else Side.SELL,
                time=trade.get("t"),
            )
            for trade in data
        ],
        response_object=response,
    )
