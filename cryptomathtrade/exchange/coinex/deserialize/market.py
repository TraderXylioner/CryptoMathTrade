from ..._response import Response
from .utils import validate_data
from ....types import OrderBook, Order, Ticker


@validate_data
def deserialize_depth(data, response) -> Response[OrderBook, object]:
    data = data["data"]['depth']
    return Response(
        data=OrderBook(
            asks=[Order(price=ask[0], volume=ask[1]) for ask in data["asks"]],
            bids=[Order(price=bid[0], volume=bid[1]) for bid in data["bids"]],
        ),
        response_object=response,
    )
