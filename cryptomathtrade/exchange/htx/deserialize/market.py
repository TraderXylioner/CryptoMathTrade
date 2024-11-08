import time

from .utils import validate_data
from ...errors import ResponseError
from ..._response import Response
from ....types import OrderBook, Trade, Ticker, Order, Side, Symbol, Kline


def deserialize_depth(data, response) -> Response[OrderBook, object]:
    if not data.get("tick"):
        raise ResponseError(data)

    data = data["tick"]
    return Response(
        data=OrderBook(
            asks=[Order(price=ask[0], volume=ask[1]) for ask in data["asks"]],
            bids=[Order(price=bid[0], volume=bid[1]) for bid in data["bids"]],
        ),
        response_object=response,
    )


@validate_data
def deserialize_trades(data, response) -> Response[list[Trade], object]:
    data = data["data"]
    return Response(
        data=[
            Trade(
                id=trade["data"][0].get("trade-id"),
                price=trade["data"][0].get("price"),
                quantity=trade["data"][0].get("amount"),
                side=(
                    Side.BUY
                    if trade["data"][0].get("direction") == "buy"
                    else Side.SELL
                ),
                time=trade["data"][0].get("ts"),
            )
            for trade in data
        ],
        response_object=response,
    )


@validate_data
def deserialize_ticker(data, symbol, response) -> Response[list[Ticker], object]:
    if data.get("data"):
        data = [
            Ticker(
                symbol=ticker.get("symbol"),
                openPrice=ticker.get("open"),
                highPrice=ticker.get("high"),
                lowPrice=ticker.get("low"),
                lastPrice=ticker.get("close"),
                volume=ticker.get("amount"),
                quoteVolume=ticker.get("vol"),
                closeTime=data.get("ts"),
            )
            for ticker in data["data"]
        ]
    elif data.get("tick"):
        tick = data["tick"]
        data = [
            Ticker(
                symbol=symbol,
                openPrice=tick.get("open"),
                highPrice=tick.get("high"),
                lowPrice=tick.get("low"),
                lastPrice=tick.get("close"),
                volume=tick.get("amount"),
                quoteVolume=tick.get("vol"),
                closeTime=data.get("ts"),
            )
        ]
    else:
        raise ResponseError(data)

    return Response(data=data, response_object=response)


@validate_data
def deserialize_symbols(data, response) -> Response[list[Symbol], object]:
    data = data["data"]
    return Response(
        data=[
            Symbol(
                symbol=i.get("sc"),
                firstCoin=i.get("bc"),
                secondCoin=i.get("qc"),
                status=i.get("state"),
                timeOnline=i.get("toa"),
            )
            for i in data
        ],
        response_object=response,
    )


@validate_data
def deserialize_kline(data, response) -> Response[list[Kline], object]:
    data = data["data"]
    return Response(
        data=[
            Kline(
                openTime=i.get("id"),
                openPrice=i.get("open"),
                highPrice=i.get("high"),
                lowerPrice=i.get("low"),
                closePrice=i.get("close"),
                closeTime=int(time.time()),
                amount=i.get("amount"),
            )
            for i in data
        ],
        response_object=response,
    )
