from ..._response import Response
from ....types import (
    OrderBook,
    Order,
)


def deserialize_depth(data, response) -> Response[OrderBook, object]:
    data = data["result"]
    return Response(
        data=OrderBook(
            asks=[Order(price=ask[0], volume=ask[1]) for ask in data["a"]],
            bids=[Order(price=bid[0], volume=bid[1]) for bid in data["b"]],
        ),
        response_object=response,
    )
