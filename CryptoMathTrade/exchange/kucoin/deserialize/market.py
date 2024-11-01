import time

from .utils import validate_data
from ..._response import Response
from CryptoMathTrade.types import OrderBook, Trade, Ticker, Order, Side, Symbol, Kline


@validate_data
def deserialize_depth(data, response) -> Response[OrderBook, object]:
    data = data["data"]
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
                id=trade.get("sequence"),
                price=trade.get("price"),
                quantity=trade.get("size"),
                side=Side.BUY if trade.get("side") == "buy" else Side.SELL,
                time=trade.get("time"),
            )
            for trade in data
        ],
        response_object=response,
    )


@validate_data
def deserialize_ticker(data, response) -> Response[list[Ticker], object]:
    data = data["data"]
    if data.get("ticker"):
        full_json_data = data
        json_data = data["ticker"]
        data = [
            Ticker(
                symbol=ticker.get("symbol"),
                openPrice=(
                    float(ticker.get("last")) - float(ticker.get("changePrice"))
                    if ticker.get("last") and ticker.get("changePrice")
                    else None
                ),
                highPrice=ticker.get("high"),
                lowPrice=ticker.get("low"),
                lastPrice=ticker.get("last"),
                volume=ticker.get("vol"),
                quoteVolume=ticker.get("volValue"),
                closeTime=full_json_data.get("time"),
            )
            for ticker in json_data
        ]

    else:
        data = [
            Ticker(
                symbol=data.get("symbol"),
                openPrice=float(data.get("last")) - float(data.get("changePrice")),
                highPrice=data.get("high"),
                lowPrice=data.get("low"),
                lastPrice=data.get("last"),
                volume=data.get("vol"),
                quoteVolume=data.get("volValue"),
                closeTime=data.get("time"),
            )
        ]

    return Response(data=data, response_object=response)


@validate_data
def deserialize_symbols(data, response) -> Response[list[Symbol], object]:
    data = data["data"]
    return Response(
        data=[
            Symbol(
                id=i.get(""),
                symbol=i.get("symbol"),
                firstCoin=i.get("baseCurrency"),
                secondCoin=i.get("quoteCurrency"),
                minQty=i.get("baseMinSize"),
                maxQty=i.get("baseMaxSize"),
                status=i.get("enableTrading"),
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
                highPrice=i[3],
                lowerPrice=i[4],
                closePrice=i[2],
                closeTime=int(time.time()),
                amount=i[5],
            )
            for i in data
        ],
        response_object=response,
    )
