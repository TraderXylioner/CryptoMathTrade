from .utils import validate_data
from ..._response import Response
from ....types import FullOrder


@validate_data
def deserialize_order(data, response) -> Response[FullOrder, object]:
    data = data["data"]
    return Response(data=FullOrder(**data), response_object=response)


@validate_data
def deserialize_orders(data, response) -> Response[list[FullOrder], object]:
    data = data["data"]
    return Response(
        data=[FullOrder(**i) for i in data["orders"]] if data["orders"] else [],
        response_object=response,
    )
