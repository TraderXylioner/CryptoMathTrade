import time

from .utils import validate_data
from ...errors import ResponseError
from ..._response import Response
from ....types import OrderBook, Trade, Ticker, Order, Side, Symbol, Kline


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
                price=trade[2],
                quantity=trade[3],
                side=Side.BUY if trade[4] == "buy" else Side.SELL,
                time=trade[1],
            )
            for trade in data
        ],
        response_object=response,
    )


@validate_data
def deserialize_ticker(data, response) -> Response[list[Ticker], object]:
    data = data["data"]
    if isinstance(data, list):
        data = [
            Ticker(
                symbol=ticker[0],
                openPrice=ticker[4],
                highPrice=ticker[5],
                lowPrice=ticker[6],
                lastPrice=ticker[1],
                volume=ticker[2],
                quoteVolume=ticker[3],
                closeTime=ticker[12],
            )
            for ticker in data
        ]
    elif isinstance(data, dict):
        data = [
            Ticker(
                symbol=data.get("symbol"),
                openPrice=data.get("open_24h"),
                highPrice=data.get("high_24h"),
                lowPrice=data.get("low_24h"),
                lastPrice=data.get("last"),
                volume=data.get("v_24h"),
                quoteVolume=data.get("qv_24h"),
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
                id=i["symbol_id"],
                symbol=i["symbol"],
                firstCoin=i["base_currency"],
                secondCoin=i["quote_currency"],
                minQty=i["base_min_size"],
                status=i["trade_status"],
            )
            for i in data["symbols"]
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


@validate_data
def deserialize_trades_for_ws(data, response):
    data = data["data"]
    return Response(
        data=[
            Trade(
                price=trade.get("price"),
                quantity=trade.get("size"),
                side=Side.BUY if trade.get("side") == "buy" else Side.SELL,
                time=trade.get("s_t"),
            )
            for trade in data
        ],
        response_object=response,
    )
