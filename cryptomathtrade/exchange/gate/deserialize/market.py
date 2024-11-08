import time

from .utils import validate_data
from ..._response import Response
from ....types import OrderBook, Order, Trade, Side, Ticker, Symbol, Kline


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
                quantity=trade.get("amount"),
                side=Side.BUY if trade.get("side") == "buy" else Side.SELL,
                time=trade.get("create_time"),
            )
            for trade in data
        ],
        response_object=response,
    )


@validate_data
def deserialize_ticker(data, response) -> Response[list[Ticker], object]:
    return Response(
        data=[
            Ticker(
                symbol=ticker.get("currency_pair"),
                openPrice=float(ticker.get("last"))
                / (1 + float(ticker.get("change_percentage")) / 100),
                highPrice=ticker.get("high_24h"),
                lowPrice=ticker.get("low_24h"),
                lastPrice=ticker.get("last"),
                volume=ticker.get("base_volume"),
                quoteVolume=ticker.get("quote_volume"),
                closeTime=int(time.time()),
            )
            for ticker in data
        ],
        response_object=response,
    )


@validate_data
def deserialize_symbols(data, response) -> Response[list[Symbol], object]:
    return Response(
        data=[
            Symbol(
                symbol=i.get("id"),
                firstCoin=i.get("base"),
                secondCoin=i.get("quote"),
                minQty=i.get("min_quote_amount"),
                maxQty=i.get("max_quote_amount"),
                status=i.get("trade_status"),
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
                openPrice=i[5],
                highPrice=i[3],
                lowerPrice=i[4],
                closePrice=i[2],
                closeTime=int(time.time()),
                amount=i[6],
            )
            for i in data
        ],
        response_object=response,
    )
