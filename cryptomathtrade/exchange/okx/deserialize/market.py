import time

from ..._response import Response
from .utils import validate_data
from ....types import OrderBook, Trade, Order, Ticker, Side, Symbol, Kline


@validate_data
def deserialize_depth(data, response) -> Response[OrderBook, object]:
    data = data["data"][0]
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
                id=trade.get("tradeId"),
                price=trade.get("px"),
                quantity=trade.get("sz"),
                side=Side.BUY if trade["side"] == "buy" else Side.SELL,
                time=trade.get("ts"),
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
                symbol=ticker.get("instId").replace("-SWAP", ""),
                openPrice=ticker.get("open24h"),
                highPrice=ticker.get("high24h"),
                lowPrice=ticker.get("low24h"),
                lastPrice=ticker.get("last"),
                volume=ticker.get("vol24h"),
                quoteVolume=ticker.get("volCcy24h"),
                closeTime=ticker.get("ts"),
            )
            for ticker in data
        ],
        response_object=response,
    )


@validate_data
def deserialize_symbols(data, response) -> Response[list[Symbol], object]:
    data = data["data"]
    return Response(
        data=[
            Symbol(
                symbol=i.get("instId"),
                firstCoin=i.get("baseCcy"),
                secondCoin=i.get("quoteCcy"),
                minQty=i.get("minSz"),
                maxQty=i.get("maxTwapSz"),
                status=i.get("state"),
                timeOnline=i.get("listTime"),
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
                openTime=i[0],
                openPrice=i[1],
                highPrice=i[2],
                lowerPrice=i[3],
                closePrice=i[4],
                closeTime=int(time.time()),
                amount=i[5],
            )
            for i in data
        ],
        response_object=response,
    )
