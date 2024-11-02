from .utils import validate_data
from ..._response import Response
from ....types import (
    OrderBook,
    Trade,
    Ticker,
    Order,
    Side,
    Kline,
    Symbol,
)


@validate_data
def deserialize_depth(data, response) -> Response[OrderBook, object]:
    data = data["data"]
    data["asks"] = data["asks"][::-1]
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
                id=trade.get("id"),
                price=trade.get("price"),
                quantity=trade.get("qty"),
                side=Side.SELL if trade.get("buyerMaker") else Side.BUY,
                time=trade.get("time"),
            )
            for trade in data
        ],
        response_object=response,
    )


@validate_data
def deserialize_ticker(data, response) -> Response[list[Ticker], object]:
    data = data["data"]
    return Response(
        data=[
            Ticker(
                symbol=ticker.get("symbol"),
                priceChange=ticker.get("priceChange"),
                priceChangePercent=ticker.get("priceChangePercent")[:-1],
                openPrice=ticker.get("openPrice"),
                highPrice=ticker.get("highPrice"),
                lowPrice=ticker.get("lowPrice"),
                lastPrice=ticker.get("lastPrice"),
                volume=ticker.get("volume"),
                quoteVolume=ticker.get("quoteVolume"),
                openTime=ticker.get("openTime"),
                closeTime=ticker.get("closeTime"),
            )
            for ticker in data
        ],
        response_object=response,
    )


@validate_data
def deserialize_symbols(data, response) -> Response[list[Symbol], object]:
    data = data["data"]
    return Response(
        data=[Symbol(**i) for i in data["symbols"]],
        response_object=response,
    )


@validate_data
def deserialize_kline(data, response) -> Response[list[Kline], object]:
    data = data["data"]
    return Response(
        data=[
            Kline(
                openTime=i[0],
                openPrice=i[1],
                highPrice=i[2],
                lowerPrice=i[3],
                closePrice=i[4],
                # transactionPrice=i[5],
                closeTime=i[6],
                amount=i[7],
            )
            for i in data
        ],
        response_object=response,
    )


@validate_data
def deserialize_trades_for_ws(data, response) -> Response[list[Trade], object]:
    data = data["data"]
    return Response(
        data=[
            Trade(
                id=data.get("t"),
                price=data.get("p"),
                quantity=data.get("q"),
                side=Side.SELL if data.get("m") else Side.BUY,
                time=data.get("T"),
            )
        ],
        response_object=response,
    )
