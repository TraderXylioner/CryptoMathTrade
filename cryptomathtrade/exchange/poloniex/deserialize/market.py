from ..._response import Response
from .utils import validate_data
from ....types import OrderBook, Order, Ticker


@validate_data
def deserialize_depth(data, response) -> Response[OrderBook, object]:
    def chunk_pairs(arr):
        return [(arr[i], arr[i + 1]) for i in range(0, len(arr), 2)]

    data = data
    asks = chunk_pairs(data["asks"])
    bids = chunk_pairs(data["bids"])

    return Response(
        data=OrderBook(
            asks=[Order(price=ask[0], volume=ask[1]) for ask in asks],
            bids=[Order(price=bid[0], volume=bid[1]) for bid in bids],
        ),
        response_object=response,
    )
