from ..._response import Response
from ....types import Coin


def deserialize_coins(data: dict, response) -> Response[list[Coin], object]:
    return Response(data=data, response_object=response)
