from ..._response import Response
from .utils import validate_data
from ....types import OrderBook, Order, Ticker


@validate_data
def deserialize_depth(data, response) -> Response[OrderBook, object]:
    data = data["data"]
    return Response(
        data=OrderBook(
            asks=[
                Order(price=ask["price"], volume=ask["volume"]) for ask in data["asks"]
            ],
            bids=[
                Order(price=bid["price"], volume=bid["volume"]) for bid in data["bids"]
            ],
        ),
        response_object=response,
    )
