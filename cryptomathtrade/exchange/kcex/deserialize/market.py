from ..._response import Response
from .utils import validate_data
from ....types import OrderBook, Order, Ticker


@validate_data
def deserialize_depth(data, response) -> Response[OrderBook, object]:
    data = data["data"]["data"]
    return Response(
        data=OrderBook(
            asks=[Order(price=ask["p"], volume=ask["q"]) for ask in data["asks"]],
            bids=[Order(price=bid["p"], volume=bid["q"]) for bid in data["bids"]],
        ),
        response_object=response,
    )
