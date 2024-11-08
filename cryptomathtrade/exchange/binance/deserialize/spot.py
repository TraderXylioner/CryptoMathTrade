from ....types import FullOrder
from ..._response import Response


def deserialize_order(data, response) -> Response[FullOrder, object]:
    return Response(data=FullOrder(**data), response_object=response)


def deserialize_orders(data, response) -> Response[list[FullOrder], object]:
    return Response(data=[FullOrder(**i) for i in data], response_object=response)
