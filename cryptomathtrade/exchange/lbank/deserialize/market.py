from ..._response import Response
from .utils import validate_data
from ....types import OrderBook, Order, Ticker


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
def deserialize_ticker(data, response) -> Response[list[Ticker], object]:
    data = data["data"]
    return Response(
        data=[
            Ticker(
                symbol=ticker["symbol"],
                firstCoin=ticker["symbol"].split("_")[0],
                secondCoin=ticker["symbol"].split("_")[1],
                highPrice=ticker["ticker"]["high"],
                lowPrice=ticker["ticker"]["low"],
                lastPrice=ticker["ticker"]["latest"],
                volume=ticker["ticker"]["vol"],
            )
            for ticker in data
        ],
        response_object=response,
    )
